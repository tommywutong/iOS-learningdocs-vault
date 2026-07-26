#!/usr/bin/env python3
"""把用户的《2026 暑假 iOS 底层学习计划》里的每个外链，映射到本地归档文件。

    python3 tools/studyplan.py            # 生成 _indexes/study-plan.md
    python3 tools/studyplan.py --report   # 只打印覆盖率统计，不写文件

## 为什么这是最有用的一个索引

归档了 5,000 多篇材料，但用户真正会按顺序读的是他计划里点名的那 338 个外链。
这个索引把「计划里的第几周第几天要读什么」和「本地哪个文件」对上，于是：

- 学到哪一天，直接点开本地文件，不用开浏览器、不用翻墙、不用担心原站下线
- 能立刻看出哪些材料**还没归档**（覆盖率报告），补抓有依据
- 译文就绪后，同一行会同时给出英文原文和中文译文两个链接

## 映射规则

| 计划里的链接 | 本地位置 |
|---|---|
| `developer.apple.com/documentation/<path>` | `apple-docs/{en,zh}/<path>.md` |
| `developer.apple.com/videos/play/<coll>/<id>/` | `wwdc/{en,zh}/<coll>/<id>-*.md` |
| `developer.apple.com/library/archive/…` | 旧仓库 `apple-developer-archive-vault`（跨仓库，只给提示） |
| 第三方博客 | `blogs/{en,zh}/<source>/*.md`，按 frontmatter 的 source_url 反查 |
| GitHub 仓库 | `oss/<repo>/`（尚未 clone 的标注为待办） |
"""
from __future__ import annotations

import json
import os
import re
import sys
import urllib.parse
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# 学习计划的位置。默认指向作者的 Obsidian vault，可用环境变量覆盖，
# 避免把个人路径写死在仓库里。
PLAN = Path(os.environ.get(
    "STUDY_PLAN",
    str(Path.home() / "Obsidian/iOS/10 学习计划/2026 暑假 iOS 底层学习计划.md"),
))
OUT = ROOT / "_indexes" / "study-plan.md"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import safe_rel


def norm_url(url: str) -> str:
    """URL 规范化，用于跨来源比对。

    同一篇文章在计划里和在 frontmatter 里的写法经常不一致：http vs https、
    带不带 www、尾斜杠、`index.html`、锚点、查询串。不规范化的话，明明抓了
    305 篇的 mikeash 也会有链接匹配不上。
    """
    p = urllib.parse.urlparse(url.split("#")[0])
    host = p.netloc.lower().removeprefix("www.")
    path = p.path.rstrip("/")
    path = re.sub(r"/(index|_index)\.html?$", "", path)
    return f"{host}{path}".lower()


def build_blog_index() -> dict[str, Path]:
    """source_url → 本地 md 路径。译文优先，其次英文原文。"""
    idx: dict[str, Path] = {}
    for lang in ("zh", "en"):
        base = ROOT / "blogs" / lang
        if not base.exists():
            continue
        for f in base.rglob("*.md"):
            text = f.read_text(encoding="utf-8")[:1200]
            m = re.search(r"^source_url: '?([^'\n]+)'?$", text, re.M)
            if m:
                idx.setdefault(norm_url(m.group(1)), f)
    return idx


def build_wwdc_index() -> dict[tuple[str, str], Path]:
    idx: dict[tuple[str, str], Path] = {}
    base = ROOT / "wwdc" / "en"
    if base.exists():
        for f in base.rglob("*.md"):
            m = re.match(r"(\d+)-", f.name)
            if m:
                idx[(f.parent.name, m.group(1))] = f
    return idx


def parse_plan() -> list[dict]:
    """按「## 第 N 周」/「#### Day N」切段，提取每段里的链接。"""
    if not PLAN.exists():
        sys.exit(f"找不到学习计划：{PLAN}")
    text = PLAN.read_text(encoding="utf-8")
    entries: list[dict] = []
    week = day = ""
    for line in text.splitlines():
        wm = re.match(r"^##\s+(第.+?周.*|第.+?阶段.*)$", line)
        if wm:
            week, day = wm.group(1).strip(), ""
            continue
        dm = re.match(r"^####\s+(Day\s*\d+.*)$", line)
        if dm:
            day = dm.group(1).strip()
            continue
        for url in re.findall(r"https?://[^\s)\]]+", line):
            entries.append({"week": week, "day": day, "url": url.rstrip(".,;")})
    return entries


def classify(url: str, blogs: dict, wwdc: dict) -> tuple[str, Path | None, str]:
    """返回 (类别, 本地文件或 None, 说明)。"""
    p = urllib.parse.urlparse(url)
    host, path = p.netloc.replace("www.", ""), p.path

    if host == "developer.apple.com":
        if path.startswith("/documentation/"):
            rel = safe_rel(path.rstrip("/"))
            f = ROOT / "apple-docs" / "en" / (rel + ".md")
            return ("Apple 现行文档", f if f.exists() else None, "" if f.exists() else "未归档")
        m = re.match(r"/videos/play/([^/]+)/(\d+)", path)
        if m:
            f = wwdc.get((m.group(1), m.group(2)))
            return ("WWDC", f, "" if f else "不在 178 场短名单里")
        if path.startswith("/library/archive/"):
            return ("Apple 旧归档", None, "在旧仓库 apple-developer-archive-vault")
        return ("Apple 其它", None, "")

    if "github.com" in host:
        return ("GitHub 源码", None, "待 clone 到 oss/")

    f = blogs.get(norm_url(url))
    if f:
        return ("第三方博客", f, "")
    return ("第三方博客", None, f"未归档（{host}）")


def main() -> None:
    blogs, wwdc = build_blog_index(), build_wwdc_index()
    entries = parse_plan()

    stats: dict[str, list[int]] = defaultdict(lambda: [0, 0])
    for e in entries:
        cat, f, note = classify(e["url"], blogs, wwdc)
        e["cat"], e["file"], e["note"] = cat, f, note
        stats[cat][0] += 1
        if f:
            stats[cat][1] += 1

    print(f"学习计划里共 {len(entries)} 个外链\n")
    print(f"{'类别':16}{'链接数':>7}{'已归档':>8}{'覆盖率':>8}")
    for cat, (tot, got) in sorted(stats.items(), key=lambda x: -x[1][0]):
        print(f"{cat:16}{tot:>7}{got:>8}{got / tot * 100:>7.0f}%")

    if "--report" in sys.argv:
        return

    lines = [
        "# 学习计划 · 材料索引",
        "",
        "> 由 `tools/studyplan.py` 从 `2026 暑假 iOS 底层学习计划.md` 自动生成。",
        "> 每一行是计划里点名的一份材料；有本地归档的给出链接，没有的标「未归档」。",
        "",
        "## 覆盖率",
        "",
        "| 类别 | 链接数 | 已归档 | 覆盖率 |",
        "|---|---:|---:|---:|",
    ]
    for cat, (tot, got) in sorted(stats.items(), key=lambda x: -x[1][0]):
        lines.append(f"| {cat} | {tot} | {got} | {got / tot * 100:.0f}% |")
    lines.append("")

    cur_week = cur_day = None
    seen: set[tuple] = set()
    for e in entries:
        if e["week"] != cur_week:
            cur_week, cur_day = e["week"], None
            lines += ["", f"## {cur_week or '（计划开头）'}", ""]
        if e["day"] != cur_day:
            cur_day = e["day"]
            if cur_day:
                lines += [f"### {cur_day}", ""]
        key = (cur_week, cur_day, e["url"])
        if key in seen:
            continue
        seen.add(key)

        if e["file"]:
            rel = e["file"].relative_to(ROOT)
            zh = Path(str(rel).replace("/en/", "/zh/", 1))
            local = f"[本地]({urllib.parse.quote(str(rel))})"
            if (ROOT / zh).exists():
                local += f" · [中文]({urllib.parse.quote(str(zh))})"
            lines.append(f"- {local} · [原文]({e['url']}) — {e['cat']}")
        else:
            note = f"（{e['note']}）" if e["note"] else ""
            lines.append(f"- [原文]({e['url']}) — {e['cat']}{note}")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\n索引 → {OUT.relative_to(ROOT)}（{len(lines)} 行）")


if __name__ == "__main__":
    main()
