#!/usr/bin/env python3
"""Verify the AI Summarization Handbook build.

Checks:
  1. Every page in site/ is well-formed HTML (balanced tags via html.parser).
  2. All internal links resolve to an existing page.
  3. No obvious secrets / API keys / personal data patterns in tracked files.

Usage:
    python3 verify.py
"""
from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = ROOT / "site"

# Patterns that should never appear committed. (No real values are used.)
SECRET_PATTERNS = [
    re.compile(r"(?i)api[_-]?key\s*[:=]\s*[^\s\"']{8,}"),
    re.compile(r"(?i)secret\s*[:=]\s*[^\s\"']{8,}"),
    re.compile(r"(?i)password\s*[:=]\s*[^\s\"']{6,}"),
    re.compile(r"(?i)sk-[A-Za-z0-9]{20,}"),
    re.compile(r"\b\d{3}[- ]?\d{2}[- ]?\d{4}\b"),  # SSN-like
    re.compile(r"\b\d{13,19}\b"),  # credit-card-like
    re.compile(r"(?i)BEGIN (RSA|EC|DSA|OPENSSH) PRIVATE KEY"),
]

# Files to scan for secrets (exclude docs examples that use placeholders only).
SCAN_FILES = [
    "README.md", "LICENSE", "AGENTS.md", "STATUS.md",
    "build.py", "verify.py",
    "static/style.css", "static/print.css",
]


class TagChecker(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.stack: list[str] = []
        self.errors: list[str] = []
        self.void = {
            "area", "base", "br", "col", "embed", "hr", "img", "input",
            "link", "meta", "param", "source", "track", "wbr",
        }

    def handle_starttag(self, tag, attrs):
        if tag not in self.void:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in self.void:
            return
        if not self.stack:
            self.errors.append(f"unexpected closing tag </{tag}>")
            return
        if self.stack[-1] != tag:
            self.errors.append(f"mismatched tag: opened <{self.stack[-1]}> closed </{tag}>")
            self.stack.pop()
        else:
            self.stack.pop()


def check_html(path: Path) -> list[str]:
    parser = TagChecker()
    text = path.read_text(encoding="utf-8")
    try:
        parser.feed(text)
    except Exception as exc:  # noqa: BLE001
        return [f"HTML parse error: {exc}"]
    problems = list(parser.errors)
    for unclosed in parser.stack:
        problems.append(f"unclosed tag <{unclosed}>")
    return problems


def check_internal_links() -> list[str]:
    errors: list[str] = []
    pages = {p.name for p in SITE.glob("*.html")}
    link_re = re.compile(r'href="([^"]+)"')
    for page in SITE.glob("*.html"):
        text = page.read_text(encoding="utf-8")
        for m in link_re.finditer(text):
            href = m.group(1)
            if href.startswith(("http://", "https://", "mailto:", "../", "static/", "#")):
                continue
            if href not in pages:
                errors.append(f"broken link in {page.name}: {href}")
    return errors


def scan_secrets() -> list[str]:
    errors: list[str] = []
    for rel in SCAN_FILES:
        path = ROOT / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pat in SECRET_PATTERNS:
            for m in pat.finditer(text):
                errors.append(f"possible secret in {rel}: {m.group(0)[:60]}")
    return errors


def main() -> None:
    errors: list[str] = []

    if not SITE.exists():
        print("site/ missing — run build.py first", file=sys.stderr)
        sys.exit(1)

    for page in sorted(SITE.glob("*.html")):
        for prob in check_html(page):
            errors.append(f"{page.name}: {prob}")

    errors.extend(check_internal_links())
    errors.extend(scan_secrets())

    if errors:
        print("VERIFY FAILED:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(1)
    print("Verify OK — HTML well-formed, links resolve, no secrets detected.")


if __name__ == "__main__":
    main()
