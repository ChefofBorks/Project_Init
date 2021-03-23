import sys
import os
import argparse
from pathlib import Path
from dotenv import load_dotenv
from src.local import local_project as lp
from src.remote import remote_project as rp


# Get base directory this file is in
env_path = Path(".", ".env")

# Join path with file name and load_dotenv
load_dotenv(dotenv_path=env_path)

# Get .env variables
"""
Enviroment variable arrgs:
NAME        = GitHub username
FILEPATH    = Local machine location for repo storage
API_URL     = GitHub API URL
TOKEN       = GitHub Authentication token
KEY         = GitHub Key setup (HTTPS or SSH URL)
"""
un      = os.getenv("NAME")
fp      = os.getenv("FILEPATH")
api_url = os.getenv("API_URL")
token   = os.getenv("TOKEN")
key     = os.getenv("KEY")

# Get arrgs for repo project setup, exit on error, add in arg parser pieces.////////////////////////
try:
    view    = str(sys.argv[1])
    pn      = str(sys.argv[2])
except IndexError as err:
    # ///////////////Need to update try/except for catching args///////////////////////
    sys.exit("Missing key argumets Repo: --Private/--Public and Project Name")

# Concat Project name to path
path = fp + "\\" + pn

# Create remote repo on GitHub and return repo information local repo
repo = rp(un, api_url, token, pn, view, key)

# Create local repo in Python folder and connect to remote repo.
lp(path, repo, pn)