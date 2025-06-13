#!/usr/bin/env bash
set -e

cd "$(dirname "$0")/../"

curl -s -X 'POST' \
  'http://localhost:9099/v1/pipelines/reload' \
  -H 'accept: application/json' \
  -H "Authorization: Bearer ${PIPELINES_API_KEY}" \
  -H 'Content-Type: application/json' \
  -d "{}"
