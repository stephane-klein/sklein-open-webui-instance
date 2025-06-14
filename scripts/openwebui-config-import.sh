#!/usr/bin/env bash
set -e
cd "$(dirname "$0")/../"
API_TOKEN="$(./scripts/get-open_webui-api-token.sh)"

CONFIG_DATA=$(cat) # read from stdin
JSON_PAYLOAD=$(jq -n --argjson config "$CONFIG_DATA" '{config: $config}')

echo "$JSON_PAYLOAD" | curl -s -X 'POST' \
  'http://localhost:3000/api/v1/configs/import' \
  -H 'accept: application/json' \
  -H "Authorization: Bearer ${API_TOKEN}" \
  -H 'Content-Type: application/json' \
  -d @-
