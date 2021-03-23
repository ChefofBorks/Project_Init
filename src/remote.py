import requests


def remote_project(un, pw, api_url, token, pn, view):
    
    # Set privacy flag based on arg for request
    if "private" in view.lower():
        data = '{"name": "' + pn + '", "private": true}'
    else:
        data = '{"name": "' + pn + '", "private": false}'
    
    # OAUTH headers for post request
    headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json"
    }

    # Create new Repo on GitHub, raise error if exists.
    try:
        post_req = requests.post(api_url + "/user/repos", data=data, headers=headers)
        post_req.raise_for_status()
    except requests.exceptions.RequestException as err:
        raise SystemExit(err)
    
    # Remote repo add for return to local
    repo = f"git@github.com:{un}/{pn}.git"

    return repo