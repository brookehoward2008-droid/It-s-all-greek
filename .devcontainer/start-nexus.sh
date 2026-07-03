#!/usr/bin/env bash
set -euo pipefail

PORT="${PORT:-8787}"
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$ROOT"

if ! command -v python3 >/dev/null 2>&1; then
  echo "ERROR: python3 is required to run the Nexus static server." >&2
  exit 1
fi

if command -v lsof >/dev/null 2>&1 && lsof -iTCP:"$PORT" -sTCP:LISTEN >/dev/null 2>&1; then
  echo "Nexus is already running on port $PORT."
  exit 0
fi

if command -v ss >/dev/null 2>&1 && ss -ltn | grep -q ":$PORT "; then
  echo "Port $PORT is already in use. Nexus server was not started again."
  exit 0
fi

echo "Starting Nexus on port $PORT from $ROOT"
nohup python3 -m http.server "$PORT" --bind 0.0.0.0 > "$ROOT/.nexus-server.log" 2>&1 &

echo $! > "$ROOT/.nexus-server.pid"
echo "Nexus started. Open the forwarded Codespaces port $PORT."
