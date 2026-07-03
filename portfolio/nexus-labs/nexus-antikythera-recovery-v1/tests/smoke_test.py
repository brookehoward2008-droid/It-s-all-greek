from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

for path in ["/health", "/", "/api/status", "/api/v2/status", "/api/agents", "/api/v2/agents", "/api/v2/agents/events", "/api/lookup/demo"]:
    response = client.get(path)
    assert response.status_code == 200, f"{path} returned {response.status_code}"

print("ALL SMOKE TESTS PASSED")
