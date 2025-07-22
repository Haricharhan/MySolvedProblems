import os
import datetime
import subprocess
import sys

# Function to log messages to log.txt with timestamp
def log_message(message):
    with open("log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")

# Function to run a command and capture output/errors
def run_cmd(cmd_list, timeout=60, description=""):
    try:
        result = subprocess.run(cmd_list, shell=True, capture_output=True, text=True, timeout=timeout)
        if result.returncode == 0:
            if description:
                log_message(f"{description} - Success")
        else:
            log_message(f"{description} - Failed")
            if result.stderr:
                log_message(f"Error: {result.stderr.strip()}")
            sys.exit(1)
        return result
    except subprocess.TimeoutExpired:
        log_message(f"❌ Timeout: {' '.join(cmd_list)}")
        sys.exit(1)
    except Exception as e:
        log_message(f"❌ Error running {' '.join(cmd_list)}: {str(e)}")
        sys.exit(1)

# Start of script
log_message("Auto Git Push Script Started")

# Set repo path
repo_path = r"C:\Users\B.Hari Charhan\OneDrive\Desktop\Python--Alllll\Problems solved"

# Change to repo directory
try:
    os.chdir(repo_path)
    log_message("Changed directory to repo successfully")
except Exception as e:
    log_message(f"❌ Failed to change directory: {str(e)}")
    sys.exit(1)

# Git path
git_path = r"C:\Program Files\Git\bin\git.exe"

# Step 1: Check for changes
status_result = run_cmd([git_path, "status", "--porcelain"], timeout=30, description="Checking git status")
if status_result.stdout.strip() == "":
    log_message("No changes to commit")
    sys.exit(0)
else:
    log_message("Git Status: Found changes")

# Step 2: Stage changes
run_cmd([git_path, "add", "."], timeout=30, description="Staging changes")

# Step 3: Commit changes
commit_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
commit_message = f"Auto-commit for {commit_time}"
run_cmd([git_path, "commit", "-m", commit_message], timeout=30, description=f"Committing with message: {commit_message}")

# Step 4: Push to GitHub
run_cmd([git_path, "push", "origin", "main"], timeout=60, description="Pushing to GitHub")

# Done
log_message("Pushed to GitHub successfully")
