#!/usr/bin/env python3
"""把博客译文里「上下篇导航」链接的显示文字换成对应文章的中文标题。

    python3 tools/fix_navlinks.py            # 试运行，只报告
    python3 tools/fix_navlinks.py --apply    # 落盘

## 为什么要单独做一个工具

导航链接（`« [上一篇标题](url)` / `[下一篇标题](url) »`）的显示文字是**另一篇文章
的标题**。翻译某一篇的 agent 手上没有别篇的译名，随手意译就会出现同一篇文章在
不同页面上叫三个名字。

所以这件事不该由翻译 agent 各自决定，而应该从「已落地的译文标题」这一个事实来源
统一推导。每轮翻译结束后重跑一次，新译好的文章的标题会自动传播到所有引用它的
导航链接上。

## 匹配规则

用 frontmatter 的 `source_url` 建 URL → 中文标题的映射，比对时去掉查询串
（同一篇文章会带 `?tag=swift`、`?tag=mac-os-classic` 等不同后缀）和末尾斜杠。

查不到的**保持原样不动**并计入报告——那说明目标文章还没译，属于真实的未完成，
不该用一个临时意译把它盖过去。
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ZH = ROOT / "blogs" / "zh"
EN = ROOT / "blogs" / "en"

# 只认整行就是一个链接、且带 « 或 » 的行。正文里的行内链接不能碰。
NAV = re.compile(r"^(?P<pre>«\s*)?\[(?P<text>[^\]]+)\]\((?P<url>[^)]+)\)(?P<post>\s*»)?$")
HAS_CJK = re.compile(r"[一-鿿]")


def norm(url: str) -> str:
    return url.split("?")[0].split("#")[0].rstrip("/")


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    out = {}
    for line in text[4:end].splitlines():
        if ": " in line:
            k, v = line.split(": ", 1)
            out[k.strip()] = v.strip().strip("'\"")
    return out


def title_map() -> dict[str, str]:
    """URL → 中文标题。只收已译出且标题确实是中文的。"""
    out: dict[str, str] = {}
    for p in ZH.rglob("*.md"):
        fm = frontmatter(p)
        url, title = fm.get("source_url"), fm.get("title")
        if url and title and HAS_CJK.search(title):
            out[norm(url)] = title
    return out


def en_exists() -> set[str]:
    """有英文原文但还没译的 URL —— 用来区分「等它被译」和「原站文章没归档」。"""
    out = set()
    for p in EN.rglob("*.md"):
        url = frontmatter(p).get("source_url")
        if url:
            out.add(norm(url))
    return out


def main() -> None:
    apply = "--apply" in sys.argv
    titles, ens = title_map(), en_exists()
    changed_files = 0
    fixed = pending_en = missing = 0
    pending_samples: list[str] = []

    for p in sorted(ZH.rglob("*.md")):
        lines = p.read_text(encoding="utf-8").splitlines(keepends=True)
        hit = False
        for i, line in enumerate(lines):
            m = NAV.match(line.strip())
            if not m or not (m["pre"] or m["post"]):
                continue
            if HAS_CJK.search(m["text"]):
                continue
            key = norm(m["url"])
            zh = titles.get(key)
            if zh is None:
                if key in ens:
                    pending_en += 1
                    if len(pending_samples) < 5:
                        pending_samples.append(f'{m["text"]}  ({p.name})')
                else:
                    missing += 1
                continue
            lines[i] = (f'{m["pre"] or ""}[{zh}]({m["url"]}){m["post"] or ""}'
                        + ("\n" if line.endswith("\n") else ""))
            fixed += 1
            hit = True
        if hit:
            changed_files += 1
            if apply:
                p.write_text("".join(lines), encoding="utf-8")

    verb = "已替换" if apply else "可替换"
    print(f"{verb} {fixed} 条导航链接文字，涉及 {changed_files} 篇")
    print(f"暂时查不到中文标题：{pending_en} 条（目标文章有英文原文、还没译，下一轮会自动跟上）")
    print(f"                    {missing} 条（目标文章连英文原文都没归档）")
    for s in pending_samples:
        print(f"    · {s}")
    if not apply:
        print("\n（试运行，加 --apply 落盘）")


if __name__ == "__main__":
    main()
