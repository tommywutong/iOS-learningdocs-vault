#!/usr/bin/env python3
"""对 validate.py 做错误注入测试。

放宽约束（FENCE 字符类、title 判据）最容易造成的是**漏报**，
而漏报比误报危险：误报会被人忽略，漏报会让坏译文当成好的合并进去。
所以每改一次判定逻辑，都要重新确认这些错误类型仍然抓得到。
"""
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from validate import check_pair  # noqa: E402

# 挑一对当前零问题、且带 objective-c 围栏的译文当基线
EN = ROOT / "apple-docs/en/metal/encoding-argument-buffers-on-the-gpu.md"
ZH = ROOT / "apple-docs/zh/metal/encoding-argument-buffers-on-the-gpu.md"


def mutate(text: str, kind: str) -> str | None:
    """往译文里注入一类错误。返回 None 表示这类错误在该样本上造不出来。"""
    lines = text.splitlines(keepends=True)

    def find(pred, start=0):
        for i in range(start, len(lines)):
            if pred(lines[i]):
                return i
        return None

    if kind == "改 frontmatter 字段":
        i = find(lambda l: l.startswith("content_hash:"))
        if i is None:
            return None
        lines[i] = "content_hash: 'sha256:deadbeefdeadbeef'\n"
    elif kind == "改链接目标":
        i = find(lambda l: re.search(r"\]\(([^)]+)\)", l) and not l.lstrip().startswith("!"))
        if i is None:
            return None
        lines[i] = re.sub(r"\]\(([^)]+)\)", r"](\1-TAMPERED)", lines[i], count=1)
    elif kind == "删一个图片":
        i = find(lambda l: re.search(r"!\[[^\]]*\]\(", l))
        if i is None:
            return None
        lines[i] = "（图片被删）\n"
    elif kind == "改代码正文":
        inside = False
        i = None
        for n, l in enumerate(lines):
            if re.match(r"^\s*```([^\s`]*)\s*$", l):
                inside = not inside
                continue
            if inside and l.strip() and not re.match(r"^\s*(//|/\*|\*|#|--)", l):
                code, _cmt = l, ""
                if "//" not in code:
                    i = n
                    break
        if i is None:
            return None
        lines[i] = lines[i].rstrip("\n") + " /* 但这里被改了 */ tampered\n"
        # 上一行加的是行尾注释外的实际改动，确保代码部分变了
        lines[i] = "tampered_identifier" + lines[i]
    elif kind == "删一整个代码块":
        starts = [n for n, l in enumerate(lines) if re.match(r"^\s*```([^\s`]*)\s*$", l)]
        if len(starts) < 2:
            return None
        del lines[starts[0] : starts[1] + 1]
    elif kind == "改代码块语言标注":
        i = find(lambda l: re.match(r"^\s*```[^\s`]+\s*$", l))
        if i is None:
            return None
        lines[i] = "```ruby\n"
    elif kind == "删一行代码":
        inside = False
        i = None
        for n, l in enumerate(lines):
            if re.match(r"^\s*```([^\s`]*)\s*$", l):
                inside = not inside
                continue
            if inside and l.strip():
                i = n
                break
        if i is None:
            return None
        del lines[i]
    elif kind == "删一个标题":
        i = find(lambda l: re.match(r"^#{2,6}\s+", l))
        if i is None:
            return None
        del lines[i]
    elif kind == "删一个列表项":
        i = find(lambda l: re.match(r"^\s*(?:[-*+]|\d+\.)\s+", l))
        if i is None:
            return None
        del lines[i]
    elif kind == "删一个表格行":
        i = find(lambda l: re.match(r"^\s*\|.*\|\s*$", l))
        if i is None:
            return None
        del lines[i]
    elif kind == "改 callout 类型":
        i = find(lambda l: re.match(r"^>\s*\[!(\w+)\]", l))
        if i is None:
            return None
        lines[i] = re.sub(r"\[!(\w+)\]", "[!warning]", lines[i], count=1)
    elif kind == "整段英文没译":
        i = find(lambda l: len(re.findall(r"\b[A-Za-z][A-Za-z'’-]*\b", l)) >= 3
                 and re.search(r"[一-鿿]", l) and not l.startswith(("#", ">", "|", "-", "*")))
        if i is None:
            return None
        lines[i] = ("The sample application demonstrates how the argument buffer "
                    "is encoded entirely on the graphics processor without any help.\n")
    elif kind == "title 漏译":
        i = find(lambda l: l.startswith("title:"))
        if i is None:
            return None
        # 必须**逐字节照抄原文标题**：判定条件是 zh == en，
        # 自己另写一个大小写不同的字符串等于没注入这类错误（第一版就栽在这）。
        en_title = next(l for l in EN.read_text(encoding="utf-8").splitlines()
                        if l.startswith("title:"))
        lines[i] = en_title + "\n"
    elif kind == "删注释":
        inside = False
        i = None
        for n, l in enumerate(lines):
            if re.match(r"^\s*```([^\s`]*)\s*$", l):
                inside = not inside
                continue
            if inside and "//" in l and not l.lstrip().startswith("//"):
                i = n
                break
        if i is None:
            return None
        lines[i] = lines[i][: lines[i].index("//")].rstrip() + "\n"
    else:
        raise AssertionError(kind)
    return "".join(lines)


KINDS = [
    "改 frontmatter 字段", "改链接目标", "删一个图片", "改代码正文",
    "删一整个代码块", "改代码块语言标注", "删一行代码", "删一个标题",
    "删一个列表项", "删一个表格行", "改 callout 类型", "整段英文没译",
    "title 漏译", "删注释",
]


# 真实样本里没有表格、也没有行尾注释，这两类错误造不出来。
# 但「行尾注释」恰好是判定逻辑最绕的一处（要跳过字符串字面量里的 //），
# 不能留成覆盖缺口，所以用一对合成样本补上。
SYNTH_EN = """---
title: Demo
---

| A | B |
|---|---|
| 1 | 2 |
| 3 | 4 |

```objective-c
    int x = 1; // set the counter
    NSString *u = @"https://example.com";
```
"""


def synth(table_rows: str, code: str, comment: str) -> str:
    return (SYNTH_EN
            .replace("title: Demo", "title: 示例")
            .replace("| A | B |", "| 甲 | 乙 |")
            .replace("| 3 | 4 |\n", table_rows)
            .replace("    int x = 1;", code)
            .replace(" // set the counter", comment))


SYNTH_CASES = {
    "基线（合成样本，正确译文）": synth("| 3 | 4 |\n", "    int x = 1;", " // 设置计数器"),
    "删一个表格行": synth("", "    int x = 1;", " // 设置计数器"),
    "删行尾注释": synth("| 3 | 4 |\n", "    int x = 1;", ""),
    "改代码但保留注释": synth("| 3 | 4 |\n", "    int x = 2;", " // 设置计数器"),
    "吃掉缩进": synth("| 3 | 4 |\n", "int x = 1;", " // 设置计数器"),
}


# 第三处被真实译文暴露的判定漏洞：跨行块注释。`/*` 开头的多行注释，续行以
# 空格加正文开头，COMMENT 只认行首标记，认不出续行，于是把已正确翻译的注释
# 报成「代码被改动」（apple-docs/zh/foundation/increasing-app-usage-… 就是这么误报的）。
BLOCK_EN = """---
title: Demo
---

```swift
/*
 Provide just enough information in the userInfo dictionary.
 The larger the dictionary, the longer it takes.
 */
let x = 1
var y = 2 /* tail block
   continues here */
let z = 3
```
"""
BLOCK_BODY = BLOCK_EN.split("```swift\n")[1].split("```")[0]

BLOCK_CASES = {
    "基线（块注释已译、代码未动）": """/*
 在 userInfo 字典里只放刚好够恢复状态的信息。
 字典越大，投递这份载荷和恢复活动就越慢。
 */
let x = 1
var y = 2 /* 行尾块注释
   续行在这里 */
let z = 3
""",
    "块注释译了但代码也被改": """/*
 译文。
 译文。
 */
let x = 999
var y = 2 /* 行尾块注释
   续行在这里 */
let z = 3
""",
    "块注释之后的代码缩进被吃掉": """/*
 译文。
 译文。
 */
let x = 1
var y = 2 /* 注释
   续行 */
    let z = 3
""",
}


FENCED_HEADING_EN = """---
title: Demo
---

## Overview

Use this page to learn the syntax.

```markdown
## Topics
```
"""

FENCED_HEADING_CASES = {
    "基线（代码围栏内固定标题保持英文）": FENCED_HEADING_EN
        .replace("title: Demo", "title: 示例")
        .replace("## Overview", "## 概述")
        .replace("Use this page to learn the syntax.", "使用此页面了解语法。"),
    "正文固定标题漏译": FENCED_HEADING_EN
        .replace("title: Demo", "title: 示例")
        .replace("Use this page to learn the syntax.", "使用此页面了解语法。"),
}


def run_fenced_headings() -> list[str]:
    """确认代码示例中的 Markdown 标题不触发正文固定译法检查。"""
    missed = []
    with tempfile.TemporaryDirectory() as td:
        en = Path(td) / "en.md"
        en.write_text(FENCED_HEADING_EN, encoding="utf-8")
        for name, text in FENCED_HEADING_CASES.items():
            zh = Path(td) / "zh.md"
            zh.write_text(text, encoding="utf-8")
            got = check_pair(en, zh)
            expect_clean = name.startswith("基线")
            ok = (not got) if expect_clean else bool(got)
            if not ok:
                missed.append(name)
            print(f"  {'OK  ' if ok else '漏报'} {name}  →  {got[0][:66] if got else '无问题'}")
    return missed


def run_block() -> list[str]:
    missed = []
    with tempfile.TemporaryDirectory() as td:
        en = Path(td) / "en.md"
        en.write_text(BLOCK_EN, encoding="utf-8")
        for name, body in BLOCK_CASES.items():
            zh = Path(td) / "zh.md"
            zh.write_text(BLOCK_EN.replace("title: Demo", "title: 示例")
                          .replace(BLOCK_BODY, body), encoding="utf-8")
            got = check_pair(en, zh)
            expect_clean = name.startswith("基线")
            ok = (not got) if expect_clean else bool(got)
            if not ok:
                missed.append(name)
            print(f"  {'OK  ' if ok else '漏报'} {name}  →  {got[0][:66] if got else '无问题'}")
    return missed


def run_synth() -> list[str]:
    """返回漏报的用例名。"""
    missed = []
    with tempfile.TemporaryDirectory() as td:
        en = Path(td) / "en.md"
        en.write_text(SYNTH_EN, encoding="utf-8")
        for name, text in SYNTH_CASES.items():
            zh = Path(td) / "zh.md"
            zh.write_text(text, encoding="utf-8")
            got = check_pair(en, zh)
            expect_clean = name.startswith("基线")
            ok = (not got) if expect_clean else bool(got)
            if not ok:
                missed.append(name)
            flag = "OK  " if ok else "漏报"
            print(f"  {flag} {name}  →  {got[0][:70] if got else '无问题'}")
    return missed


def main() -> None:
    base_issues = check_pair(EN, ZH)
    print(f"基线（未注入）：{len(base_issues)} 个问题 {base_issues}\n")
    zh_text = ZH.read_text(encoding="utf-8")

    missed, skipped = [], []
    with tempfile.TemporaryDirectory() as td:
        for kind in KINDS:
            bad = mutate(zh_text, kind)
            if bad is None:
                skipped.append(kind)
                print(f"  --   {kind}：该样本里造不出这类错误")
                continue
            p = Path(td) / "zh.md"
            p.write_text(bad, encoding="utf-8")
            got = check_pair(EN, p)
            new = [g for g in got if g not in base_issues]
            if new:
                print(f"  OK   {kind}  →  {new[0][:76]}")
            else:
                missed.append(kind)
                print(f"  漏报 {kind}  ←←← 校验器没抓到")

    print(f"\n真实样本：注入 {len(KINDS) - len(skipped)} 类，漏报 {len(missed)} 类"
          + (f"：{missed}" if missed else "")
          + (f"；{len(skipped)} 类真实样本内造不出，转合成样本" if skipped else ""))

    print("\n合成样本（补真实样本盖不到的表格行与行尾注释）：")
    synth_missed = run_synth()

    print("\n合成样本（跨行块注释）：")
    block_missed = run_block()

    print("\n合成样本（代码围栏内的 Markdown 标题）：")
    fenced_heading_missed = run_fenced_headings()

    total = missed + synth_missed + block_missed + fenced_heading_missed
    print(f"\n合计漏报 {len(total)} 类" + (f"：{total}" if total else "——校验器判定逻辑无回退"))
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
