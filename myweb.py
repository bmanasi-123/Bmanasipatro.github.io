import os
import subprocess
from git import Repo
import requests

# User-specific variables
GITHUB_USERNAME = "bmanasi-123"
GITHUB_TOKEN = ""  
REPO_NAME = f"{GITHUB_USERNAME}.github.io"
GITHUB_REPO_URL = f"https://{GITHUB_USERNAME}:{GITHUB_TOKEN}@github.com/{GITHUB_USERNAME}/{REPO_NAME}.git"

# Step 1: Create a new repository on GitHub (if it doesn't already exist)
# def create_github_repo():
#     headers = {
#         "Authorization": f"token {GITHUB_TOKEN}",
#         "Accept": "application/vnd.github.v3+json"
#     }
#     data = {
#         "name": REPO_NAME,
#         "auto_init": True,  # Initialize with a README
#         "private": False
#     }
#     response = requests.post('https://api.github.com/user/repos', headers=headers, json=data)
#     if response.status_code == 201:
#         print(f"Repository '{REPO_NAME}' created successfully.")
#     elif response.status_code == 422:  # Unprocessable Entity (e.g., repository already exists)
#         print(f"Repository '{REPO_NAME}' already exists.")
#     else:
#         print(f"Failed to create repository: {response.json()}")

# Step 2: Clone the repository
def clone_repo():
    if not os.path.exists(REPO_NAME):
        print(f"Cloning repository from {GITHUB_REPO_URL}...")
        Repo.clone_from(GITHUB_REPO_URL, REPO_NAME)
    else:
        print(f"Repository '{REPO_NAME}' already exists locally.")

# Step 3: Create an index.html file
def create_index_html():
    index_html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Personal Website</title>
    </head>
    <body>
        <h1>Welcome to My Website</h1>
        <p>This is where I showcase my projects and games.</p>
    </body>
    </html>
    """
    with open(os.path.join(REPO_NAME, "index.html"), "w") as file:
        file.write(index_html_content)
    print("index.html file created.")

# Step 4: Commit and push changes to GitHub
def commit_and_push_changes():
    repo = Repo(REPO_NAME)
    repo.git.add(A=True)
    repo.index.commit("Initial commit")
    origin = repo.remote(name='origin')
    origin.push()
    print("Changes pushed to GitHub.")

# Main function to run all steps
def main():
    create_github_repo()
    clone_repo()
    create_index_html()
    commit_and_push_changes()
    print(f"Your website is live at https://{REPO_NAME}")

if __name__ == "__main__":
    main()
