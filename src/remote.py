import sys
import os
import requests



def remote_project(un, pw, api_url, token, pn, view):
    headers = {
    "Authorization": "token " + token,
    "Accept": "application/vnd.github.v3+json"
    }

    payload = "{'name':'Test_Name'}"
    req = requests.post(api_url + "/users/repos")

    repo = ""
    
    return repo