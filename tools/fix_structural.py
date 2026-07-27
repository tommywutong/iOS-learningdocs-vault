#!/usr/bin/env python3
"""把译文里漏译的结构性文字统一成 TRANSLATION_STYLE.md 第三节的固定译法。

    python3 tools/fix_structural.py            # 试运行，只报告
    python3 tools/fix_structural.py --apply    # 落盘

## 为什么需要它

`## Topics` / `## See Also` / `## Transcript` 这类渲染器生成的结构标题只有一种
正确译法，但它们躲得过「残留英文」检查——只有一两个单词，够不到 8 词阈值。
结果是同一个标题在仓库里出现两种写法：`## 概述` 465 处、`## Overview` 15 处。

译法表由 `validate.py` 单独持有（`FIXED_LINES` / `FIXED_INLINE`），这里直接引用，
避免两处各写一份、日后改一处忘另一处。

## 安全边界

- 只改 `zh/` 下的文件
- 只在**英文原文确实有这段结构**时才替换（正文里偶然出现同名标题不动）
- 整行匹配用整行替换；`> Navigation:` 这类前缀只替换前缀，后面的链接原样保留
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate import (  # noqa: E402
    FIXED_INLINE, FIXED_LINES, HEADING, ROOT, split_frontmatter,
)

SOURCES = ["apple-docs", "wwdc", "blogs"]


def fix_file(en: Path, zh: Path) -> tuple[str, int]:
    """返回 (新内容, 改动处数)。"""
    en_text = en.read_text(encoding="utf-8")
    zh_text = zh.read_text(encoding="utf-8")
    _, en_body = split_frontmatter(en_text)
    en_lines = {ln.strip() for ln in en_body.splitlines()}
    n = 0

    lines = zh_text.splitlines(keepends=True)

    # 标题按序列逐位对齐后强制成固定译法。这样既能修「原样留英文」，也能修
    # 「各译一个变体」（`### Essentials` 曾有基础 / 基础知识 / 要点 / 基础要点四种）。
    # 只在标题数量相等时做——不相等说明结构本身有问题，该由 validate.py 报出来，
    # 这里硬改只会把错位固化下去。
    en_heads = [ln.strip() for ln in en_body.splitlines() if HEADING.match(ln.strip())]
    zh_idx = [i for i, ln in enumerate(lines) if HEADING.match(ln.strip())]
    if len(en_heads) == len(zh_idx):
        for e, i in zip(en_heads, zh_idx):
            want = FIXED_LINES.get(e)
            if want and lines[i].strip() != want:
                lines[i] = want + ("\n" if lines[i].endswith("\n") else "")
                n += 1
    else:
        # 标题对不齐时退回保守做法：只把原样残留的英文换掉
        for i, line in enumerate(lines):
            s = line.strip()
            if s in FIXED_LINES and s in en_lines:
                lines[i] = FIXED_LINES[s] + ("\n" if line.endswith("\n") else "")
                n += 1
    out = "".join(lines)

    for en_form, zh_form in FIXED_INLINE.items():
        if en_form in en_body and en_form in out:
            n += out.count(en_form)
            out = out.replace(en_form, zh_form)
    # `> Navigation: [x]` → `> 导航：[x]`：前缀替换后会多留一个空格
    out = out.replace("> 导航： ", "> 导航：")
    return out, n


def main() -> None:
    apply = "--apply" in sys.argv
    total_files = total_hits = 0
    per_source: dict[str, int] = {}

    for src in SOURCES:
        zh_root = ROOT / src / "zh"
        if not zh_root.exists():
            continue
        for zh in sorted(zh_root.rglob("*.md")):
            en = Path(str(zh).replace("/zh/", "/en/", 1))
            if not en.exists():
                continue
            new, n = fix_file(en, zh)
            if n == 0:
                continue
            total_files += 1
            total_hits += n
            per_source[src] = per_source.get(src, 0) + 1
            if apply:
                zh.write_text(new, encoding="utf-8")

    verb = "已统一" if apply else "可统一"
    print(f"{verb} {total_hits} 处结构性文字，涉及 {total_files} 篇")
    for src, n in sorted(per_source.items()):
        print(f"    {src}: {n} 篇")
    if not apply:
        print("\n（试运行，加 --apply 落盘）")


if __name__ == "__main__":
    main()
