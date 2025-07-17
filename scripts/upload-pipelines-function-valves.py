#!/usr/bin/env python3
import os
import argparse
import json
import requests


def main():
    parser = argparse.ArgumentParser(description='Upload Pipelines function Valves on Open WebUI')
    parser.add_argument('path', 
                       help='Pipeline Valve file path to upload')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.path):
        print(f"Error: File '{args.path}' does not exist", file=sys.stderr)
        sys.exit(1)
    
    if not os.path.isfile(args.path):
        print(f"Error: '{args.path}' is not a file", file=sys.stderr)
        sys.exit(1)
    
    session = requests.Session()

    auth_response = session.post(
        "http://localhost:3000/api/v1/auths/signin",
        json={
            "email": "contact+admin@stephane-klein.info",
            "password": os.environ['OPEN_WEBUI_ADMIN_PASSWORD']
        }
    )
    session.headers.update({"Authorization": f'Bearer {auth_response.json()["token"]}'})

    urlIdx = session.get("http://localhost:3000/api/v1/pipelines/list").json()["data"][0]["idx"]

    with open(args.path, "r") as f:
        pipeline_valves = json.load(f)
        response = session.post(
            f'http://localhost:3000/api/v1/pipelines/{os.path.splitext(pipeline_valves["function_filename"])[0]}/valves/update?urlIdx={urlIdx}',
            json=pipeline_valves["valves"]
        )
        print(response.text)

if __name__ == "__main__":
    main()
