#!/usr/bin/env bash
set -e

cd "$(dirname "$0")/../"

curl \
  -X POST "http://localhost:3000/api/v1/auths/signup" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d "{ \"email\": \"contact+admin@stephane-klein.info\", \"password\": \"${OPEN_WEBUI_ADMIN_PASSWORD}\", \"name\": \"admin\" }"
