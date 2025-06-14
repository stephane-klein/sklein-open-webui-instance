#!/usr/bin/env python3
import requests
import os
import glob
from inspect import cleandoc

session = requests.Session()
session.headers.update({'Content-Type': 'application/json'})

auth_response = session.post(
    'http://localhost:3000/api/v1/auths/signin',
    json={
        'email': 'contact+admin@stephane-klein.info',
        'password': os.environ['OPEN_WEBUI_ADMIN_PASSWORD']
    }
)
session.headers.update({'Authorization': f'Bearer {auth_response.json()["token"]}'})

for function_file in glob.glob('./functions/*.py'):
    function_id = os.path.splitext(os.path.basename(function_file))[0]
    function_name = function_id.capitalize().replace('_', ' ')
    
    with open(function_file, 'r') as file:
        function_content = file.read()

    function_not_exists = session.get(
        f'http://localhost:3000/api/v1/functions/id/{function_id}'
    ).status_code != 200
    
    if function_not_exists:
        response = session.post(
            'http://localhost:3000/api/v1/functions/create',
            json={
                'id': function_id,
                'name': function_name,
                'meta': {},
                'content': function_content
            }
        )
    else:
        response = session.post(
            f'http://localhost:3000/api/v1/functions/id/{function_id}/update',
            json={
                'id': function_id,
                'name': function_name,
                'meta': {},
                'content': function_content
            }
        )

    if response.status_code != 200:
        print(f"{function_id} sync error")
        print(response.text)
        continue

    response = session.post(
        f'http://localhost:3000/api/v1/functions/id/{function_id}/toggle'
    )
    if response.status_code != 200:
        print(f"{function_id} sync error")
        print(response.text)
        continue

    print(f"{function_id} sync with success")
