import os
import datetime
import subprocess

# Set your Git repo path
repo_path = r"C:\Users\B.Hari Charhan\OneDrive\Desktop\Python--Alllll\Problems solved"
os.chdir(repo_path)

# Stage and commit changes
today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
commit_message = f"✅ Auto-commit for {today}"

# Use full path to Git
git_path = r"C:\Program Files\Git\bin\git.exe"

subprocess.run([git_path, "add", "."], shell=True)
subprocess.run([git_path, "commit", "-m", commit_message], shell=True)
subprocess.run([git_path, "push", "origin", "main"], shell=True)
