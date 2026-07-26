#!/usr/bin/env python3
"""生成 README.md 和 _indexes/ 下的导航索引。

    python3 tools/indexes.py

所有数字都是**实际统计出来的**，不是写死的——内容增加后重跑一遍就刷新。
这样避免了旧仓库那种「README 写 35,753 个文件、实测 35,752 / 35,884 三个数都对不上」
的情况。
"""
from __future__ import annotations

import json
import os
import re
import statistics
import urllib.parse
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IDX = ROOT / "_indexes"


def read_fm(path: Path) -> dict:
    try:
        text = path.read_text(encoding="utf-8")[:2000]
    except Exception:
        return {}
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    fm = {}
    for line in text[4:end].splitlines():
        if ": " in line:
            k, v = line.split(": ", 1)
            fm[k.strip()] = v.strip().strip("'")
    return fm


def count_md(base: Path) -> tuple[int, int]:
    n = sz = 0
    for p in base.rglob("*.md"):
        n += 1
        sz += p.stat().st_size
    return n, sz


def link(path: Path) -> str:
    return urllib.parse.quote(str(path.relative_to(ROOT)))


# ---------------------------------------------------------------- 各来源索引


def index_apple_docs() -> dict:
    base = ROOT / "apple-docs" / "en"
    if not base.exists():
        return {}
    per_fw: dict[str, dict] = defaultdict(lambda: {"total": 0, "longform": 0, "bytes": 0})
    LONG = {"article", "overview", "collection", "sampleCode", "module"}
    for p in base.rglob("*.md"):
        fw = p.relative_to(base).parts[0]
        fm = read_fm(p)
        d = per_fw[fw]
        d["total"] += 1
        d["bytes"] += p.stat().st_size
        if fm.get("symbol_kind") in LONG or fm.get("role") in ("article", "collectionGroup", "sampleCode"):
            d["longform"] += 1

    lines = [
        "# Apple 现行文档 · 按框架",
        "",
        f"> 来源：`developer.apple.com/documentation`，抓取于 {date.today()}。",
        "> 「成篇文章」是有正文、值得翻译的部分；其余是 API 条目（一两句话的摘要 + 声明）。",
        "",
        "| 框架 | 页面总数 | 成篇文章 | 体积 |",
        "|---|---:|---:|---:|",
    ]
    for fw, d in sorted(per_fw.items(), key=lambda x: -x[1]["total"]):
        lines.append(
            f"| [{fw}](../apple-docs/en/{urllib.parse.quote(fw)}/) "
            f"| {d['total']:,} | {d['longform']:,} | {d['bytes'] / 1e6:.1f} MB |"
        )
    tot = sum(d["total"] for d in per_fw.values())
    lf = sum(d["longform"] for d in per_fw.values())
    lines.append(f"| **合计** | **{tot:,}** | **{lf:,}** | |")
    (IDX / "apple-docs.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {"total": tot, "longform": lf, "frameworks": len(per_fw)}


def index_wwdc() -> dict:
    base = ROOT / "wwdc" / "en"
    if not base.exists():
        return {}
    groups: dict[str, list] = defaultdict(list)
    years = Counter()
    for p in base.rglob("*.md"):
        fm = read_fm(p)
        groups[fm.get("group", "未分组")].append((fm, p))
        if fm.get("year") and fm["year"] != "null":
            years[fm["year"]] += 1

    lines = [
        "# WWDC session 逐字稿",
        "",
        f"> 按主题筛选的 {sum(len(v) for v in groups.values())} 场，抓取于 {date.today()}。",
        "> 逐字稿是 Apple 的自动语音识别产物，未经人工校对。",
        "",
        "**注意**：2013 年及更早的 session 已被 Apple 彻底下架，老年份也被大幅裁剪"
        "（WWDC2014 只剩 6 场）。这是归档的紧迫性所在。",
        "",
    ]
    for g in sorted(groups):
        # year 可能是 'null'（Tech Talks 这类没有年份的），不能直接 int()
        def year_of(fm: dict) -> int:
            v = fm.get("year") or ""
            return int(v) if v.isdigit() else 0

        items = sorted(groups[g], key=lambda x: (-year_of(x[0]), x[0].get("title", "")))
        ever = sum(1 for fm, _ in items if fm.get("evergreen") == "true")
        lines += [f"## {g}", "", f"{len(items)} 场，其中 {ever} 场标为「讲机制、长期有效」", ""]
        for fm, p in items:
            tag = "" if fm.get("evergreen") == "true" else " _(版本性)_"
            lines.append(
                f"- [{fm.get('title', p.stem)}]({link(p)}) "
                f"· {fm.get('collection', '')} · {fm.get('duration', '')}{tag}"
            )
        lines.append("")
    (IDX / "wwdc.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {"total": sum(len(v) for v in groups.values()), "groups": len(groups)}


def index_blogs() -> dict:
    lines = [
        "# 第三方技术博客归档",
        "",
        "> **本仓库为私有个人学习归档。** 第三方博客大多是 All rights reserved 或未声明",
        "> 授权（法律上默认保留全部权利），存作个人资料与公开发布是两回事。",
        "> 逐源授权状况见下表，也记在 `meta/blog_sources.json` 每条的 `license` 字段。",
        "",
        "已按 robots.txt 明确排除、**未抓取**的站点：`massicotte.org`、`casatwy.com`"
        "——它们在 `User-agent: *` 放开的同时单独点名禁止 ClaudeBot / anthropic-ai。",
        "",
        "| 源 | 篇数 | 中位字数 | 代码率 | 语言 | 状态 | 授权 |",
        "|---|---:|---:|---:|---|---|---|",
    ]
    cfgs = {}
    for name in ("blog_sources.json", "blog_sources_batch2.json"):
        f = ROOT / "meta" / name
        if f.exists():
            for s in json.loads(f.read_text(encoding="utf-8")).get("sources", []):
                cfgs[s["key"]] = s

    total = 0
    for lang in ("en", "zh"):
        base = ROOT / "blogs" / lang
        if not base.exists():
            continue
        for d in sorted(base.iterdir()):
            if not d.is_dir():
                continue
            files = list(d.glob("*.md"))
            if not files:
                continue
            sizes, fenced = [], 0
            for f in files:
                body = f.read_text(encoding="utf-8").split("---", 2)[-1]
                sizes.append(len(body))
                if "```" in body:
                    fenced += 1
            s = cfgs.get(d.name, {})
            total += len(files)
            lines.append(
                f"| [{s.get('name', d.name)}](../blogs/{lang}/{urllib.parse.quote(d.name)}/) "
                f"| {len(files)} | {int(statistics.median(sizes)):,} "
                f"| {fenced / len(files) * 100:.0f}% | {lang} "
                f"| {s.get('status', '')} | {s.get('license', '未记录')[:28]} |"
            )
    snap = ROOT / "blogs" / "snapshots"
    if snap.exists():
        n = len(list(snap.rglob("*.md")))
        total += n
        lines.append(f"| [学习计划点名的单页快照](../blogs/snapshots/) | {n} | | | 混合 | | 逐条不同 |")
    lines.append(f"| **合计** | **{total}** | | | | | |")
    (IDX / "blogs.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {"total": total}


# ---------------------------------------------------------------- README


def main() -> None:
    IDX.mkdir(parents=True, exist_ok=True)
    ad = index_apple_docs()
    ww = index_wwdc()
    bl = index_blogs()

    att = ROOT / "attachments"
    n_att = sum(1 for p in att.rglob("*") if p.is_file()) if att.exists() else 0
    sz_att = sum(p.stat().st_size for p in att.rglob("*") if p.is_file()) if att.exists() else 0
    oss = ROOT / "oss"
    n_oss = sum(1 for p in oss.iterdir() if p.is_dir()) if oss.exists() else 0

    zh_counts = {
        k: len(list((ROOT / k / "zh").rglob("*.md"))) if (ROOT / k / "zh").exists() else 0
        for k in ("apple-docs", "wwdc", "blogs")
    }

    readme = f"""# Apple 文档与 iOS 底层知识归档

> 私有个人学习归档。生成于 {date.today()}，统计数字由 `tools/indexes.py` 实际扫描得出。

## 这是什么

把 iOS 底层学习需要的一手材料抓成本地 Markdown，放进 Obsidian 阅读，并翻译成中文。
四个来源：

| 来源 | 内容 | 数量 | 已译 |
|---|---|---:|---:|
| **Apple 现行文档** | `developer.apple.com/documentation`，{ad.get('frameworks', 0)} 个框架 | {ad.get('total', 0):,} 页（成篇文章 {ad.get('longform', 0):,}） | {zh_counts['apple-docs']:,} |
| **WWDC 逐字稿** | 按主题筛选，{ww.get('groups', 0)} 个分组 | {ww.get('total', 0)} 场 | {zh_counts['wwdc']:,} |
| **第三方技术博客** | 经甄别的一手来源 | {bl.get('total', 0):,} 篇 | {zh_counts['blogs']:,} |
| **Apple 开源** | objc4 / dyld / CF / libdispatch 等 | {n_oss} 个仓库 | — |

图片附件 {n_att:,} 个 / {sz_att / 1e9:.2f} GB（超过 1 MB 的已按最长边压缩，见 `meta/shrink_report.json`）。

## 怎么用

| 我想… | 去哪 |
|---|---|
| **按学习计划找材料** | [`_indexes/study-plan.md`](_indexes/study-plan.md) —— 把 2026 暑假学习计划的每个外链映射到本地文件，按周次和 Day 组织 |
| 按框架浏览 Apple 文档 | [`_indexes/apple-docs.md`](_indexes/apple-docs.md) |
| 找 WWDC session | [`_indexes/wwdc.md`](_indexes/wwdc.md) |
| 看博客归档与授权 | [`_indexes/blogs.md`](_indexes/blogs.md) |

## 目录结构

```
apple-docs/{{en,zh}}/<框架>/**.md    Apple 现行文档
wwdc/{{en,zh}}/<年份>/*.md           WWDC 逐字稿
blogs/{{en,zh}}/<源>/*.md            第三方博客
blogs/snapshots/<域名>/*.md        学习计划点名的单页快照
oss/<仓库>/                        Apple 开源与 Swift 一手资料
attachments/                       图片，各来源共用
_indexes/                          导航索引
meta/                              规范、术语表、清单、侦察报告
tools/                             抓取与渲染工具链
```

**英文原文在 `en/`，中文译文在 `zh/`，路径一一对应。** 不做原地替换——现行文档是
Apple 在维护的活内容，留着英文基线才能靠 frontmatter 里的 `content_hash` 做增量
diff、只重译变化的部分。中文来源的博客只有 `zh/`。

## 翻译

- 规范：[`meta/TRANSLATION_STYLE.md`](meta/TRANSLATION_STYLE.md)
- 术语表：[`meta/TERMS.md`](meta/TERMS.md) —— 按 **Apple 官方简体中文优先**裁决，
  187 条有官方依据。与旧仓库 `apple-developer-archive-vault` 的术语选择**有意分歧**，
  不要互相「纠正」。
- 三道关：译者 → 独立审校 → `tools/validate.py` 机械校验（13 类错误注入测试，零漏检零误报）

## 版权

Apple 文档与 WWDC 逐字稿为 Apple 版权所有。第三方博客逐源授权见
[`_indexes/blogs.md`](_indexes/blogs.md)，其中仅 `onevcat`（CC BY 4.0）与
`saagarjha`（CC BY-SA 4.0）明确允许再分发。Apple 开源代码为 APSL 2.0 / Apache-2.0，
源码目录保持逐字节原样，笔记一律写在 `oss/notes/`。

**本仓库为私有个人学习归档，不得转为公开。**
"""
    (ROOT / "README.md").write_text(readme, encoding="utf-8")
    print(f"README.md + _indexes/ 已生成")
    print(f"  Apple 文档 {ad.get('total', 0):,} 页（成篇 {ad.get('longform', 0):,}）")
    print(f"  WWDC {ww.get('total', 0)} 场 · 博客 {bl.get('total', 0):,} 篇 · OSS {n_oss} 仓库")
    print(f"  图片 {n_att:,} 个 / {sz_att / 1e9:.2f} GB")


if __name__ == "__main__":
    main()
