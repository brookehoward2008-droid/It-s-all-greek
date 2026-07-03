# Nexus Command Center

This branch contains the working browser-first Nexus interface for the `It-s-all-greek` repository.

## Current build

The app is intentionally shipped as a single-file `index.html` first so it works immediately in GitHub Codespaces, GitHub Pages, or a local static server.

## What works

- Dashboard
- Research source tracker
- Build task board
- Evidence / truth-state tracker
- Public live-data checks
- Local JSON export/import
- Supabase configuration guardrail
- Local persistence through browser `localStorage`

## Truth rule

Nexus must label each panel as one of the following:

- `live` — fetched from a named current source
- `local` — stored in the browser or added manually
- `static` — documented but not live
- `blocked` — not accessible or not configured
- `unknown` — needs verification

No panel should pretend static data is live.

## Run in GitHub Codespaces

Open the repo in Codespaces, then run:

```bash
python3 -m http.server 8787
```

Open the forwarded port `8787` from the Codespaces **Ports** tab.

## Run locally on Windows

From the repo folder:

```powershell
py -m http.server 8787
```

Then open:

```text
http://localhost:8787
```

## Phone access from local PC

If the server is running on the Windows PC and the iPhone is on the same Wi-Fi, open the PC IPv4 address with the port:

```text
http://YOUR-PC-IP:8787
```

Do not use `localhost` on the iPhone. On the phone, `localhost` means the phone itself.

## Backend plan

Use Supabase for:

- Auth
- RLS-protected project data
- Research source records
- Evidence records
- Realtime build status
- Edge Functions for private server logic

Never expose service-role or secret keys in this frontend.

## Repo target

`brookehoward2008-droid/It-s-all-greek`
