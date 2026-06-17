#!/usr/bin/env python3
from pathlib import Path
import html
import re
import shutil

import markdown


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

FRONT_MATTER = re.compile(r"^---\s*\n.*?\n---\s*\n", re.S)
LIQUID_RELATIVE = re.compile(r"\{\{\s*'([^']+)'\s*\|\s*relative_url\s*\}\}")
DAY_NUM = re.compile(r"Day\s+(\d+)")


def day_key(path):
    match = DAY_NUM.search(path.stem)
    return int(match.group(1)) if match else 999


def markdown_converter():
    return markdown.Markdown(
        extensions=["extra", "toc", "codehilite"],
        extension_configs={
            "codehilite": {
                "guess_lang": False,
                "use_pygments": True,
                "css_class": "codehilite",
            },
            "toc": {"permalink": False},
        },
        output_format="html5",
    )


def convert_markdown(text, page_depth):
    text = FRONT_MATTER.sub("", text, count=1)

    def liquid_link(match):
        raw = match.group(1).lstrip("/")
        return ("../" * page_depth) + raw

    text = LIQUID_RELATIVE.sub(liquid_link, text)
    converter = markdown_converter()
    return converter.convert(text)


def preview_path_for(page, current_depth):
    if page == "home":
        return "../" * current_depth or "."
    prefix = "" if current_depth else "docs/"
    return f"{prefix}{page.stem}.html"


def nav_html(active=None, current_depth=0):
    links = [
        f'<a class="preview-title" href="{preview_path_for("home", current_depth)}">28 天速通 LeetCode</a>'
    ]
    for path in sorted(DOCS.glob("Day*.md"), key=day_key):
        cls = ' class="active"' if active == path.stem else ""
        href = preview_path_for(path, current_depth)
        links.append(f'<a{cls} href="{html.escape(href)}">{html.escape(path.stem)}</a>')
    return "\n".join(links)


def head_custom():
    path = ROOT / "_includes" / "head_custom.html"
    return path.read_text(encoding="utf-8") if path.exists() else ""


BASE_CSS = """
:root {
  --preview-bg: #fffdf7;
  --preview-nav-bg: #f7f2e8;
  --preview-ink: #171513;
  --preview-muted: #635f58;
  --preview-line: rgba(23, 21, 19, 0.14);
  --preview-hover: rgba(229, 75, 55, 0.12);
}

html {
  scroll-behavior: smooth;
}

body {
  margin: 0;
  background: var(--preview-bg);
  color: var(--preview-ink);
}

.preview-layout {
  display: grid;
  grid-template-columns: 286px minmax(0, 1fr);
  min-height: 100vh;
}

.preview-nav {
  position: sticky;
  top: 0;
  box-sizing: border-box;
  height: 100vh;
  overflow: auto;
  padding: 16px 14px;
  border-right: 1px solid var(--preview-line);
  background: var(--preview-nav-bg);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans SC", sans-serif;
}

.preview-nav a {
  display: block;
  padding: 7px 9px;
  border-radius: 6px;
  color: #2a2620;
  font-size: 14px;
  line-height: 1.35;
  text-decoration: none;
}

.preview-nav a:hover,
.preview-nav a.active {
  background: var(--preview-hover);
  color: var(--preview-ink);
}

.preview-nav a.active {
  font-weight: 800;
}

.preview-nav .preview-title {
  margin: 0 0 10px;
  padding: 10px 9px 13px;
  border-bottom: 1px solid rgba(23, 21, 19, 0.16);
  border-radius: 0;
  color: var(--preview-ink);
  font-size: 16px;
  font-weight: 800;
}

.preview-main {
  box-sizing: border-box;
  min-width: 0;
  padding: 24px clamp(14px, 3vw, 34px);
}

.preview-doc {
  max-width: 980px;
  margin: 0 auto;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans SC", sans-serif;
  line-height: 1.72;
}

.preview-doc img {
  max-width: 100%;
  height: auto;
}

.preview-doc pre {
  overflow-x: auto;
}

.preview-doc a {
  color: #2f6fcb;
}

.main-content-wrap,
.main-content,
.main-content .fastpass-page {
  max-width: none;
}

@media (max-width: 860px) {
  .preview-layout {
    display: block;
  }

  .preview-nav {
    position: relative;
    height: auto;
    max-height: 230px;
  }

  .preview-main {
    padding: 14px;
  }
}
"""


def shell(title, body, active=None, current_depth=0, doc=False):
    if doc:
        open_tag = '<article class="preview-doc">'
        close_tag = "</article>"
    else:
        open_tag = '<div class="main-content-wrap"><div class="main-content">'
        close_tag = "</div></div>"

    return clean_html(f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<style>{BASE_CSS}</style>
{head_custom()}
</head>
<body>
<div class="preview-layout">
<nav class="preview-nav" aria-label="教程导航">{nav_html(active, current_depth)}</nav>
<main class="preview-main">{open_tag}{body}{close_tag}</main>
</div>
</body>
</html>""")


def clean_html(output):
    return "\n".join(line.rstrip() for line in output.splitlines()) + "\n"


def copy_assets():
    resources_src = DOCS / "resources"
    resources_dst = DOCS / "resources"
    if resources_src.exists() and resources_src != resources_dst:
        shutil.copytree(resources_src, resources_dst, dirs_exist_ok=True)


def build():
    copy_assets()
    index_body = convert_markdown((ROOT / "index.md").read_text(encoding="utf-8"), page_depth=0)
    (ROOT / "index.html").write_text(
        shell("28 天速通 LeetCode", index_body, current_depth=0),
        encoding="utf-8",
    )

    for src in sorted(DOCS.glob("Day*.md"), key=day_key):
        body = convert_markdown(src.read_text(encoding="utf-8"), page_depth=1)
        (DOCS / f"{src.stem}.html").write_text(
            shell(src.stem, body, active=src.stem, current_depth=1, doc=True),
            encoding="utf-8",
        )


if __name__ == "__main__":
    build()
