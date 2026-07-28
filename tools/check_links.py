#!/usr/bin/env python3
"""检查仓库导航文档中的本地 Markdown 链接。

默认检查 README、CONTRIBUTING 和 _indexes 下的 Markdown：

    python3 tools/check_links.py

只验证本地目标是否存在。HTTP(S)、mailto、纯锚点与 Obsidian wikilink不在本工具范围内。
"""
from __future__ import annotations

import sys
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def markdown_destinations(text: str):
    """提取 Markdown 内联链接目标，支持目标路径中的成对括号。"""
    pos = 0
    while True:
        start = text.find("](", pos)
        if start == -1:
            return
        i = start + 2
        if i < len(text) and text[i] == "<":
            end = text.find(">", i + 1)
            if end == -1:
                pos = i + 1
                continue
            yield text[i + 1 : end]
            pos = end + 1
            continue

        depth = 1
        escaped = False
        begin = i
        while i < len(text):
            ch = text[i]
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == "(":
                depth += 1
            elif ch == ")":
                depth -= 1
                if depth == 0:
                    yield text[begin:i]
                    pos = i + 1
                    break
            i += 1
        else:
            pos = start + 2


def navigation_files() -> list[Path]:
    files = [ROOT / "README.md", ROOT / "CONTRIBUTING.md"]
    indexes = ROOT / "_indexes"
    if indexes.exists():
        files.extend(indexes.rglob("*.md"))
    return sorted({p for p in files if p.exists()})


def local_path(raw: str, source: Path) -> Path | None:
    target = raw.strip()
    if not target or target.startswith(("#", "mailto:", "data:")):
        return None
    parsed = urllib.parse.urlsplit(target)
    if parsed.scheme or parsed.netloc:
        return None
    path = urllib.parse.unquote(parsed.path)
    if not path:
        return None
    return (source.parent / path).resolve()


def main() -> int:
    files = navigation_files()
    issues: list[tuple[Path, str, Path]] = []
    checked = 0
    for source in files:
        text = source.read_text(encoding="utf-8")
        for raw in markdown_destinations(text):
            target = local_path(raw, source)
            if target is None:
                continue
            checked += 1
            if not target.exists():
                issues.append((source, raw, target))

    print(f"检查 {len(files)} 个导航文件、{checked} 个本地链接")
    if not issues:
        print("本地链接：全部有效")
        return 0

    print(f"本地链接：发现 {len(issues)} 个失效目标", file=sys.stderr)
    for source, raw, target in issues[:100]:
        print(
            f"  {source.relative_to(ROOT)}: {raw} -> {target}",
            file=sys.stderr,
        )
    if len(issues) > 100:
        print(f"  ……另有 {len(issues) - 100} 个", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
