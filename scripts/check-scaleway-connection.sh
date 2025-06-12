#!/usr/bin/env bash
set -e

cd "$(dirname "$0")/../"

curl -s https://api.scaleway.ai/355b9bff-ac63-4696-9c10-5f6603f27a68/v1/models \
  -H "Authorization: Bearer $SCALEWAY_GENERATIVE_API_SECRET_KEY" | jq
