import sys
import requests


def remote_project(un, api_url, token, pn, view, key):
    
    # Set privacy flag based on arg for request
    if "private" in view.lower():
        data = f'{{"name": "{pn}", "private": true}}'
    else:
        data = f'{{"name": "{pn}", "private": false}}'
    
    # OAUTH headers for post request
    headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json"
    }

    # Create new Repo on GitHub, raise error if exists.
    try:
        post_req = requests.post(f"{api_url}/user/repos", data=data, headers=headers)
        post_req.raise_for_status()
    except requests.exceptions.RequestException as err:
        raise SystemExit(err)
    
    # Remote repo add for return to local.
    if key.lower() == "ssh":
        repo = f"git@github.com:{un}/{pn}.git"
    elif key.lower() == "https":
        repo = f"https://github.com/{un}/{pn}"
    else:
        sys.exit("Your key for GitHub is not defined as a recognized option \
            in your enviroment variables, please update!")

    return repo