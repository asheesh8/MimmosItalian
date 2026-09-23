#!/usr/bin/env python3
"""Assembles site/*.html from the shared shell + per-page bodies in pages/.

Edit pages/<name>.html (just the <main> content) and re-run this script.
The <head>, nav and footer live here so every page stays in sync.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = ROOT / "pages"

NAV_LINKS = [
    ("index", "Home", "/"),
    ("menu", "Menu", "/menu.html"),
    ("catering", "Catering", "/catering.html"),
    ("about", "Our Story", "/about.html"),
    ("visit", "Visit", "/visit.html"),
    ("careers", "Careers", "/about.html#careers"),
]

ORDER_URL = "https://www.toasttab.com/mimmos-pizzeria-restaurant/v3/"
PHONE = "802-524-2244"
PHONE_TEL = "+18025242244"

PAGE_META = {
    "index": (
        "Mimmo's Pizzeria & Restaurant | St. Albans, VT",
        "Southern Italian recipes and New York-style pizza in St. Albans, Vermont since 1995. Dine in, take out, delivery and catering.",
    ),
    "menu": (
        "Menu | Mimmo's Pizzeria & Restaurant",
        "Pizza, calzones, heroes, pasta, entrees, salads and dessert. The full Mimmo's menu, St. Albans, VT.",
    ),
    "catering": (
        "Catering | Mimmo's Pizzeria & Restaurant",
        "Delivery and pickup catering from Mimmo's in St. Albans, VT: platters, pasta trays, baked specialties and dessert.",
    ),
    "about": (
        "Our Story | Mimmo's Pizzeria & Restaurant",
        "Family-run in St. Albans, Vermont since 1995. The story behind Mimmo's and our original marinara.",
    ),
    "visit": (
        "Visit Us | Mimmo's Pizzeria & Restaurant",
        "Hours, address and directions for Mimmo's Pizzeria & Restaurant, 22 South Main Street, St. Albans, VT.",
    ),
}


def build_nav(active):
    items = []
    for slug, label, href in NAV_LINKS:
        cls = ' class="active"' if slug == active else ""
        items.append(f'<li><a href="{href}"{cls}>{label}</a></li>')
    return "\n        ".join(items)


def render_shell(active, body):
    title, description = PAGE_META[active]
    nav_items = build_nav(active)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="icon" href="/assets/illustration/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/assets/fonts/eb-garamond-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/work-sans.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/styles.css">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="restaurant.restaurant">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap header-row">
    <a class="brand" href="/" aria-label="Mimmo's home">
      <img src="/assets/illustration/logo.png" alt="Mimmo's Pizzeria &amp; Restaurant" class="brand-mark">
    </a>
    <nav class="site-nav" aria-label="Primary">
      <ul>
        {nav_items}
      </ul>
    </nav>
    <div class="header-actions">
      <a class="btn btn-ghost" href="tel:{PHONE_TEL}">{PHONE}</a>
      <a class="btn btn-primary" href="{ORDER_URL}" target="_blank" rel="noopener">Order Online</a>
    </div>
    <button class="nav-toggle" aria-expanded="false" aria-controls="mobile-nav" aria-label="Menu">
      <span></span><span></span><span></span>
    </button>
  </div>
  <div class="mobile-nav" id="mobile-nav">
    <ul>
      {nav_items}
    </ul>
    <a class="btn btn-primary" href="{ORDER_URL}" target="_blank" rel="noopener">Order Online</a>
    <a class="btn btn-ghost" href="tel:{PHONE_TEL}">Call {PHONE}</a>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap footer-grid">
    <div class="footer-brand">
      <img src="/assets/illustration/logo-footer.png" alt="Mimmo's Pizzeria &amp; Restaurant" class="footer-logo">
      <p>Southern Italian recipes and New York-style pizza in St. Albans, Vermont since 1995.</p>
    </div>
    <div class="footer-col">
      <h3>Find Us</h3>
      <p>22 South Main Street<br>St. Albans, VT 05478</p>
      <p><a href="tel:{PHONE_TEL}">{PHONE}</a></p>
    </div>
    <div class="footer-col">
      <h3>Hours</h3>
      <p>Mon - Thu: 11am - 8:30pm<br>
      Friday: 11am - 9:30pm<br>
      Saturday: 11am - 9pm<br>
      Sunday: Closed</p>
    </div>
    <div class="footer-col">
      <h3>Explore</h3>
      <ul class="footer-links">
        {nav_items}
      </ul>
    </div>
  </div>
  <div class="wrap footer-bottom">
    <p>&copy; 2026 Mimmo's Pizzeria &amp; Restaurant. Family-run in St. Albans since 1995.</p>
    <p><a href="https://www.mimmositalian.com/employment-1" target="_blank" rel="noopener">Now hiring</a></p>
  </div>
</footer>
<script src="/main.js"></script>
</body>
</html>
"""


def main():
    for slug in PAGE_META:
        body_path = PAGES / f"{slug}.html"
        body = body_path.read_text()
        html = render_shell(slug, body)
        out_path = ROOT / ("index.html" if slug == "index" else f"{slug}.html")
        out_path.write_text(html)
        print(f"wrote {out_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
