<!-- docs/AUTO_DEPLOY.md -->
# Automatic GitHub Pages Deployment

This repository is configured to publish automatically with GitHub Actions.

## What runs automatically

- Every push to `main` runs `.github/workflows/github-pages.yml`.
- The workflow checks for `index.html` and the `app/` folder.
- The workflow uploads the repository as a static Pages artifact.
- The workflow publishes the site to GitHub Pages.

## One-time GitHub setting

In the repository, open:

`Settings → Pages → Build and deployment → Source`

Set the source to:

`GitHub Actions`

After that, future updates publish automatically when files are pushed to `main`.

## Expected public URL

The site should publish at:

`https://brookehoward2008-droid.github.io/It-s-all-greek/`

## Render note

Render is not required for this static HTML project. If Render is still connected, it can be ignored or removed to avoid Python `requirements.txt` deploy errors.
