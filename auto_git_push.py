import os
import datetime
import subprocess

# Set your repo path here
repo_path = r"C:\Users\B.Hari Charhan\OneDrive\Desktop\Python--Alllll\Problems solved"

# Go to your repo directory
os.chdir(repo_path)

# Stage all changes
subprocess.run(["git", "add", "."])

# Commit with today's date
today = datetime.datetime.now().strftime("%Y-%m-%d")
commit_message = f"✅ Auto-commit for {today}"
subprocess.run(["git", "commit", "-m", commit_message])

# Push to GitHub
subprocess.run(["git", "push", "origin", "main"])
