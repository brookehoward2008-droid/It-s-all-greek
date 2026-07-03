from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="NEXUS Antikythera Recovery", version="1.0.0")

AGENTS = [
    {"agent_id": "socrates", "display_name": "Socrates", "role": "Matrix Analyst", "auto_fire": False},
    {"agent_id": "aristotle", "display_name": "Aristotle", "role": "Triage Classifier", "auto_fire": True},
    {"agent_id": "heraclitus", "display_name": "Heraclitus", "role": "Trace Investigator", "auto_fire": False},
    {"agent_id": "pythagoras", "display_name": "Pythagoras", "role": "Pattern Linker", "auto_fire": True},
    {"agent_id": "diogenes", "display_name": "Diogenes", "role": "Sentinel", "auto_fire": True},
    {"agent_id": "plato", "display_name": "Plato", "role": "Curator", "auto_fire": False},
    {"agent_id": "plotinus", "display_name": "Plotinus", "role": "Creative Steward", "auto_fire": False},
    {"agent_id": "epictetus", "display_name": "Epictetus", "role": "Runtime Sentinel", "auto_fire": True},
    {"agent_id": "xenophanes", "display_name": "Xenophanes", "role": "Design Critic", "auto_fire": False},
    {"agent_id": "empedocles", "display_name": "Empedocles", "role": "Chain Router", "auto_fire": False},
]

EVENTS: list[dict[str, Any]] = []


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def universe_node(text: str, nodes: int = 42) -> int:
    total = sum(text.encode("utf-8")) + 42
    return total % nodes


HTML = """
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="NEXUS">
<title>NEXUS // Antikythera</title>
<style>
:root{--bg:#05070b;--panel:#0c1118;--line:#1e2b3a;--teal:#00e5cc;--text:#d9edf4;--muted:#6f8798;--warn:#ffb454;--purple:#9d4edd}*{box-sizing:border-box}body{margin:0;background:radial-gradient(circle at top,#11202a,#05070b 55%);color:var(--text);font-family:Consolas,Menlo,monospace}.wrap{max-width:980px;margin:0 auto;padding:14px;padding-bottom:90px}header{border:1px solid var(--line);background:rgba(12,17,24,.9);padding:14px;margin-bottom:12px}h1{margin:0;color:var(--teal);letter-spacing:2px;font-size:20px}.sub{color:var(--muted);font-size:12px;margin-top:6px}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:10px}.card{border:1px solid var(--line);background:rgba(12,17,24,.86);padding:12px}.label{font-size:10px;color:var(--muted);letter-spacing:2px;text-transform:uppercase}.value{font-size:22px;color:var(--teal);margin-top:4px}.agent{display:flex;justify-content:space-between;gap:8px;border-bottom:1px solid var(--line);padding:8px 0}.agent:last-child{border-bottom:0}.role{color:var(--muted);font-size:11px}.dot{width:8px;height:8px;border-radius:50%;background:var(--teal);box-shadow:0 0 10px var(--teal);display:inline-block;margin-right:6px}input,button{width:100%;padding:12px;background:#070b11;border:1px solid var(--line);color:var(--text);font-family:inherit}button{margin-top:8px;color:#00110f;background:var(--teal);font-weight:bold;letter-spacing:1px}pre{white-space:pre-wrap;word-break:break-word;background:#070b11;border:1px solid var(--line);padding:10px;font-size:12px}.nav{position:fixed;left:0;right:0;bottom:0;background:#05070b;border-top:1px solid var(--line);display:flex;justify-content:center;gap:6px;padding:8px}.nav a{color:var(--teal);text-decoration:none;border:1px solid var(--line);padding:8px 10px;font-size:11px}@media(max-width:560px){h1{font-size:16px}.value{font-size:18px}.wrap{padding:10px;padding-bottom:80px}}
</style>
</head>
<body>
<div class="wrap">
<header><h1><span class="dot"></span>NEXUS // ANTIKYTHERA</h1><div class="sub">Recovery shell live on port 8731. Phone-ready Codespaces build.</div></header>
<div class="grid">
<div class="card"><div class="label">Status</div><div class="value" id="status">loading</div></div>
<div class="card"><div class="label">Build</div><div class="value">Recovery v1</div></div>
<div class="card"><div class="label">Universe</div><div class="value">42</div></div>
</div>
<div class="card" style="margin-top:10px"><div class="label">Address / text lookup</div><input id="lookup" placeholder="Paste public address or note"><button onclick="doLookup()">LOOKUP</button><pre id="out">Ready.</pre></div>
<div class="card" style="margin-top:10px"><div class="label">Agents</div><div id="agents"></div></div>
</div>
<div class="nav"><a href="/health">health</a><a href="/api/status">status</a><a href="/api/v2/agents">agents</a></div>
<script>
async function j(path){const r=await fetch(path);return await r.json()}
async function boot(){const s=await j('/api/status');document.getElementById('status').textContent=s.status;const a=await j('/api/v2/agents');document.getElementById('agents').innerHTML=a.agents.map(x=>`<div class="agent"><div><b>${x.display_name}</b><div class="role">${x.role}</div></div><div>${x.auto_fire?'AUTO':'ASK'}</div></div>`).join('')}
async function doLookup(){const v=document.getElementById('lookup').value.trim();if(!v)return;const d=await j('/api/lookup/'+encodeURIComponent(v));document.getElementById('out').textContent=JSON.stringify(d,null,2)}
boot()
</script>
</body>
</html>
"""


@app.get("/", response_class=HTMLResponse)
def index() -> str:
    return HTML


@app.get("/health")
def health() -> dict[str, Any]:
    return {"ok": True, "build": "NEXUS Antikythera Recovery v1", "port": 8731}


@app.get("/api/status")
def status() -> dict[str, Any]:
    return {"status": "live", "version": "Antikythera Recovery v1", "updated_at": now_iso(), "counts": {"agents": len(AGENTS), "events": len(EVENTS)}}


@app.get("/api/v2/status")
def v2_status() -> dict[str, Any]:
    data = status()
    data["version"] = "Antikythera"
    return data


@app.get("/api/v2/agents")
def v2_agents() -> dict[str, Any]:
    return {"agents": AGENTS}


@app.get("/api/agents")
def agents() -> dict[str, Any]:
    return {"agents": AGENTS}


@app.get("/api/v2/agents/events")
def agent_events() -> dict[str, Any]:
    return {"events": EVENTS[-50:]}


@app.get("/api/lookup/{text}")
def lookup(text: str) -> dict[str, Any]:
    node = universe_node(text)
    event = {"agent_id": "empedocles", "event_type": "lookup", "subject": text[:80], "node": node, "created_at": now_iso()}
    EVENTS.append(event)
    return {"input": text, "mode": "read_only_recovery", "universe": 42, "node": node, "top_nodes": sorted([(node + i * 7) % 42 for i in range(5)])}
