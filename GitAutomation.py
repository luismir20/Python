import subprocess
import os

def push_with_password(repo_directory):
    git_password = os.environ["GIT_PASSWORD"]
    env = os.environ.copy()
    env["GIT_ASKPASS"] = "echo"

    subprocess.run(
        ["git", "push"],
        cwd=repo_directory,
        env=env,
        input=git_password.encode("utf-8"),
        check=True,
    )

msg = "Automated CI/CD update"

repos = [
    {
        "directory": "/Users/fernando/Desktop/Code/Python",
        "url": "git@github.com:luismir20/PythonProjects.git",
    },
    {
        "directory": "/Users/fernando/Desktop/Code/Output",
        "url": "git@github.com:luismir20/FilesOutput.git",
    },
    {
        "directory": "/Users/fernando/Desktop/Code/Sources",
        "url": "git@github.com:luismir20/FilesSources.git",
    },
    {
        "directory": "/Users/fernando/Desktop/Code/Resources",
        "url": "git@github.com:luismir20/Resources.git",
    },
]

for repo in repos:
    repo_directory = repo["directory"]
    repo_url = repo["url"]

    if not os.path.exists(repo_directory):
        subprocess.run(["git", "clone", repo_url, repo_directory])

    subprocess.run(["git", "add", "."], cwd=repo_directory)
    subprocess.run(["git", "commit", "-m", msg], cwd=repo_directory)
    push_with_password(repo_directory)
