#!/usr/bin/env python3
"""Build the AI Summarization Handbook static HTML site from Markdown.

Reads chapters from docs/, converts each to HTML with a shared nav + CSS,
and writes everything to site/. Also validates internal links and fails
loudly on broken references.

Usage:
    python3 build.py
"""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
STATIC = ROOT / "static"
SITE = ROOT / "site"

CSS_FILES = ["style.css", "print.css"]

# (display title, source markdown, destination html, is_home_page)
# Order here is also the navigation order.
PAGES = [
    ("Welcome", "introduction.md", "index.html", True),
    ("Free AI tools", "free-tools.md", "free-tools.html", False),
    ("Safety & paste safely", "safety.md", "safety.html", False),
    ("Articles", "articles.md", "articles.html", False),
    ("Meeting notes", "meeting-notes.md", "meeting-notes.html", False),
    ("Documents", "documents.md", "documents.html", False),
    ("Emails", "emails.md", "emails.html", False),
    ("Prompt templates", "prompt-templates.md", "prompt-templates.html", False),
    ("Local vs cloud", "local-vs-cloud.md", "local-vs-cloud.html", False),
    ("Length & tone", "length-tone.md", "length-tone.html", False),
    ("Printable cheat sheet", "cheatsheet.md", "cheatsheet.html", False),
]

# Map source markdown filename -> destination html filename.
SRC_TO_DEST = {src: dest for _title, src, dest, _home in PAGES}

NAV_TEMPLATE = """<nav class="site-nav">
  <ul>
    {links}
  </ul>
</nav>"""

NAV_LINK = '    <li><a href="{href}"{active}>{title}</a></li>'

PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — AI Summarization Handbook</title>
<link rel="stylesheet" href="static/style.css">
<link rel="stylesheet" href="static/print.css" media="print">
</head>
<body>
<header class="site-header">
  <div class="inner">
    <h1><a href="index.html">AI Summarization Handbook</a> <sub>Asdale Dynamics, LLC</sub></h1>
    {nav}
  </div>
</header>
<main class="container">
  <article class="{cheat}">
    {body}
  </article>
  <div class="copyright">
    Credit: Asdale Dynamics, LLC. &copy; 2026 Asdale Dynamics, LLC.
    MIT License. <a href="../README.md">Project README</a> &bull;
    <a href="../LICENSE">License</a>
  </div>
</main>
</body>
</html>"""

LINK_RE = re.compile(r'href="([^"]+)"')
MD_LINK_RE = re.compile(r'href="([^"]+\.md)"')


def md_to_html(text: str) -> str:
    return markdown.markdown(text, extensions=["extra", "toc", "tables"])


def rewrite_md_links(html_text: str) -> str:
    """Rewrite internal [text](file.md) links to the built .html page."""

    def repl(m):
        src = m.group(1)
        dest = SRC_TO_DEST.get(src)
        if dest is None:
            return m.group(0)
        return f'href="{dest}"'

    return MD_LINK_RE.sub(repl, html_text)


def build_nav(current: str) -> str:
    links = []
    for title, _src, dest, is_home in PAGES:
        active = ' class="active"' if dest == current else ""
        href = dest if dest != "index.html" else "index.html"
        links.append(NAV_LINK.format(href=href, title=title, active=active))
    return NAV_TEMPLATE.format(links="\n".join(links))


def build() -> list[str]:
    errors: list[str] = []
    SITE.mkdir(parents=True, exist_ok=True)
    (SITE / "static").mkdir(parents=True, exist_ok=True)

    # Copy static assets.
    for css in CSS_FILES:
        src = STATIC / css
        if src.exists():
            (SITE / "static" / css).write_bytes(src.read_bytes())
        else:
            errors.append(f"missing static asset: static/{css}")

    # Build each page.
    dest_set = {dest for _, _, dest, _ in PAGES}
    for title, src_name, dest, is_home in PAGES:
        src_path = DOCS / src_name
        if not src_path.exists():
            errors.append(f"missing source: docs/{src_name}")
            continue
        body_md = src_path.read_text(encoding="utf-8")
        body_html = md_to_html(body_md)
        body_html = rewrite_md_links(body_html)
        cheat_class = "print-cheatsheet" if dest == "cheatsheet.html" else ""
        page = PAGE_TEMPLATE.format(
            title=title,
            nav=build_nav(dest),
            body=body_html,
            cheat=cheat_class,
        )
        (SITE / dest).write_text(page, encoding="utf-8")

    # Validate internal links point to existing pages.
    for title, _src, dest, _ in PAGES:
        page_path = SITE / dest
        html_text = page_path.read_text(encoding="utf-8")
        for m in LINK_RE.finditer(html_text):
            href = m.group(1)
            if href.startswith(("http://", "https://", "mailto:", "../", "static/", "#")):
                continue
            if href.startswith("#"):
                continue
            if href not in dest_set:
                errors.append(f"broken link in {dest}: {href}")

    return errors


def main() -> None:
    errors = build()
    if errors:
        print("BUILD FAILED:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(1)
    print(f"Built {len(PAGES)} pages -> {SITE}/")


if __name__ == "__main__":
    main()
