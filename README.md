# Mimmo's Pizzeria & Restaurant

Website for **Mimmo's Pizzeria & Restaurant** in St. Albans, Vermont: home, menu, catering, about and visit pages.

**Live:** https://mimmos-italian.vercel.app

## How it fits together

- Plain HTML, CSS and JavaScript — no framework and no build step on the server.
- The root `*.html` files are **generated**. Edit the page body in `pages/<name>.html`, then run `python3 scripts/build-pages.py`; it wraps each body in the shared `<head>`, nav and footer so every page stays in sync.
- `main.js` handles the mobile menu and scroll-reveal; `styles.css` is the whole visual system.
- No environment variables and no server code.

## Local setup

```bash
python3 scripts/build-pages.py   # after editing anything in pages/
npm run dev                      # python3 -m http.server 5179
```

## Deploying

Vercel serves the files as they are (`vercel.json` sets clean URLs and long caching for `/assets`). Commit the regenerated HTML; pushes to `main` deploy to production.
