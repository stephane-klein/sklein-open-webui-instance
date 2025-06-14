#!/usr/bin/env python3
import http.client
import json
import os
import time
from inspect import cleandoc

conn = http.client.HTTPConnection('localhost', 3000)
conn.request(
    'POST',
    '/api/v1/auths/signin',
    body=json.dumps({
        'email': 'contact+admin@stephane-klein.info',
        'password': os.environ['OPEN_WEBUI_ADMIN_PASSWORD']
    }),
    headers={'Content-Type': 'application/json'}
)
api_key = json.loads(conn.getresponse().read())['token']

conn.request(
    'POST',
    '/api/v1/functions/sync',
    body=json.dumps(
        {
            'id': '',
            'name': '',
            'content': '',
            'meta': {},
            'functions': [
                {
                    'id': 'hello_world2',
                    'user_id': '3aaa0156-3181-403b-bcbd-6047a2988a9d',
                    'name': 'Hello world2',
                    'type': 'pipe',
                    'meta': {},
                    'content': cleandoc("""
                        from pydantic import BaseModel, Field

                        class Pipe:
                            class Valves(BaseModel):
                                pass

                            def __init__(self):
                                self.valves = self.Valves()

                            def pipe(self, body: dict):
                                print("body", body)
                                return "Hello, World!"
                    """),
                    'is_active': True,
                    'is_global': True,
                    'created_at': int(time.time()),
                    'updated_at': int(time.time())
                }
            ]
        }
    ),
    headers={
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
)
response = conn.getresponse()
print(response.read().decode())

