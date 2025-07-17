#!/usr/bin/env python3
import requests
import os

pipelines_folder_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "pipelines"
    )
)

session = requests.Session()

auth_response = session.post(
    "http://localhost:3000/api/v1/auths/signin",
    json={
        "email": "contact+admin@stephane-klein.info",
        "password": os.environ['OPEN_WEBUI_ADMIN_PASSWORD']
    }
)
session.headers.update({"Authorization": f'Bearer {auth_response.json()["token"]}'})

with open(os.path.join(pipelines_folder_path, "hello_world.py"), "r") as f:
    response = session.post(
        "http://localhost:3000/api/v1/pipelines/upload",
        files={
            "file": ("hello_world3.py", f, "text/x-python")
        },
        data={
            "urlIdx": "2"
        }
    )
    print(response.text)
