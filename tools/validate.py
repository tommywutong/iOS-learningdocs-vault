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

FENCE = re.compile(r"^```(\w*)\s*$")
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(<?([^)>]+)>?\)")
IMAGE = re.compile(r"!\[[^\]]*\]\(<?([^)>]+)>?\)")
HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
CALLOUT = re.compile(r"^>\s*\[!(\w+)\]")
LIST_ITEM = re.compile(r"^\s*(?:[-*+]|\d+\.)\s+")
TABLE_ROW = re.compile(r"^\s*\|.*\|\s*$")
COMMENT = re.compile(r"^\s*(//|/\*|\*|#|--)")
INLINE_CODE = re.compile(r"`[^`]*`")

# 允许译文改动的 frontmatter 字段
MUTABLE_FIELDS = {"title", "translated", "translated_at", "translator", "reviewed"}


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
        elif line.strip() == "```" and inside:
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
        if FENCE.match(line) or (line.strip() == "```" and inside):
            inside = not inside if not (line.strip() == "```" and inside) else False
            continue
        if not inside:
            out.append(line)
    return "\n".join(out)


def headings(body: str) -> list[int]:
    return [len(m.group(1)) for line in body.splitlines() if (m := HEADING.match(line))]


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
        if re.search(r"[一-鿿]", s):
            continue
        s = INLINE_CODE.sub(" ", s)
        s = re.sub(r"\]\([^)]*\)", "] ", s)
        s = re.sub(r"https?://\S+", " ", s)
        s = re.sub(r"^#{1,6}\s+|^\s*(?:[-*+]|\d+\.)\s+|^>\s*", "", s)
        s = re.sub(r"<[^>]+>", " ", s)
        words = re.findall(r"\b[A-Za-z][A-Za-z'’-]*\b", s)
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
        )
        if not looks_like_identifier:
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
            for ln, (e, z) in enumerate(zip(ec, zc), 1):
                if COMMENT.match(e):
                    continue  # 注释允许译
                if e != z:
                    issues.append(f"第 {i} 个代码块第 {ln} 行代码被改动：{e.strip()[:60]!r}")
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

    # 8. 残留英文
    hits = residual_english(zh_body)
    if hits:
        issues.append(f"疑似未翻译的英文 {len(hits)} 处，首条：{hits[0]!r}")

    return issues


def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    as_json = "--json" in sys.argv
    target = ROOT / (args[0] if args else "apple-docs")

    # 从 zh 路径推 en 路径
    if "/zh" in str(target) or target.name == "zh":
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
