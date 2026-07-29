#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from segmented_markdown import (  # noqa: E402
    SegmentedMarkdownError,
    build_segmented_document,
    normalize_segment_terms,
    parse_segment_response,
    segment_batches,
    untranslated_generic_terms,
)
from validate import check_pair, residual_english  # noqa: E402


SOURCE = """---
title: 'Using the demo linker'
source_url: 'https://example.com/demo'
translated: false
---

# Using the demo linker

Use `ld.lld` to read the [linker guide](https://example.com/linker) before continuing.

## Overview

| Option | Description |
|---|---|
| `--verbose` | Print verbose diagnostics. |

% ruby -ane 'puts "technical output from the original command line"'

```c
errx(1, "could not open /proc/self/pagemap: %s", strerror(errno));
```
"""


class SegmentedMarkdownTests(unittest.TestCase):
    def test_rebuild_preserves_skeleton_and_passes_strict_validation(self):
        document = build_segmented_document(SOURCE)
        sources = [segment.source for segment in document.segments]
        joined = "\n".join(sources)
        self.assertNotIn("https://example.com/linker", joined)
        self.assertNotIn("`ld.lld`", joined)
        self.assertNotIn("errx(1", joined)
        self.assertNotIn("% ruby", joined)

        translations = {
            segment.id: {
                "Using the demo linker": "使用示例链接器",
                "Use ": "请使用",
                " to read the ": "阅读",
                "linker guide": "链接器指南",
                " before continuing.": "，然后再继续。",
                "Option ": "选项",
                "Description ": "说明",
                "Print verbose diagnostics. ": "输出详细诊断信息。",
            }.get(segment.source, "已翻译：" + segment.source)
            for segment in document.segments
        }
        candidate = document.reconstruct(translations)
        self.assertIn("translated: true", candidate)
        self.assertIn("## 概述", candidate)
        self.assertIn("](https://example.com/linker)", candidate)
        self.assertIn("`ld.lld`", candidate)
        self.assertIn("% ruby -ane", candidate)
        self.assertIn('errx(1, "could not open', candidate)
        linker_segment = next(
            segment for segment in document.segments if segment.source == " to read the "
        )
        fixed_tokens = document.fixed_tokens(linker_segment.line_id)
        self.assertIn("ld.lld", fixed_tokens)
        self.assertIn("https://example.com/linker", fixed_tokens)

        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            en = root / "en.md"
            zh = root / "zh.md"
            en.write_text(SOURCE, encoding="utf-8")
            zh.write_text(candidate, encoding="utf-8")
            self.assertEqual(check_pair(en, zh, strict_identifiers=True), [])

        self.assertEqual(document.extract(candidate), translations)

    def test_fixed_token_spacing_and_generic_english_gate(self):
        document = build_segmented_document(SOURCE)
        translations = {segment.id: "译文" for segment in document.segments}
        before = next(
            segment for segment in document.segments if segment.source == "Use "
        )
        after = next(
            segment for segment in document.segments if segment.source == " to read the "
        )
        normalized = document.normalize_fixed_spacing(translations)
        self.assertEqual(normalized[before.id], "译文 ")
        self.assertEqual(normalized[after.id], " 译文")
        duplicated = dict(translations)
        duplicated[after.id] = "ld.lld 阅读"
        self.assertEqual(
            document.normalize_fixed_spacing(duplicated)[after.id],
            " 阅读",
        )
        self.assertEqual(
            untranslated_generic_terms("the dynamic linker section header"),
            {"dynamic linker", "linker"},
        )
        self.assertEqual(
            normalize_segment_terms("dynamic linkter and linker"),
            "动态链接器 and 链接器",
        )

    def test_candidate_with_changed_fixed_skeleton_is_rejected(self):
        document = build_segmented_document(SOURCE)
        candidate = document.reconstruct(
            {segment.id: "译文" for segment in document.segments}
        )
        candidate = candidate.replace(
            "(https://example.com/linker)",
            "(https://example.com/changed)",
        )
        with self.assertRaises(SegmentedMarkdownError):
            document.extract(candidate)

    def test_json_response_requires_every_id_and_single_line_strings(self):
        parsed = parse_segment_response(
            '```json\n{"translations":{"S000001":"译文一","S000002":"译文二"}}\n```',
            ["S000001", "S000002"],
        )
        self.assertEqual(parsed["S000002"], "译文二")
        with self.assertRaises(SegmentedMarkdownError):
            parse_segment_response(
                json.dumps({"translations": {"S000001": "译文"}}),
                ["S000001", "S000002"],
            )
        self.assertEqual(
            parse_segment_response(
                json.dumps({"translations": {"S000001": "译文"}}),
                ["S000001", "S000002"],
                require_all=False,
            ),
            {"S000001": "译文"},
        )

    def test_malformed_inline_code_does_not_freeze_chinese_prose(self):
        source = """---
title: Demo
translated: false
---

执行`/lib/libc.so: version `GLIBC_2.14' not found`，即系統glibc的`libc.so`。
"""
        document = build_segmented_document(source)
        joined = "".join(segment.source for segment in document.segments)
        self.assertIn("即系統glibc的", joined)
        with self.assertRaises(SegmentedMarkdownError):
            parse_segment_response(
                json.dumps({"translations": {"S000001": "第一行\n第二行"}}),
                ["S000001"],
            )

    def test_batch_limits_are_bounded(self):
        document = build_segmented_document(SOURCE)
        batches = segment_batches(document.segments, max_chars=80, max_items=2)
        self.assertGreater(len(batches), 1)
        batch_by_segment = {
            segment.id: index
            for index, batch in enumerate(batches)
            for segment in batch
        }
        for line_id in {segment.line_id for segment in document.segments}:
            indexes = {
                batch_by_segment[segment.id]
                for segment in document.segments
                if segment.line_id == line_id
            }
            self.assertEqual(len(indexes), 1)

    def test_source_aware_residual_check_only_exempts_exact_technical_lines(self):
        technical = "% ruby -ane 'puts \"many english words from command output\"'"
        prose = "This ordinary English sentence should still be translated before publication"
        source = technical + "\n" + prose
        self.assertEqual(residual_english(technical, source), [])
        self.assertEqual(len(residual_english(prose, source)), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
