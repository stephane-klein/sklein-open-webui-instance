#!/usr/bin/env bash
set -e

cd "$(dirname "$0")/../"

API_TOKEN="$(./scripts/get-open_webui-api-token.sh)"

curl -s -X 'POST' \
  'http://localhost:3000/api/v1/auths/add' \
  -H 'accept: application/json' \
  -H "Authorization: Bearer ${API_TOKEN}" \
  -H 'Content-Type: application/json' \
  -d "{
  \"name\": \"stephane-klein\",
  \"email\": \"contact@stephane-klein.info\",
  \"password\": \"${OPEN_WEBUI_STEPHANE_KLEIN_PASSWORD}\",
  \"profile_image_url\": \"https://sklein.xyz/_app/immutable/assets/avatar.Di4npmkQ.avif\",
  \"role\": \"admin\"
}"
