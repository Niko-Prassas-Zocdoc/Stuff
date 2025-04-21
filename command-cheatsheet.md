# Commands Cheat Sheet

A handy collection of frequently used commands for various tools and tasks.

---

## Table of Contents
1. [Vim Shortcuts](#vim-shortcuts)
2. [Git Commands](#git-commands)
3. [AWS Commands](#aws-commands)
4. [Dotnet Commands](#dotnet-commands)
5. [Docker Commands](#docker-commands)
6. [Pants Commands](#pants-commands)
7. [Other Useful Tips](#other-useful-tips)

---

## Vim Shortcuts
- `Ctrl-e` - Scroll down one line (without moving the cursor).
- `Ctrl-y` - Scroll up one line (without moving the cursor).
- `yyp` - Copy and paste the current line.
- `/search_term` - Search for `search_term`.
- `:set nu` - Show line numbers.

---

## Git Commands
- `git status` - Show the status of the repository.
- `git log` - Show commit history.
- `git checkout -b <branch-name>` - Create and switch to a new branch.
- `git pull origin main` - Pull changes from the main branch.
- `git stash` - Temporarily save changes.
- `git remote -v` - View configured remote repositories (like origin, upstream) and their URLs.
- `git clean -fd` - Remove untracked files.  Be careful as this includes a -f for forcing it.
- ``current_branch_name=`git rev-parse --abbrev-ref HEAD` && git fetch origin $current_branch_name && git rebase origin/"$current_branch_name"`` - Rebase remote branch onto local branch (Same branch name)

---

## AWS Commands
- `aws ecr describe-images --repository-name interop-availability-api --image-ids imageTag=fake-latest` - Get latest image tag (replace interop-availability-api with the name of the repository)
- `aws ecr describe-images --repository-name monolith-api-fakes --image-ids imageTag=appointment-api-fake-latest` - Get latest image tag for a monolith api (replace appointment-api with the name of the api)
- `aws lambda list-functions` - List lambda functions
- `aws s3 ls` - List S3 buckets.
- `aws s3 cp file.txt s3://bucket-name/` - Copy a file to an S3 bucket.
- `aws ec2 describe-instances` - Describe EC2 instances.
- `aws sts get-caller-identity --profile ci` - Get caller identity from local command line, make sure your credentials are working as expected

---

## Dotnet Commands
- `dotnet add package [PackageName]` - Update package to the latest version
- `dotnet add package [PackageName] -v [VersionNumber]` - Add specific version of package
- `dotnet list package` - List all packages in current project

---

## Pants Commands
- `$ pants run //cdk:cdk --cdk-profile=ci --cdk-args='--context=zd:skipEcrImageValidation=true --no-change-set'` - See the result of cdk diff against the CI account
- `pants package //cdk:cdk --cdk-profile=ci` - Generate result of cdk synth

---

## Docker Commands
- `docker ps` - List running containers
- `docker images` - List all Docker images
- `docker rm -f $(docker ps -aq)` - Stop and remove all containers in one go
- `docker kill $(docker ps -q)` - Kill all running containers
- `docker rm $(docker ps -a -q)` - Remove all stopped containers
- `docker rmi -f $(docker images -q)` - Remove all images
- `docker system prune -a --volumes` - Remove all unused containers, networks, images, and volumes (most thorough cleanup)

---

## Other Useful Tips
- **Curl Command**:
  - `curl -X GET "https://api.example.com"` - Make a GET request

---

*Feel free to add more commands as you discover new tools or workflows!*
