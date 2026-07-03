# NEXUS Antikythera Recovery

Local-first, safe recovery shell for Universe 42 puzzle exploration.

## Features

✅ **Safe & Local** - No private keys, no wallet automation, read-only public data only
✅ **FastAPI Backend** - Modern Python async framework on port 8731
✅ **SQLite Storage** - Local data persistence
✅ **Phone-Friendly HUD** - Responsive HTML interface
✅ **Public Puzzle Registry** - BTC puzzle lookup with Universe 42 ranking
✅ **Address Format Detection** - Analyze Bitcoin address formats
✅ **Codespaces Compatible** - Open from iPhone via port forwarding

## Quick Start

### Run the startup script:
```bash
bash nexus.sh
```

This will:
1. Create a Python virtual environment
2. Install dependencies from `requirements.in`
3. Run smoke tests
4. Start the FastAPI server on port 8731

### Manual setup:
```bash
cd portfolio/nexus-labs/nexus-antikythera-recovery-v1
python3 -m venv .venv
source .venv/bin/activate  # or .venv\\Scripts\\activate on Windows
python -m pip install --upgrade pip
pip install -r requirements.in
python tests/smoke_test.py
python -m uvicorn app:app --host 0.0.0.0 --port 8731
```

## API Endpoints

### `GET /`
Serves the main HUD dashboard.

### `GET /api/status`
Returns service status and configuration.
```json
{
  "service": "NEXUS Antikythera Recovery",
  "status": "ready",
  "port": 8731,
  "mode": "read-only public data"
}
```

### `GET /api/puzzles`
Get public BTC puzzle registry with Universe 42 ranking.
```json
{
  "puzzles": [
    {
      "id": 1,
      "puzzle_number": 1,
      "description": "First puzzle",
      "difficulty": "easy",
      "universe_42_rank": 1
    }
  ],
  "count": 1
}
```

### `GET /api/formats`
Get address format detection information.
```json
{
  "formats": [
    {
      "format_name": "P2PKH",
      "pattern": "^1[1-9A-HJ-NP-Z]{25,34}$",
      "example": "1A1z7agoat..."
    }
  ]
}
```

### `GET /api/universe42`
Universe 42 normalized scan-ahead ranking (planning mode).
```json
{
  "universe": 42,
  "mode": "planning",
  "message": "Public puzzle ranking available via /api/puzzles"
}
```

## Architecture

```
portfolio/nexus-labs/nexus-antikythera-recovery-v1/
├── app.py              # FastAPI application
├── requirements.in     # Python dependencies
├── nexus.sh            # Startup script (from parent)
├── tests/
│   └── smoke_test.py   # Integration tests
├── templates/
│   └── hud.html        # Main dashboard UI
├── nexus.db            # SQLite database (generated)
└── .venv/              # Virtual environment (generated)
```

## Development

### Run tests:
```bash
python tests/smoke_test.py
```

### Allowed improvements:
- Frontend responsiveness
- FastAPI route reliability
- Read-only status endpoints
- Public BTC puzzle registry display
- Address format detection
- Universe 42 ranking
- Tests and documentation

### Blocked (security):
- Private-key search or handling
- Wallet sweeping
- Transaction signing or broadcasting
- Seed phrase storage
- Automatic crypto actions
- Hidden API keys in frontend

## Deployment

### Codespaces:
1. Open repository in Codespaces
2. Run `bash nexus.sh`
3. Forward port 8731
4. Open the forwarded URL on iPhone or desktop

### Docker (optional future enhancement):
Currently designed for simple deployment in Codespaces.

## License

Portfolio project - local development only.
