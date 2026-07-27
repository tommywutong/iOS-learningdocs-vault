#!/usr/bin/env python3
"""找出译法不一致的结构性文字。

    python3 tools/audit_consistency.py            # 全部来源
    python3 tools/audit_consistency.py apple-docs # 只看一个来源

## 它回答的问题

「同一段英文结构文字，是不是在一部分译文里译了、在另一部分里没译？」

这类不一致靠人逐个猜是猜不完的。`## Overview` 那次是我偶然看到 WWDC 的
`## Transcript` 才发现，回头一查全仓库漏了 150 处。所以要有一个能把这类问题
一次全捞出来的东西，而不是每次等它咬人。

## 判据

对每一行英文结构文字（`##`/`###` 标题、`> Navigation:` 这类前缀），统计：
- 有多少篇译文**原样保留**了它（疑似漏译）
- 有多少篇译文**没有**这一行，但原文有（疑似已译）

两个数都不为零 = 译法不统一，需要定一个固定译法并写进
`validate.py` 的 `FIXED_LINES`，然后用 `fix_structural.py` 统一存量。

只报同时满足下面两条的，避免噪声：
- 英文原文里至少出现在 5 篇里（偶发的正文标题不算结构性文字）
- 「保留」和「已译」两边都至少有 2 篇
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate import FIXED_LINES, ROOT, split_frontmatter  # noqa: E402

SOURCES = ["apple-docs", "wwdc", "blogs"]
# 只看结构性的行：标题、以及整行就是一个已知前缀的行
STRUCTURAL = re.compile(r"^#{2,4}\s+\S.*$")
MIN_EN_FILES = 5
MIN_EACH_SIDE = 2


def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    sources = args or SOURCES

    kept: dict[str, int] = {}       # 译文里原样保留的篇数
    translated: dict[str, int] = {}  # 原文有、译文没有的篇数
    en_files: dict[str, int] = {}

    for src in sources:
        zh_root = ROOT / src / "zh"
        if not zh_root.exists():
            continue
        for zh in zh_root.rglob("*.md"):
            en = Path(str(zh).replace("/zh/", "/en/", 1))
            if not en.exists():
                continue
            _, en_body = split_frontmatter(en.read_text(encoding="utf-8"))
            _, zh_body = split_frontmatter(zh.read_text(encoding="utf-8"))
            en_lines = {ln.strip() for ln in en_body.splitlines()
                        if STRUCTURAL.match(ln.strip())}
            zh_lines = {ln.strip() for ln in zh_body.splitlines()}
            for ln in en_lines:
                en_files[ln] = en_files.get(ln, 0) + 1
                if ln in zh_lines:
                    kept[ln] = kept.get(ln, 0) + 1
                else:
                    translated[ln] = translated.get(ln, 0) + 1

    rows = []
    for ln, n_en in en_files.items():
        k, t = kept.get(ln, 0), translated.get(ln, 0)
        if n_en < MIN_EN_FILES or k < MIN_EACH_SIDE or t < MIN_EACH_SIDE:
            continue
        rows.append((k, t, n_en, ln))
    rows.sort(reverse=True)

    if not rows:
        print("没有发现译法不一致的结构性文字")
        return

    print(f"发现 {len(rows)} 段结构性文字译法不统一"
          f"（原文出现 ≥{MIN_EN_FILES} 篇，且两种处理各 ≥{MIN_EACH_SIDE} 篇）：\n")
    print(f"{'留英文':>7}{'已译':>7}{'原文篇数':>9}   文字")
    for k, t, n_en, ln in rows:
        mark = "  ← 已在 FIXED_LINES" if ln in FIXED_LINES else ""
        print(f"{k:>7}{t:>7}{n_en:>9}   {ln[:60]}{mark}")
    print("\n处理办法：给每段定一个固定译法写进 validate.py 的 FIXED_LINES，"
          "再跑 tools/fix_structural.py --apply 统一存量。")


if __name__ == "__main__":
    main()
