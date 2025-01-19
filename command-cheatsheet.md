# Commands Cheat Sheet

A handy collection of frequently used commands for various tools and tasks.

---

## Table of Contents
1. [Vim Shortcuts](#vim-shortcuts)
2. [Git Commands](#git-commands)
3. [AWS Commands](#aws-commands)
4. [Other Useful Tips](#other-useful-tips)

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

---

## AWS Commands
- `aws ecr describe-images --repository-name interop-availability-api --image-ids imageTag=fake-latest` - Get latest image tag (replace interop-availability-api with the name of the repository)
- `aws ecr describe-images --repository-name monolith-api-fakes --image-ids imageTag=appointment-api-fake-latest` - Get latest image tag for a monolith api (replace appointment-api with the name of the api)
- `aws s3 ls` - List S3 buckets.
- `aws s3 cp file.txt s3://bucket-name/` - Copy a file to an S3 bucket.
- `aws ec2 describe-instances` - Describe EC2 instances.

---

## Other Useful Tips
- **Curl Command**:
  - `curl -X GET "https://api.example.com"` - Make a GET request.
- **Docker Commands**:
  - `docker ps` - List running containers.
  - `docker images` - List all Docker images.

---

*Feel free to add more commands as you discover new tools or workflows!*
