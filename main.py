import sys
import os
import argparse
from typing import Optional, Sequence
from pathlib import Path
from dotenv import load_dotenv
from src.local import local_project as lp
from src.remote import remote_project as rp


def main(argv: Optional[Sequence[str]] = None) -> int:
    
    # Intilaize argparser and set arguments
    parser = argparse.ArgumentParser(description="Necessary GitHub arguments for new Remote and local repo")
    
    parser.add_argument(
        "-v", "--view", 
        default="public",
        choices=("private", "public"),
        type=str,
        help="GitHub view status Public vs Private. (default: %(default)s).",
        )
    
    parser.add_argument(
        "-n", "--projectname", 
        required=True,
        type=str,
        help="Your project Name for Remote and local creation.",
        )

    # Get argpars arguments
    args = parser.parse_args(argv)
    view = args.view
    pn = args.projectname

    # Get base directory this file is in
    env_path = Path(".", ".env")

    # Join path with file name and load_dotenv
    load_dotenv(dotenv_path=env_path)

    # Get .env variables
    un      = os.getenv("NAME")
    fp      = os.getenv("FILEPATH")
    api_url = os.getenv("API_URL")
    token   = os.getenv("TOKEN")
    key     = os.getenv("KEY")

    # Concat Project name to path
    path = fp + "\\" + pn

    # Create remote repo on GitHub and return repo information local repo
    repo = rp(un, api_url, token, pn, view, key)

    # Create local repo in Python folder and connect to remote repo.
    lp(path, repo, pn)



if __name__ == '__main__':
    main()