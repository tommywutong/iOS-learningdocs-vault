#!/usr/bin/env python3
"""把 Markdown 拆成只含自然语言的可翻译片段，并由原文骨架确定性重建。

模型不会收到需要原样返回的 Markdown 骨架，也不会负责输出代码块、链接目标、
图片路径或行内代码。它只按片段 ID 返回自然语言译文。
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from typing import Any

from validate import (
    FENCE,
    FIXED_INLINE,
    FIXED_LINES,
    looks_like_technical_output_continuation,
    looks_like_technical_output_line,
)

SEGMENT_MARKER = "\x00APPLE_DOCS_SEGMENT_{:06d}\x00"
MARKER_PATTERN = re.compile(r"\x00APPLE_DOCS_SEGMENT_(\d{6})\x00")
FRONTMATTER_TITLE = re.compile(
    r"^(?P<prefix>\s*title:\s*)(?P<quote>['\"]?)(?P<value>.*?)(?P=quote)$"
)
FRONTMATTER_TRANSLATED = re.compile(
    r"^(?P<prefix>\s*translated:\s*)(?:false|true)(?P<suffix>\s*)$",
    re.IGNORECASE,
)
MARKDOWN_LINK = re.compile(
    r"(?P<image>!)?\[(?P<label>[^\]]*)\]\((?P<target><?[^)\n]+>?)\)"
)
INLINE_CODE = re.compile(r"(?P<ticks>`+)(?P<value>[^\n]*?)(?P=ticks)")
RAW_URL = re.compile(r"https?://[^\s<>)]+")
HTML_TAG = re.compile(r"</?[A-Za-z][^>\n]*>")
CALLOUT_MARKER = re.compile(r"\[![A-Za-z0-9_-]+\]")
MARKDOWN_MARKER = re.compile(r"\||\*{1,3}|_{1,3}|~{2}|\\.")
CODE_LIKE_TOKEN = re.compile(
    r"""
    (?<![A-Za-z0-9_])
    (?:
        --?[A-Za-z0-9][A-Za-z0-9_.,=+:/-]*
      | /[A-Za-z0-9_.+/-]+
      | [A-Za-z_]\w*(?:::[A-Za-z_]\w*)+
      | info\s+'[^'\n]*\)?\s*
      | [A-Za-z_][A-Za-z0-9_]*(?:-[A-Za-z0-9_+.]+)+(?:\.[A-Za-z0-9_+-]+)*
      | [A-Za-z_]\w*(?:\.[A-Za-z_]\w*)+
      | [A-Z][A-Z0-9_]{2,}
      | [A-Za-z_]\w*\([^)\n]*\)
    )
    """,
    re.VERBOSE,
)
SPECIAL = re.compile(
    "|".join(
        f"(?P<{name}>{pattern.pattern})"
        for name, pattern in (
            ("link", MARKDOWN_LINK),
            ("inline", INLINE_CODE),
            ("url", RAW_URL),
            ("html", HTML_TAG),
            ("callout", CALLOUT_MARKER),
            ("markdown", MARKDOWN_MARKER),
            ("code_token", CODE_LIKE_TOKEN),
        )
    ),
    re.VERBOSE,
)
TRADITIONAL_CHARS = set(
    "問舊環裏於對現壓執錯誤統號參庫兩編譯機較實軟鏈認徑變種將賴這樣證"
    "蓋後辦構並載來簡稱爲項觀幾個調無產東慮還輕運進處裝從與發會為應開"
)
GENERIC_TRANSLATABLE_TERMS = (
    "dynamic linker",
    "linker",
)


class SegmentedMarkdownError(ValueError):
    """分段或确定性重建失败。"""


@dataclass(frozen=True)
class Segment:
    id: str
    source: str
    context: str
    line_id: str


@dataclass(frozen=True)
class LineTemplate:
    template: str
    newline: str

    @property
    def segment_ids(self) -> list[str]:
        return [
            f"S{int(number):06d}"
            for number in MARKER_PATTERN.findall(self.template)
        ]


@dataclass
class SegmentedDocument:
    lines: list[LineTemplate]
    segments: list[Segment]

    def line_parts(
        self,
        line_id: str,
        *,
        candidates: dict[str, str] | None = None,
    ) -> list[dict[str, str]]:
        """返回一行中交错排列的待译 part 与只读 fixed part。"""
        try:
            line_number = int(line_id[1:])
            line = self.lines[line_number - 1]
        except (ValueError, IndexError) as exc:
            raise SegmentedMarkdownError(f"无效的行 ID：{line_id}") from exc
        source_map = {segment.id: segment.source for segment in self.segments}
        output: list[dict[str, str]] = []
        position = 0
        for match in MARKER_PATTERN.finditer(line.template):
            literal = line.template[position : match.start()]
            if literal:
                output.append({"fixed": literal})
            segment_id = f"S{int(match.group(1)):06d}"
            part = {"id": segment_id, "source": source_map[segment_id]}
            if candidates is not None:
                part["candidate"] = candidates[segment_id]
            output.append(part)
            position = match.end()
        literal = line.template[position:]
        if literal:
            output.append({"fixed": literal})
        return output

    def fixed_tokens(self, line_id: str) -> set[str]:
        """提取一行中模型不得在译文 part 内重复输出的固定标识符。"""
        tokens: set[str] = set()
        for part in self.line_parts(line_id):
            fixed = part.get("fixed")
            if not fixed:
                continue
            for match in INLINE_CODE.finditer(fixed):
                value = match.group("value")
                if len(value) >= 2:
                    tokens.add(value)
            for pattern in (RAW_URL, CODE_LIKE_TOKEN):
                for match in pattern.finditer(fixed):
                    value = match.group(0)
                    if len(value) >= 2:
                        tokens.add(value)
        return tokens

    def normalize_fixed_spacing(
        self,
        translations: dict[str, str],
        segment_ids: set[str] | None = None,
    ) -> dict[str, str]:
        """在中文与相邻固定英文标识符之间补可读空格，不触碰固定内容。"""
        normalized = dict(translations)
        selected = segment_ids or set(normalized)
        for line_number, line in enumerate(self.lines, 1):
            line_id = f"L{line_number:06d}"
            parts = self.line_parts(line_id)
            fixed_tokens = self.fixed_tokens(line_id)
            for index, part in enumerate(parts):
                segment_id = part.get("id")
                if not segment_id or segment_id not in selected:
                    continue
                value = normalized[segment_id]
                previous = parts[index - 1].get("fixed", "") if index else ""
                following = (
                    parts[index + 1].get("fixed", "")
                    if index + 1 < len(parts)
                    else ""
                )
                previous_token = _fixed_boundary_token(
                    previous,
                    fixed_tokens,
                    at_start=False,
                )
                following_token = _fixed_boundary_token(
                    following,
                    fixed_tokens,
                    at_start=True,
                )
                if previous_token:
                    stripped = value.lstrip()
                    for form in (f"`{previous_token}`", previous_token):
                        if stripped.startswith(form):
                            value = value[: len(value) - len(stripped)] + stripped[
                                len(form) :
                            ].lstrip()
                            break
                if following_token:
                    stripped = value.rstrip()
                    for form in (f"`{following_token}`", following_token):
                        if stripped.endswith(form):
                            value = stripped[: -len(form)].rstrip() + value[
                                len(stripped) :
                            ]
                            break
                if (
                    value
                    and re.match(r"[\u3400-\u9fff]", value)
                    and _fixed_ends_with_token(previous, fixed_tokens)
                    and not value.startswith(" ")
                ):
                    value = " " + value
                if (
                    value
                    and re.search(r"[\u3400-\u9fff]$", value)
                    and _fixed_starts_with_token(following, fixed_tokens)
                    and not value.endswith(" ")
                ):
                    value += " "
                normalized[segment_id] = value
        return normalized

    def reconstruct(self, translations: dict[str, str]) -> str:
        expected = {segment.id for segment in self.segments}
        missing = sorted(expected - translations.keys())
        if missing:
            raise SegmentedMarkdownError(f"缺少片段译文：{missing[:5]}")
        for segment_id in expected:
            value = translations[segment_id]
            if not isinstance(value, str):
                raise SegmentedMarkdownError(f"片段 {segment_id} 的译文不是字符串")
            if "\n" in value or "\r" in value or "\x00" in value:
                raise SegmentedMarkdownError(f"片段 {segment_id} 的译文破坏行结构")

        output: list[str] = []
        for line in self.lines:
            rendered = MARKER_PATTERN.sub(
                lambda match: translations[f"S{int(match.group(1)):06d}"],
                line.template,
            )
            output.append(rendered + line.newline)
        return "".join(output)

    def extract(self, candidate: str) -> dict[str, str]:
        """从同一骨架生成的候选中反向提取片段译文，供独立审校使用。"""
        candidate_lines = candidate.splitlines(keepends=True)
        if len(candidate_lines) != len(self.lines):
            raise SegmentedMarkdownError(
                f"候选行数与原文骨架不一致：{len(candidate_lines)} != {len(self.lines)}"
            )

        extracted: dict[str, str] = {}
        for index, (line, candidate_line) in enumerate(
            zip(self.lines, candidate_lines),
            1,
        ):
            body, newline = _split_newline(candidate_line)
            if newline != line.newline:
                raise SegmentedMarkdownError(f"候选第 {index} 行换行结构不一致")
            ids = line.segment_ids
            if not ids:
                if body != line.template:
                    raise SegmentedMarkdownError(
                        f"候选第 {index} 行修改了不可翻译骨架"
                    )
                continue
            pattern_parts: list[str] = []
            position = 0
            for match in MARKER_PATTERN.finditer(line.template):
                pattern_parts.append(re.escape(line.template[position : match.start()]))
                segment_id = f"S{int(match.group(1)):06d}"
                pattern_parts.append(f"(?P<{segment_id}>.*?)")
                position = match.end()
            pattern_parts.append(re.escape(line.template[position:]))
            matched = re.fullmatch("".join(pattern_parts), body)
            if not matched:
                raise SegmentedMarkdownError(
                    f"候选第 {index} 行无法按原文骨架对齐"
                )
            for segment_id in ids:
                value = matched.group(segment_id)
                if segment_id in extracted and extracted[segment_id] != value:
                    raise SegmentedMarkdownError(f"片段 {segment_id} 重复且内容不一致")
                extracted[segment_id] = value

        missing = [segment.id for segment in self.segments if segment.id not in extracted]
        if missing:
            raise SegmentedMarkdownError(f"候选缺少可审校片段：{missing[:5]}")
        return extracted


class _Builder:
    def __init__(self) -> None:
        self.segments: list[Segment] = []

    def add_segment(self, text: str, context: str, line_id: str) -> str:
        if not re.search(r"[A-Za-z\u3400-\u9fff]", text):
            return text
        segment_id = f"S{len(self.segments) + 1:06d}"
        self.segments.append(Segment(segment_id, text, context[:1200], line_id))
        return SEGMENT_MARKER.format(len(self.segments))

    def scan(self, text: str, context: str, line_id: str) -> str:
        output: list[str] = []
        position = 0
        for match in SPECIAL.finditer(text):
            output.append(
                self.add_segment(text[position : match.start()], context, line_id)
            )
            if match.lastgroup == "link":
                link = MARKDOWN_LINK.fullmatch(match.group(0))
                assert link is not None
                output.append("![" if link.group("image") else "[")
                output.append(self.scan(link.group("label"), context, line_id))
                output.append(f"]({link.group('target')})")
            elif match.lastgroup == "inline" and re.search(
                r"[\u3400-\u9fff]",
                match.group(0),
            ):
                inline = INLINE_CODE.fullmatch(match.group(0))
                assert inline is not None
                ticks = inline.group("ticks")
                output.append(ticks)
                output.append(self.scan(inline.group("value"), context, line_id))
                output.append(ticks)
            else:
                output.append(match.group(0))
            position = match.end()
        output.append(self.add_segment(text[position:], context, line_id))
        return "".join(output)


def _split_newline(line: str) -> tuple[str, str]:
    if line.endswith("\r\n"):
        return line[:-2], "\r\n"
    if line.endswith("\n") or line.endswith("\r"):
        return line[:-1], line[-1]
    return line, ""


def _leading_markdown_prefix(text: str) -> tuple[str, str]:
    position = len(text) - len(text.lstrip(" \t"))
    while text.startswith(">", position):
        position += 1
        if position < len(text) and text[position] == " ":
            position += 1
    structural = re.match(
        r"(?:#{1,6}\s+|(?:[-*+]|\d+\.)\s+(?:\[[ xX]\]\s+)?)",
        text[position:],
    )
    if structural:
        position += structural.end()
    return text[:position], text[position:]


def build_segmented_document(source: str) -> SegmentedDocument:
    builder = _Builder()
    lines: list[LineTemplate] = []
    in_frontmatter = source.startswith("---\n") or source.startswith("---\r\n")
    frontmatter_started = False
    in_code = False
    technical_run = False

    for line_number, raw_line in enumerate(source.splitlines(keepends=True), 1):
        body, newline = _split_newline(raw_line)
        context = body
        line_id = f"L{line_number:06d}"

        if in_frontmatter:
            if body == "---":
                lines.append(LineTemplate(body, newline))
                if frontmatter_started:
                    in_frontmatter = False
                else:
                    frontmatter_started = True
                continue
            title = FRONTMATTER_TITLE.match(body)
            if title:
                value = title.group("value")
                template = (
                    title.group("prefix")
                    + title.group("quote")
                    + builder.add_segment(value, context, line_id)
                    + title.group("quote")
                )
                lines.append(LineTemplate(template, newline))
                continue
            translated = FRONTMATTER_TRANSLATED.match(body)
            if translated:
                lines.append(
                    LineTemplate(
                        translated.group("prefix") + "true" + translated.group("suffix"),
                        newline,
                    )
                )
                continue
            lines.append(LineTemplate(body, newline))
            continue

        if in_code:
            lines.append(LineTemplate(body, newline))
            if body.strip().startswith("```"):
                in_code = False
            continue
        if FENCE.match(body):
            in_code = True
            lines.append(LineTemplate(body, newline))
            continue
        if not body.strip():
            technical_run = False
        starts_technical = looks_like_technical_output_line(body)
        if starts_technical or (
            technical_run and looks_like_technical_output_continuation(body)
        ):
            lines.append(LineTemplate(body, newline))
            technical_run = bool(body.strip())
            continue
        technical_run = False

        stripped = body.strip()
        if stripped in FIXED_LINES:
            indentation = body[: len(body) - len(body.lstrip())]
            lines.append(LineTemplate(indentation + FIXED_LINES[stripped], newline))
            continue

        fixed = body
        for english, chinese in FIXED_INLINE.items():
            fixed = fixed.replace(english, chinese)
        prefix, content = _leading_markdown_prefix(fixed)
        lines.append(
            LineTemplate(
                prefix + builder.scan(content, context, line_id),
                newline,
            )
        )

    if not source or source.endswith(("\n", "\r")):
        pass
    elif not lines:
        lines.append(LineTemplate("", ""))
    return SegmentedDocument(lines, builder.segments)


def parse_segment_response(
    content: str,
    expected_ids: list[str],
    *,
    require_all: bool = True,
) -> dict[str, str]:
    """解析模型返回的 JSON，并拒绝缺失片段或会破坏骨架的值。"""
    text = content.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text, count=1, flags=re.IGNORECASE)
        text = re.sub(r"\s*```$", "", text, count=1)
    try:
        payload: Any = json.loads(text)
    except json.JSONDecodeError as exc:
        start, end = text.find("{"), text.rfind("}")
        if start < 0 or end <= start:
            raise SegmentedMarkdownError("模型没有返回可解析的 JSON") from exc
        try:
            payload = json.loads(text[start : end + 1])
        except json.JSONDecodeError as nested:
            raise SegmentedMarkdownError("模型没有返回可解析的 JSON") from nested

    if isinstance(payload, dict) and isinstance(payload.get("translations"), dict):
        payload = payload["translations"]
    if not isinstance(payload, dict):
        raise SegmentedMarkdownError("模型 JSON 顶层必须是对象")

    expected = set(expected_ids)
    result = {key: value for key, value in payload.items() if key in expected}
    missing = sorted(expected - result.keys())
    if missing and require_all:
        raise SegmentedMarkdownError(f"模型漏掉片段：{missing[:5]}")
    for key, value in result.items():
        if not isinstance(value, str):
            raise SegmentedMarkdownError(f"片段 {key} 的译文不是字符串")
        if "\n" in value or "\r" in value or "\x00" in value:
            raise SegmentedMarkdownError(f"片段 {key} 的译文破坏行结构")
    return result


def traditional_characters(text: str) -> set[str]:
    """返回高置信度的繁体字；仅检查模型负责的自然语言片段。"""
    return set(text) & TRADITIONAL_CHARS


def untranslated_generic_terms(text: str) -> set[str]:
    """找出模型自然语言译文里不应原样残留的通用技术名词。"""
    return {
        term
        for term in GENERIC_TRANSLATABLE_TERMS
        if re.search(rf"\b{re.escape(term)}\b", text, re.IGNORECASE)
    }


def normalize_segment_terms(text: str) -> str:
    """落实 TERMS.md 已明确裁决的通用术语，不处理术语表未覆盖的词。"""
    normalized = re.sub(
        r"\bdynamic\s+link(?:er|ter)\b",
        "动态链接器",
        text,
        flags=re.IGNORECASE,
    )
    return re.sub(r"\blinker\b", "链接器", normalized, flags=re.IGNORECASE)


def _fixed_starts_with_token(fixed: str, tokens: set[str]) -> bool:
    stripped = fixed.lstrip()
    return any(
        stripped.startswith(token) or stripped.startswith(f"`{token}`")
        for token in tokens
    )


def _fixed_ends_with_token(fixed: str, tokens: set[str]) -> bool:
    stripped = fixed.rstrip()
    return any(
        stripped.endswith(token) or stripped.endswith(f"`{token}`")
        for token in tokens
    )


def _fixed_boundary_token(
    fixed: str,
    tokens: set[str],
    *,
    at_start: bool,
) -> str | None:
    stripped = fixed.strip()
    for token in sorted(tokens, key=len, reverse=True):
        forms = (token, f"`{token}`")
        if any(
            stripped.startswith(form) if at_start else stripped.endswith(form)
            for form in forms
        ):
            return token
    return None


def segment_batches(
    segments: list[Segment],
    *,
    max_chars: int = 12_000,
    max_items: int = 80,
) -> list[list[Segment]]:
    batches: list[list[Segment]] = []
    current: list[Segment] = []
    current_chars = 0
    groups: list[list[Segment]] = []
    for segment in segments:
        if not groups or groups[-1][0].line_id != segment.line_id:
            groups.append([])
        groups[-1].append(segment)
    for group in groups:
        size = sum(len(segment.source) for segment in group) + len(group[0].context)
        if current and (
            current_chars + size > max_chars
            or len(current) + len(group) > max_items
        ):
            batches.append(current)
            current = []
            current_chars = 0
        current.extend(group)
        current_chars += size
    if current:
        batches.append(current)
    return batches
