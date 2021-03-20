import sys
import os
import requests



def local_project(path, repo):
    folder_name = str(sys.argv[1])
    folder_path = os.path.join(path, folder_name)

    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    
    try:
        os.chdir(folder_path)
    except:
        print(f"Error changing directory to {folder_path}")
    
    try:
        os.system(f"New-Item {folder_name}/README.md")
    except:
        print(f"Error creatung README.md file")

    try:
        os.system("git init")
        os.system("git add .")
        os.system('git commit -m "Initialize Repo"')
    except:
        print(f"Error intializing local repo")
    
    try:
        os.system(f"git remote add {repo}")
    except:
        print(f"Error associating remote repo")
    
    try:
        os.system("git push origin master")
        print(f"{folder_name} has been created and remote repo added")
    except:
        print(f"Error pushing Initial commit to master branch")

    # Launch VSCODE
    os.system("code .")