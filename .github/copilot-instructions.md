# Copilot instructions for NEXUS Antikythera recovery

Project branch: `nexus-antikythera-recovery-v1`.

## Prime directive

Keep this build safe, local-first, and portfolio-safe. Do not add wallet automation, private-key handling, seed phrase storage, transaction signing, transaction broadcasting, wallet sweeping, or fund movement.

## Current recovery goal

Bring up a visible Codespaces-compatible recovery shell for Brooke's NEXUS Antikythera project.

The expected app surface is:

- FastAPI backend
- SQLite local data store
- phone-friendly HTML HUD
- port `8731`
- safe public puzzle lookup / Universe 42 planning only
- no secrets committed
- no private keys
- no automatic crypto actions

## Run commands

```bash
cd portfolio/nexus-labs/nexus-antikythera-recovery-v1
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python tests/smoke_test.py
python -m uvicorn app:app --host 0.0.0.0 --port 8731
```

Open the forwarded Codespaces port `8731`.

## Safe scope

Allowed:

- Improve frontend responsiveness
- Improve FastAPI route reliability
- Add read-only status endpoints
- Add public BTC puzzle registry display
- Add address format detection
- Add Universe 42 normalized scan-ahead ranking
- Add tests
- Add documentation

Blocked:

- Private-key search execution
- Wallet sweeping
- Transaction signing
- Transaction broadcasting
- Seed phrase storage
- Balance hunting against random wallets
- Hidden API keys in frontend code
- Real trading, posting, claiming, minting, or bridge automation

## Style

Brooke wants practical, direct, working code. Keep the project easy to open from an iPhone through Codespaces. Prioritize a clean visible result over complex automation.
