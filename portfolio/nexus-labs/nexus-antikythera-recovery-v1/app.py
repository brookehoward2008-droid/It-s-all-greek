"""NEXUS Antikythera Recovery - FastAPI Backend

Safe, local-first recovery shell for Universe 42 puzzle exploration.
No private keys, no wallet automation, read-only public data only.
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import sqlite3
import os
from pathlib import Path

app = FastAPI(title="NEXUS Antikythera Recovery", version="0.1.0")

# Initialize SQLite database
DB_PATH = Path(__file__).parent / "nexus.db"

def init_db():
    """Initialize local SQLite database for safe public data storage."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Create tables for public puzzle registry
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS btc_puzzles (
            id INTEGER PRIMARY KEY,
            puzzle_number INTEGER UNIQUE,
            description TEXT,
            difficulty TEXT,
            universe_42_rank INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS address_formats (
            id INTEGER PRIMARY KEY,
            format_name TEXT UNIQUE,
            pattern TEXT,
            example TEXT
        )
    """)
    
    conn.commit()
    conn.close()

# Initialize database on startup
init_db()

@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve the main HUD."""
    hud_path = Path(__file__).parent / "templates" / "hud.html"
    if hud_path.exists():
        return hud_path.read_text()
    return "<h1>NEXUS Antikythera Recovery</h1><p>Loading HUD...</p>"

@app.get("/api/status")
async def status():
    """Read-only status endpoint."""
    return {
        "service": "NEXUS Antikythera Recovery",
        "status": "ready",
        "port": 8731,
        "database": str(DB_PATH),
        "mode": "read-only public data"
    }

@app.get("/api/puzzles")
async def get_puzzles():
    """Get public BTC puzzle registry."""
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM btc_puzzles ORDER BY puzzle_number")
        puzzles = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return {"puzzles": puzzles, "count": len(puzzles)}
    except Exception as e:
        return {"error": str(e), "puzzles": []}

@app.get("/api/formats")
async def get_address_formats():
    """Get address format detection info."""
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM address_formats")
        formats = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return {"formats": formats}
    except Exception as e:
        return {"error": str(e), "formats": []}

@app.get("/api/universe42")
async def universe_42_ranking():
    """Universe 42 normalized scan-ahead ranking (read-only)."""
    return {
        "universe": 42,
        "mode": "planning",
        "message": "Public puzzle ranking available via /api/puzzles"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8731)
