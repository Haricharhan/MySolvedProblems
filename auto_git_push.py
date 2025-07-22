import os
import datetime
import subprocess
import sys

# Function to log messages to log.txt with timestamp
def log_message(message):
    with open("log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(f"{datetime.datetime.now()} - {message}\n")

# Function to run a command and log its output and errors
def run_cmd(cmd_list, timeout=60):
    try:
        result = subprocess.run(cmd_list, shell=True, capture_output=True, text=True, timeout=timeout)
        log_message(f"Running: {' '.join(cmd_list)}")
        if result.stdout:
            log_message(f"STDOUT:\n{result.stdout.strip()}")
        if result.stderr:
            log_message(f"STDERR:\n{result.stderr.strip()}")
        return result
    except subprocess.TimeoutExpired:
        log_message(f"❌ Command timed out: {' '.join(cmd_list)}")
        sys.exit(1)
    except Exception as e:
        log_message(f"❌ Unexpected error: {str(e)}")
        sys.exit(1)

# Log the start of execution
log_message("🚀 Starting auto push script")

# Set the Git repository path
repo_path = r"C:\Users\B.Hari Charhan\OneDrive\Desktop\Python--Alllll\Problems solved"

# Change to the repo directory
try:
    os.chdir(repo_path)
    log_message(f"Changed working directory to: {repo_path}")
except Exception as e:
    log_message(f"❌ Failed to change directory: {str(e)}")
    sys.exit(1)

# Full path to Git executable
git_path = r"C:\Program Files\Git\bin\git.exe"

# Step 1: Check if there are any changes to commit
status_result = run_cmd([git_path, "status", "--porcelain"], timeout=30)
if status_result.stdout.strip() == "":
    log_message("ℹ️ No changes to commit")
    sys.exit(0)

# Step 2: Stage all changes
run_cmd([git_path, "add", "."], timeout=30)

# Step 3: Commit with timestamp message
today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
commit_message = f"✅ Auto-commit for {today}"
run_cmd([git_path, "commit", "-m", commit_message], timeout=30)

# Step 4: Push changes to GitHub
run_cmd([git_path, "push", "origin", "main"], timeout=60)

# Final log entry after successful push
log_message("✅ Changes pushed to GitHub successfully")

sys.exit(0)
