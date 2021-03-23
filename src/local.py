import sys
import os


def local_project(path, repo, pn):

    if not os.path.exists(path):
        os.mkdir(path)
    
    try:
        os.chdir(path)
        os.system("git init")
        os.system("git remote add origin " + repo)
        os.system(f"echo '# {pn}'>> README.md")
        os.system("git add .")
        os.system("git commit -m 'Initialize Repo'")
        os.system("git push origin master")
    except FileExistsError as err:
        raise SystemExit(err)

    # Complete message
    print(f"Local and Remote repository for project {pn} has been created!")

    # Launch VSCODE
    os.system("code .")