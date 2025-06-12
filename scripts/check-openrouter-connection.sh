#!/usr/bin/env bash
set -e

cd "$(dirname "$0")/../"

curl -s https://openrouter.ai/api/v1/models \
  -H "Authorization: Bearer $OPENROUTER_API_SECRET_KEY" | jq
