# Nexus Master Build

This repository contains a cleaned Nexus browser build packaged as a single launchable entry point.

## Structure
- `index.html` — root homepage
- `app/nexus-main-browser-v10.html` — main browser build
- `app/nexus-winnings-v3.html` — compatibility alias
- `docs/` — cleanup notes from the bundle cleanup
- `launch/README.md` — local launch instructions

## Launch
Serve the repository root with a simple local web server, then open:
- `http://localhost:8080`

One easy option is:
- `python -m http.server 8080`

You can also open `index.html` directly in a browser.

## Notes
This repository is an HTML/browser project. It is not an R Shiny app.
