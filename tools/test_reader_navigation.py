#!/usr/bin/env python3
"""读者导航与目录标题的离线回归测试；不会访问网络。"""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

from reader_navigation import (  # noqa: E402
    classify_subtopic,
    display_status,
    is_reader_visible_title,
    load_title_aliases,
    preferred_title,
    status_rank,
    title_alias_for,
    topic_slug,
)
from title_aliases import (  # noqa: E402
    normalize_title_alias,
    summarize_state,
    validate_response,
)
from indexes import classify_topics, item  # noqa: E402


class ReaderVisibilityTests(unittest.TestCase):
    def test_archive_titles_and_pagination_urls_are_hidden(self):
        self.assertFalse(is_reader_visible_title("Archives"))
        self.assertFalse(is_reader_visible_title("About"))
        self.assertFalse(is_reader_visible_title("previous"))
        self.assertFalse(
            is_reader_visible_title(
                "OneV’s Den",
                "https://onevcat.com/page14/",
            )
        )
        self.assertTrue(
            is_reader_visible_title(
                "Swift 中的错误处理",
                "https://onevcat.com/2016/03/swift-error-handling/",
            )
        )

    def test_stable_topic_slug_and_subtopic(self):
        self.assertEqual(topic_slug("内存与 ARC"), "memory-arc")
        self.assertEqual(
            classify_subtopic("内存与 ARC", "Understanding autorelease pools"),
            "ARC 与引用计数",
        )
        self.assertEqual(
            classify_subtopic(
                "Objective-C Runtime",
                "Using associated references in an Objective-C category",
            ),
            "Category、Swizzling 与关联对象",
        )

    def test_runtime_rules_do_not_match_unrelated_isa_architectures(self):
        self.assertNotIn(
            "Objective-C Runtime",
            classify_topics("Linker notes on Power ISA"),
        )

    def test_source_name_alone_does_not_assign_a_topic(self):
        entry = item(
            kind="技术博客",
            source_key="objccn",
            source_name="ObjC 中国",
            en=None,
            zh=None,
            source_url="",
        )
        self.assertEqual(entry["topics"], ())


class ReaderPriorityTests(unittest.TestCase):
    def test_real_chinese_title_wins_over_alias(self):
        entry = {
            "zh_title": "理解 ARC",
            "title_alias": "ARC 原理",
            "en_title": "Understanding ARC",
        }
        self.assertEqual(preferred_title(entry), "理解 ARC")

    def test_alias_replaces_all_english_translated_title(self):
        entry = {
            "zh_title": "Friday Q&A: ARC",
            "title_alias": "Friday Q&A：理解 ARC",
            "en_title": "Friday Q&A: ARC",
        }
        self.assertEqual(preferred_title(entry), "Friday Q&A：理解 ARC")

    def test_title_only_is_not_counted_as_full_translation(self):
        entry = {
            "status": "待翻译",
            "title_alias": "理解 ARC",
            "reader_visible": True,
        }
        self.assertEqual(display_status(entry), "仅标题中文，正文待翻译")
        self.assertEqual(status_rank(entry), 2)


class AliasFileTests(unittest.TestCase):
    def test_alias_requires_exact_current_english_title(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            en = root / "blogs" / "en" / "demo" / "article.md"
            en.parent.mkdir(parents=True)
            en.write_text("# New title\n", encoding="utf-8")
            aliases_path = root / "meta" / "blog_title_aliases.json"
            aliases_path.parent.mkdir()
            aliases_path.write_text(
                json.dumps(
                    {
                        "version": 1,
                        "titles": {
                            "blogs/en/demo/article.md": {
                                "en_title": "Old title",
                                "zh_title": "旧标题",
                            }
                        },
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            aliases = load_title_aliases(root)
            with self.assertRaisesRegex(ValueError, "已过期"):
                title_alias_for(
                    en,
                    root=root,
                    aliases=aliases,
                    current_title="New title",
                )

    def test_model_response_requires_exact_ids(self):
        batch = [
            {"id": "T00001", "title": "Memory"},
            {"id": "T00002", "title": "Runtime"},
        ]
        with self.assertRaisesRegex(Exception, "标题 ID 不匹配"):
            validate_response(
                '{"titles":{"T00001":"内存"}}',
                batch,
            )
        self.assertEqual(
            validate_response(
                '```json\n{"titles":{"T00001":"内存","T00002":"运行时"}}\n```',
                batch,
            ),
            {"T00001": "内存", "T00002": "运行时"},
        )

    def test_social_hashtag_can_be_a_real_title(self):
        batch = [
            {"id": "T00001", "title": "#TalkPay"},
            {"id": "T00002", "title": "-fno-semantic-interposition"},
        ]
        self.assertEqual(
            validate_response(
                '{"titles":{"T00001":"#TalkPay",'
                '"T00002":"-fno-semantic-interposition"}}',
                batch,
            ),
            {
                "T00001": "#TalkPay",
                "T00002": "-fno-semantic-interposition",
            },
        )

    def test_known_series_prefixes_are_chinese(self):
        self.assertEqual(
            normalize_title_alias("Friday Q&A 2018-01-01: Swift"),
            "星期五问答 2018-01-01: Swift",
        )
        self.assertEqual(
            normalize_title_alias("[objc explain]: objc_msgSend"),
            "[objc 解析]: objc_msgSend",
        )
        self.assertEqual(
            normalize_title_alias("介绍ComponentKit：iOS上的 UI"),
            "介绍 ComponentKit：iOS 上的 UI",
        )

    def test_failed_calls_are_included_in_cost_summary(self):
        state = {
            "target_count": 1,
            "batches": [],
            "failures": [
                {
                    "batch": 1,
                    "error": "格式错误",
                    "calls": [
                        {
                            "usage": {
                                "prompt_tokens": 10,
                                "completion_tokens": 5,
                            },
                            "estimated_cost_usd": 0.01,
                        }
                    ],
                }
            ],
        }
        with patch("builtins.print") as mocked_print:
            summarize_state(state)
        output = "\n".join(str(call.args[0]) for call in mocked_print.call_args_list)
        self.assertIn("API 1 次", output)
        self.assertIn("估算 $0.0100", output)


if __name__ == "__main__":
    unittest.main()
