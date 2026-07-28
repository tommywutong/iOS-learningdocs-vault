#!/usr/bin/env python3
"""校验中文译文对英文原文的结构保真度。

    python3 tools/validate.py apple-docs           # 校验该来源下全部已译文件
    python3 tools/validate.py apple-docs/zh/uikit  # 只校验一个子树
    python3 tools/validate.py --json               # 输出机器可读结果

这是翻译流水线的第三道关，也是唯一确定性的一道：前两道（译者 agent、审校 agent）
都是模型判断，可能出错也可能自我说服；这一道是逐字符比对，过不了就是真有问题。

检查项（每一项都是「译文必须与原文一致」的硬约束）：
  1. frontmatter 除 title / translated 外零改动
  2. 链接目标集合完全一致（路径 + 锚点）——译者只能改显示文字
  3. 图片链接集合完全一致
  4. 代码块：数量、语言标注、行数一致；**非注释行逐字符一致**（注释允许译）
  5. 标题结构：层级序列一致
  6. 列表项数量、表格行列数一致
  7. Obsidian callout 标记（> [!note] 之类）数量与类型一致
  8. 译文里不应残留成句英文（排除代码、行内代码、链接、术语）
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# 围栏允许前导空白：列表项内的代码块是缩进的（`  ```objc`），
# 行首锚定的正则识别不了，会把整块代码当正文去做「残留英文」扫描而误报。
#
# 语言标注**不能**用 `\w*`：`\w` 不含连字符，于是 ```objective-c（仓库里 503 处）、
# ```c++、```obj-c 都识别不出开围栏。后果是连锁的——闭围栏 ``` 反被当成开围栏，
# 紧随其后的正文被当成代码做逐字符比对（正文当然译过 → 假报「代码被改动」），
# 同时真代码被当成正文去扫残留英文（→ 假报 NSAssert 之类未翻译）。
# 一个字符类吃掉了两类假问题，所以这里放宽到「除空白和反引号以外的任何字符」。
FENCE = re.compile(r"^\s*```([^\s`]*)\s*$")
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(<?([^)>]+)>?\)")
IMAGE = re.compile(r"!\[[^\]]*\]\(<?([^)>]+)>?\)")
HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
CALLOUT = re.compile(r"^>\s*\[!(\w+)\]")
LIST_ITEM = re.compile(r"^\s*(?:[-*+]|\d+\.)\s+")
TABLE_ROW = re.compile(r"^\s*\|.*\|\s*$")
COMMENT = re.compile(r"^\s*(//|/\*|\*|#|--)")
INLINE_CODE = re.compile(r"`[^`]*`")
PLATFORM_WORDS = {
    "iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS",
    "Mac", "Catalyst",
}

# 允许译文改动的 frontmatter 字段
MUTABLE_FIELDS = {"title", "translated", "translated_at", "translator", "reviewed"}

# 渲染器生成的结构性文字，必须用 TRANSLATION_STYLE.md 第三节的固定译法。
# 这一项是「同一语料里译法不统一」的唯一确定性防线：`## Topics` 只有 1 种正确
# 写法，而它躲得过「残留英文」检查（只有 1 个单词，够不到 8 词阈值）。
# 实测漏出去过 108 处：39 篇 `## Topics`、33 篇 `## See Also`、15 篇 `## Overview`
# 与 WWDC 的 21 篇 `## Transcript`、21 篇 `## Resources`、7 篇 `## Chapters`。
FIXED_LINES = {
    "## Topics": "## 主题",
    "## See Also": "## 另请参阅",
    "## Relationships": "## 关系",
    "## Parameters": "## 参数",
    "## Default Implementations": "## 默认实现",
    "## Download": "## 下载",
    "## Overview": "## 概述",
    # WWDC 这三个：前两个跟随仓库已有先例
    # （wwdc2021/10132、10133 用的是 `## 相关资源` 而不是 `## 资源`），
    # `## Chapters` 无先例，定为 `## 章节`
    "## Transcript": "## 逐字稿",
    "## Resources": "## 相关资源",
    "## Chapters": "## 章节",
    # DocC 生成的三级分组名。译法取自 tools/audit_consistency.py 的实测多数：
    # `### Essentials` 曾出现「基础 17 / 基础知识 9 / 要点 6 / 基础要点 1」四种写法。
    # 与本文件 FIXED_INLINE 里 <sub> 角色标签的译法保持一致。
    "### Essentials": "### 基础",
    "### Reference": "### 参考",
    "### Related Documentation": "### 相关文档",
    "### Constants": "### 常量",
    "### Variables": "### 变量",
    "### Functions": "### 函数",
    "### Macros": "### 宏",
    "### Classes": "### 类",
    "### Structures": "### 结构体",
    "### Protocols": "### 协议",
    "### Enumerations": "### 枚举",
    "### Enumeration Cases": "### 枚举 case",
    "### Type Aliases": "### 类型别名",
    "### Initializers": "### 初始化方法",
    "### Instance Methods": "### 实例方法",
    "### Instance Properties": "### 实例属性",
    "### Type Methods": "### 类型方法",
    "### Type Properties": "### 类型属性",
    "### Operators": "### 运算符",
    "### Deprecated": "### 已废弃",
    "### Error codes": "### 错误码",
    "### Supporting types": "### 支持类型",
    # Xcode 工具名称。项目现有正文和 Xcode 界面均以英文产品名使用，
    # 不把 Sanitizer 机械译成「消毒器」或「清理器」。
    "### Thread Sanitizer": "### Thread Sanitizer",
    "### Undefined Behavior Sanitizer": "### Undefined Behavior Sanitizer",
}
FIXED_INLINE = {
    "> Navigation:": "> 导航：",
    "<sub>Article</sub>": "<sub>文章</sub>",
    "<sub>Framework</sub>": "<sub>框架</sub>",
    "<sub>Sample Code</sub>": "<sub>示例代码</sub>",
    "<sub>API Collection</sub>": "<sub>API 集合</sub>",
    "<sub>Instance Method</sub>": "<sub>实例方法</sub>",
    "<sub>Instance Property</sub>": "<sub>实例属性</sub>",
    "<sub>Type Method</sub>": "<sub>类型方法</sub>",
    "<sub>Initializer</sub>": "<sub>初始化方法</sub>",
    "<sub>Enumeration Case</sub>": "<sub>枚举 case</sub>",
}


def split_frontmatter(text: str) -> tuple[dict, str]:
    """返回 (frontmatter 字典, 正文)。没有 frontmatter 就返回空字典。"""
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    fm: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ": " in line:
            k, v = line.split(": ", 1)
            fm[k.strip()] = v.strip()
        elif line.endswith(":"):
            fm[line[:-1].strip()] = ""
    return fm, text[end + 5 :]


def code_blocks(body: str) -> list[tuple[str, list[str]]]:
    """提取代码块 → [(语言, 行列表)]。"""
    out, lang, buf, inside = [], "", [], False
    for line in body.splitlines():
        m = FENCE.match(line)
        if m and not inside:
            inside, lang, buf = True, m.group(1), []
        elif line.strip().startswith("```") and inside:
            out.append((lang, buf))
            inside = False
        elif inside:
            buf.append(line)
    if inside:  # 未闭合，也记下来，让检查项报出来
        out.append((lang + "  [未闭合]", buf))
    return out


def strip_code(body: str) -> str:
    """去掉代码块，用于「残留英文」检测。"""
    out, inside = [], False
    for line in body.splitlines():
        if FENCE.match(line):
            inside = not inside
            continue
        if not inside:
            out.append(line)
    return "\n".join(out)


def split_trailing_comment(line: str) -> tuple[str, str]:
    """把一行代码切成 (代码部分, 行尾注释)。

    规范允许译注释，但 COMMENT 只认整行注释，`print("A") // prints "A"`
    这种行尾注释会被当成代码去逐字符比对，报出假问题。

    只处理 `//` 和 `/*`：本仓库的代码块几乎全是 Swift/ObjC/C。不处理 `#`，
    因为 Swift 的 `#if` / `#selector` / `#"raw"#` 和 ObjC 的 `#import` 会误伤，
    Python 那点行尾注释不值得为此冒险。
    需要跳过字符串字面量里的 `//`——`URL(string: "https://…")` 满地都是。
    """
    quote: str | None = None
    i = 0
    while i < len(line):
        c = line[i]
        if quote:
            if c == "\\":
                i += 2
                continue
            if c == quote:
                quote = None
        elif c in "\"'":
            quote = c
        elif c == "/" and line[i + 1 : i + 2] in ("/", "*"):
            return line[:i], line[i:]
        i += 1
    return line, ""


def prose_lines(body: str) -> list[str]:
    """返回代码围栏外的正文行。

    DocC 教程会在 `markdown` 代码围栏中演示 `## Topics`、`## Overview`
    等标题。这些行是示例代码，不是当前页面的结构性标题，不能参与标题结构
    或固定译法检查。
    """
    out: list[str] = []
    inside = False
    for line in body.splitlines():
        if FENCE.match(line):
            inside = not inside
            continue
        if not inside:
            out.append(line)
    return out


def headings(body: str) -> list[int]:
    return [len(m.group(1)) for line in prose_lines(body) if (m := HEADING.match(line))]


def count(body: str, pattern: re.Pattern) -> int:
    return sum(1 for line in body.splitlines() if pattern.match(line))


def callouts(body: str) -> list[str]:
    return [m.group(1).lower() for line in body.splitlines() if (m := CALLOUT.match(line))]


def residual_english(body: str) -> list[str]:
    """找出疑似未翻译的成句英文。

    判定：一行里去掉行内代码、链接目标、URL 之后，仍有连续 8 个及以上的
    纯 ASCII 单词，且该行不含中文字符。阈值取 8 是为了放过术语短语和 API 名。
    """
    hits = []
    for line in strip_code(body).splitlines():
        s = line.strip()
        if not s or s.startswith(">") and "[!" in s:
            continue
        if re.fullmatch(r"(?:[-*+]\s+)?(?:\[[^\]]+\]\([^)]+\)\s*)+", s):
            continue
        if re.fullmatch(r"Copyright © \d{4}(?:-\d{4})?.*All Rights Reserved", s):
            continue
        if s.startswith(">") and re.search(
            r"(?:dyld:|@selector\(|\[\[?[A-Za-z_]|/var/|"
            r"@(?:executable|loader|rpath)_path)",
            s,
        ):
            continue
        if re.search(r"[一-鿿]", s):
            continue
        s = INLINE_CODE.sub(" ", s)
        s = re.sub(r"\]\([^)]*\)", "] ", s)
        s = re.sub(r"https?://\S+", " ", s)
        s = re.sub(r"^#{1,6}\s+|^\s*(?:[-*+]|\d+\.)\s+|^>\s*", "", s)
        s = re.sub(r"<[^>]+>", " ", s)
        words = re.findall(r"\b[A-Za-z][A-Za-z'’-]*\b", s)
        # DocC 的 <sub> 平台可用性列表可能刚好达到 8 个词，但这些全是
        # 不可翻译的平台名，不是残留英文句子。只豁免纯平台词集合。
        if words and all(word in PLATFORM_WORDS for word in words):
            continue
        if len(words) >= 8:
            hits.append(line.strip()[:110])
    return hits


def check_pair(en: Path, zh: Path) -> list[str]:
    issues: list[str] = []
    en_fm, en_body = split_frontmatter(en.read_text(encoding="utf-8"))
    zh_fm, zh_body = split_frontmatter(zh.read_text(encoding="utf-8"))

    # 1. frontmatter
    if not zh_fm:
        issues.append("译文缺 frontmatter")
    for k, v in en_fm.items():
        if k in MUTABLE_FIELDS:
            continue
        if k not in zh_fm:
            issues.append(f"frontmatter 少了字段 `{k}`")
        elif zh_fm[k] != v:
            issues.append(f"frontmatter `{k}` 被改动：{v!r} → {zh_fm[k]!r}")
    for k in zh_fm.keys() - en_fm.keys() - MUTABLE_FIELDS:
        issues.append(f"frontmatter 多了字段 `{k}`")
    # title 与原文相同不一定是漏译：很多 API 页的标题本身就是标识符
    # （`mask`、`buckets`、`viewIsAppearing(_:)`），按规范就该保留英文。
    # 只有当标题像自然语言（含空格且不是纯标识符）时才判为漏译。
    t = en_fm.get("title", "").strip("'\"")
    if t and zh_fm.get("title") == en_fm.get("title"):
        looks_like_identifier = bool(
            re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*(\([^)]*\))?", t)
            or re.fullmatch(r"[+-]?\s*[A-Za-z_][\w:.\-]*", t)
            or re.fullmatch(r"<[A-Za-z0-9_.+-]+\.h>", t)
            # 崩溃信号那类标题整个由全大写标识符加括号组成
            # （`EXC_BAD_ACCESS (SIGSEGV)`、
            #  `EXC_BREAKPOINT (SIGTRAP) and EXC_BAD_INSTRUCTION (SIGILL)`），
            # 去掉全大写词、括号和连接词后什么都不剩，就说明它不是自然语言标题。
            or not re.sub(r"[A-Z][A-Z0-9_]{2,}|[()/]|\b(and|or)\b|\s+", "", t)
        )
        # 框架落地页的标题就是框架自己的名字（`Core Data`、`Push to Talk`），
        # 规范规定框架名不译。判据取三者同时成立，避免顺手放过真漏译。
        is_framework_landing = (
            t == en_fm.get("framework", "").strip("'\"")
            and en_fm.get("symbol_kind") == "module"
            and en_fm.get("role") == "collection"
        )
        # 少数产品集合页也直接以不可翻译的产品名作标题，但其 frontmatter 的
        # framework 是抓取器内部分类值，不能用上面的 framework 判据识别。
        is_preserved_product_title = t in {"Xcode Cloud"}
        if (
            not looks_like_identifier
            and not is_framework_landing
            and not is_preserved_product_title
        ):
            issues.append("title 未翻译（与原文相同）")

    # 2 & 3. 链接与图片目标
    for name, pat in (("链接", LINK), ("图片", IMAGE)):
        a, b = sorted(pat.findall(en_body)), sorted(pat.findall(zh_body))
        if a != b:
            only_en = [x for x in a if x not in b]
            only_zh = [x for x in b if x not in a]
            if only_en:
                issues.append(f"{name}目标丢失或被改：{only_en[:3]}")
            if only_zh:
                issues.append(f"{name}目标凭空多出：{only_zh[:3]}")

    # 4. 代码块
    ea, za = code_blocks(en_body), code_blocks(zh_body)
    if len(ea) != len(za):
        issues.append(f"代码块数量不一致：原文 {len(ea)}，译文 {len(za)}")
    else:
        for i, ((el, ec), (zl, zc)) in enumerate(zip(ea, za), 1):
            if el != zl:
                issues.append(f"第 {i} 个代码块语言标注被改：{el!r} → {zl!r}")
            if len(ec) != len(zc):
                issues.append(f"第 {i} 个代码块行数不一致：{len(ec)} → {len(zc)}")
                continue
            # 跨行块注释要单独跟踪：`/*` 开头的多行注释，**续行往往以空格加正文
            # 开头**（`  Provide just enough information …`），COMMENT 只认行首的
            # // /* * # 标记，认不出这种续行，于是把已正确翻译的注释报成「代码被改动」。
            in_block = False
            for ln, (e, z) in enumerate(zip(ec, zc), 1):
                if in_block:
                    if "*/" in e:
                        in_block = False
                    continue  # 块注释内部允许译
                if COMMENT.match(e):
                    # 单行 `/* … */` 不进入块注释状态，只有未闭合的才进
                    if "/*" in e and "*/" not in e:
                        in_block = True
                    continue  # 整行注释允许译
                ecode, ecmt = split_trailing_comment(e)
                zcode, zcmt = split_trailing_comment(z)
                # 只 rstrip：缩进必须逐字符保留，但代码与行尾注释之间的空格
                # 无意义。不 rstrip 的话「删掉行尾注释」会报成「代码被改动」，
                # 指错方向。
                if ecode.rstrip() != zcode.rstrip():
                    issues.append(f"第 {i} 个代码块第 {ln} 行代码被改动：{e.strip()[:60]!r}")
                    break
                # 代码后面跟着未闭合的 `/*`：块注释从这一行的行尾开始
                if ecmt.startswith("/*") and "*/" not in ecmt:
                    in_block = True
                    continue
                # 注释可以译，但不能整条删掉——那是内容丢失
                if ecmt.strip() and not zcmt.strip():
                    issues.append(
                        f"第 {i} 个代码块第 {ln} 行的注释被删掉：{ecmt.strip()[:60]!r}"
                    )
                    break

    # 5 & 6. 结构
    if headings(en_body) != headings(zh_body):
        issues.append(
            f"标题结构不一致：原文 {headings(en_body)}，译文 {headings(zh_body)}"
        )
    for name, pat in (("列表项", LIST_ITEM), ("表格行", TABLE_ROW)):
        a, b = count(en_body, pat), count(zh_body, pat)
        if a != b:
            issues.append(f"{name}数量不一致：原文 {a}，译文 {b}")

    # 7. callout
    if callouts(en_body) != callouts(zh_body):
        issues.append(f"callout 不一致：原文 {callouts(en_body)}，译文 {callouts(zh_body)}")

    # 8. 结构性文字的固定译法。
    #    按**标题序列逐位对齐**判定，而不是简单看英文有没有残留——因为不统一有
    #    两种形态：一是原样留英文，二是各译一个变体（`### Essentials` 实测出现过
    #    「基础 / 基础知识 / 要点 / 基础要点」四种）。只看残留英文抓不到后者。
    #    对齐的前提是标题数量相等，而这由检查项 5 保证；不相等时它已经报错了，
    #    这里跳过以免连带产生一串错位的假问题。
    en_heads = [ln.strip() for ln in prose_lines(en_body) if HEADING.match(ln.strip())]
    zh_heads = [ln.strip() for ln in prose_lines(zh_body) if HEADING.match(ln.strip())]
    if len(en_heads) == len(zh_heads):
        reported: set[str] = set()
        for e, z in zip(en_heads, zh_heads):
            want = FIXED_LINES.get(e)
            if want and z != want and e not in reported:
                reported.add(e)
                actual = "原样保留英文" if z == e else f"实为 `{z}`"
                issues.append(f"结构性文字未按固定译法：`{e}` 应为 `{want}`（{actual}）")
    en_prose = "\n".join(prose_lines(en_body))
    zh_prose = "\n".join(prose_lines(zh_body))
    for en_form, zh_form in FIXED_INLINE.items():
        if en_form in en_prose and en_form in zh_prose:
            issues.append(f"结构性文字未按固定译法：`{en_form}` 应为 `{zh_form}`")

    # 9. 残留英文
    hits = residual_english(zh_body)
    if hits:
        issues.append(f"疑似未翻译的英文 {len(hits)} 处，首条：{hits[0]!r}")

    return issues


def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    as_json = "--json" in sys.argv
    target = ROOT / (args[0] if args else "apple-docs")

    # 从 zh 路径推 en 路径
    if "/zh" in str(target) or target.name in {"zh", "snapshots-zh"}:
        zh_files = sorted(target.rglob("*.md"))
    else:
        zh_root = target / "zh"
        zh_files = sorted(zh_root.rglob("*.md")) if zh_root.exists() else []

    if not zh_files:
        print(f"{target} 下没有找到译文（zh/ 为空），无需校验")
        return

    results: dict[str, list[str]] = {}
    native_zh = 0
    for zh in zh_files:
        if "/snapshots-zh/" in str(zh):
            en = Path(str(zh).replace("/snapshots-zh/", "/snapshots/", 1))
        else:
            en = Path(str(zh).replace("/zh/", "/en/", 1))
        if not en.exists():
            # 中文来源的博客（ibireme、onevcat 这些）本来就没有英文版，
            # 它们直接躺在 zh/ 下，不是译文，不参与结构比对。
            # 不排除的话会产生几百条误报，校验器就没人看了。
            fm, _ = split_frontmatter(zh.read_text(encoding="utf-8"))
            if fm.get("original_language") == "zh":
                native_zh += 1
                continue
            results[str(zh.relative_to(ROOT))] = ["找不到对应的英文原文"]
            continue
        issues = check_pair(en, zh)
        if issues:
            results[str(zh.relative_to(ROOT))] = issues

    if as_json:
        print(json.dumps(results, ensure_ascii=False, indent=1))
    else:
        checked = len(zh_files) - native_zh
        clean = checked - len(results)
        print(f"校验 {checked} 篇译文：通过 {clean}，有问题 {len(results)}"
              + (f"（另有 {native_zh} 篇中文原生内容，无需比对）" if native_zh else ""))
        for path, issues in list(results.items())[:40]:
            print(f"\n  {path}")
            for i in issues[:6]:
                print(f"    · {i}")
        if len(results) > 40:
            print(f"\n  …还有 {len(results) - 40} 篇有问题，用 --json 看全部")

    sys.exit(1 if results else 0)


if __name__ == "__main__":
    main()
