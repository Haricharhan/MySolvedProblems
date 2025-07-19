import os
import datetime
import subprocess
import sys

# Log the execution
with open("log.txt", "a") as log_file:
    log_file.write(f"{datetime.datetime.now()} - Running auto push\n")

# Set your Git repo path
repo_path = r"C:\Users\B.Hari Charhan\OneDrive\Desktop\Python--Alllll\Problems solved"
os.chdir(repo_path)

# Use full path to Git
git_path = r"C:\Program Files\Git\bin\git.exe"

# Check if there are any changes to commit
result = subprocess.run([git_path, "status", "--porcelain"], capture_output=True, text=True)
if result.stdout.strip() == "":
    with open("log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - ℹ️ No changes to commit\n")
    sys.exit()

# Stage and commit changes
today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
commit_message = f"✅ Auto-commit for {today}"

subprocess.run([git_path, "add", "."], shell=True)
subprocess.run([git_path, "commit", "-m", commit_message], shell=True)
subprocess.run([git_path, "push", "origin", "main"], shell=True)

# Log successful push
with open("log.txt", "a") as log_file:
    log_file.write(f"{datetime.datetime.now()} - ✅ Changes pushed to GitHub\n")

sys.exit()
