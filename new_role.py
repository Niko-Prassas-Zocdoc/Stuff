import sys
import os.path
import re
import subprocess
from datetime import datetime

def to_snake_case_lower(string):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()
    
def is_camel_case_with_dots(string):
    """
    Checks if a string is formatted as camel case.
    """
    if not string[0].isalnum():
        return False

    # Check if the string contains only letters and numbers
    if not all(c.isalnum() or c == '.' for c in string):
        return False

    # Check if the string contains at least one uppercase letter
    if not any(c.isupper() for c in string):
        return False

    if not any(c == '.' for c in string):
        return False

    return True

def verify_args():
    if not (sys.version_info.major == 3 and sys.version_info.minor >= 9):
        sys.exit("Error: This script requires Python 3.9 or higher.")

    if len(sys.argv) != 2:
        sys.exit("Wrong, need a command line argument for the role name")

    role_name = sys.argv[1] 
    if not is_camel_case_with_dots(role_name):
        sys.exit("Please enter the role name in camel case with periods where appropriate, as you would want it to appear in sql, like PhoneBot.ReadPhi")

def get_sql_script(new_role_name):
    sql_script = f"""
-- Script generated using https://zocdoc-technology-dashboard-v1.east.zocdoccloud.net/tools/zocdoc/authorization
use zocdoc
go

declare @roleName nvarchar(256) = '{new_role_name}'
if not exists(select 1 from aspnet_Roles where RoleName = @roleName)
begin
    exec aspnet_Roles_CreateRole '/ZocDoc', @roleName
end
"""
    return sql_script


def write_sql_to_scripts_folder(file_path, sql):  
    branch_name = "new_role_6"
    path = os.path.expanduser("~/src/zocdoc_web")
    os.chdir(path)
    subprocess.run(["git", "switch", "master"], check=True)
    # subprocess.run(["git", "switch", "-c", branch_name], check=True)
    subprocess.run(["git", "switch", branch_name], check=True)
    file = open(file_path, "w")
    file.write(sql)
    file.close()
    subprocess.run(["git", "add", "-A"], check=True)
    subprocess.run(["git", "commit", "-m", "Create new role"], check=True)
    subprocess.run(["git", "push"], check=True)

def touch_other_monolith_files(role_name_with_dots):
    base_path = os.path.expanduser("~/src/zocdoc_web")
    role_name = role_name_with_dots.replace(".", "")
    role_name_snake_case = to_snake_case_lower(role_name)

    files_to_touch = [
        (os.path.join(base_path, "ZocDoc.Constants/RoleName.cs"), f"""
// add this
const string {role_name} = "{role_name_with_dots}";
        """),
        (os.path.join(base_path, "ZocDoc.Security/ZocDoc.Security.Impl/JWT/v2/JwtRoleIds.cs"), f"""
// add this, but change the number
public const int {role_name_snake_case} = -12345;
        """),
        (os.path.join(base_path, "ZocDoc.Security/ZocDoc.Security.Impl/JWT/v2/JwtV2ClaimsService.cs"), f"""
// add this to the _roleMapping variable
[RoleName.{role_name}] = JwtRoleIds.{role_name_snake_case},
        """),
        (os.path.join(base_path, "ZocDoc.Security/ZocDoc.Security.Tests/JWT/v2/JwtV2ClaimsServiceTests.cs"), f"""
// add this
(RoleName.{role_name}, JwtRoleIds.{role_name_snake_case}),
        """),
    ]

#    add_role_name_to_csharp_class(files_to_touch[0], role_name, role_name)

    for f, code_to_add in files_to_touch:
        with open(f, 'a') as f:
            f.write(code_to_add)

    subprocess.run(["git", "add", "-A"], check=True)
    subprocess.run(["git", "commit", "-m", "Touch other files"], check=True)
    subprocess.run(["git", "push"], check=True)

def add_role_name_to_csharp_class(file_path, new_const_name, new_const_value):
    # Read the contents of the file
    with open(file_path, 'r') as file:
        content = file.read()

    # Define the pattern to match the class content
    pattern = r'(public static class RoleName\s*{)([^}]*)(})'

    # Find the class content
    match = re.search(pattern, content, re.DOTALL)

    if match:
        # Get the existing class parts
        class_start = match.group(1)
        class_content = match.group(2)
        class_end = match.group(3)

        # Determine the indentation of the last line in class_content
        last_line = class_content.strip().split('\n')[-1]
        indentation = re.match(r'\s*', last_line).group()

        # Create the new const string with matching indentation
        new_const = f'\n{indentation}public const string {new_const_name} = "{new_const_value}";'

        # Add the new const to the class content
        updated_class_content = class_content.rstrip() + new_const

        # Reconstruct the updated class
        updated_class = f'{class_start}{updated_class_content}\n{indentation[:-4]}{class_end}'

        # Replace the old class with the updated one
        updated_content = content.replace(match.group(0), updated_class)

        # Write the updated content back to the file
        with open(file_path, 'w') as file:
            file.write(updated_content)

        print(f"Successfully added {new_const_name} to the RoleName class.")
    else:
        print("RoleName class not found in the file.")

def main():
    verify_args()

    role_name_arg = sys.argv[1]
    role_name = role_name_arg[0].upper() + role_name_arg[1:]
    role_name_snake_case = to_snake_case_lower(role_name)

    script_file_name = f"{datetime.today().strftime('%Y-%m-%d')}_{role_name_snake_case}.sql"
    script_file_path = os.path.join(os.path.expanduser("~/src/zocdoc_web/Database/DataScripts"), script_file_name)
    sql_script = get_sql_script(role_name)

    write_sql_to_scripts_folder(script_file_path, sql_script)
    touch_other_monolith_files(role_name)

    print("SQL Script file:")
    print(script_file_path)

    print("SQL Script:")
    print(sql_script)

if __name__ == "__main__":
    main()

