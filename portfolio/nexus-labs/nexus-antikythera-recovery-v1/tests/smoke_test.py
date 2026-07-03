"""Smoke tests for NEXUS Antikythera recovery app."""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

import sqlite3
from app import app, DB_PATH, init_db
from fastapi.testclient import TestClient

client = TestClient(app)

def test_app_startup():
    """Test that app initializes without errors."""
    assert app is not None
    print("✓ App startup successful")

def test_database_init():
    """Test that database initializes with required tables."""
    init_db()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Check required tables exist
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='btc_puzzles'"
    )
    assert cursor.fetchone() is not None, "btc_puzzles table not found"
    
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='address_formats'"
    )
    assert cursor.fetchone() is not None, "address_formats table not found"
    
    conn.close()
    print("✓ Database initialization successful")

def test_root_endpoint():
    """Test that root endpoint responds."""
    response = client.get("/")
    assert response.status_code == 200
    print("✓ Root endpoint responds")

def test_status_endpoint():
    """Test that status endpoint returns correct data."""
    response = client.get("/api/status")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ready"
    assert data["port"] == 8731
    assert data["mode"] == "read-only public data"
    print("✓ Status endpoint operational")

def test_puzzles_endpoint():
    """Test that puzzles endpoint responds."""
    response = client.get("/api/puzzles")
    assert response.status_code == 200
    data = response.json()
    assert "puzzles" in data
    print("✓ Puzzles endpoint operational")

def test_formats_endpoint():
    """Test that address formats endpoint responds."""
    response = client.get("/api/formats")
    assert response.status_code == 200
    data = response.json()
    assert "formats" in data
    print("✓ Formats endpoint operational")

def test_universe42_endpoint():
    """Test that Universe 42 ranking endpoint responds."""
    response = client.get("/api/universe42")
    assert response.status_code == 200
    data = response.json()
    assert data["universe"] == 42
    assert data["mode"] == "planning"
    print("✓ Universe 42 endpoint operational")

if __name__ == "__main__":
    print("\n🔧 Running NEXUS Antikythera Recovery smoke tests...\n")
    try:
        test_app_startup()
        test_database_init()
        test_root_endpoint()
        test_status_endpoint()
        test_puzzles_endpoint()
        test_formats_endpoint()
        test_universe42_endpoint()
        print("\n✅ All smoke tests passed!\n")
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}\n")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}\n")
        sys.exit(1)
