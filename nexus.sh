#!/usr/bin/env bash
set -e
cd portfolio/nexus-labs/nexus-antikythera-recovery-v1
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.in
python tests/smoke_test.py
python -m uvicorn app:app --host 0.0.0.0 --port 8731
