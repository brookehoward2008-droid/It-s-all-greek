# Nexus Master Build

This repository contains a cleaned Nexus browser build packaged as a single launchable entry point.

## Structure
- `index.html` — root homepage
- `app/nexus-main-browser-v10.html` — main browser build
- `app/nexus-winnings-v3.html` — compatibility alias
- `docs/` — cleanup notes and inventory from the bundle cleanup
- `launch/start_nexus_master.bat` — Windows local server launcher
- `archive/` — placeholder for older builds and backups
- `local_python/` — placeholder for Python branch assets
- `workspace/` — placeholder working folders

## Launch
### Windows
Run:
- `launch/start_nexus_master.bat`

Then open:
- `http://localhost:8080`

### Manual
Open `index.html` directly in a browser.

## Notes
This repository is an HTML/browser project. It is not an R Shiny app.
