#!/usr/bin/env python3
"""暑期知识地图生成辅助函数的离线回归测试。"""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

from studyplan import (  # noqa: E402
    article_value_key,
    classify,
    module_entry_matches,
    parse_plan_steps_text,
    parse_plan_text,
    summer_module_for,
    table_text,
    title_from_path,
)


class SummerIndexTests(unittest.TestCase):
    def test_plan_heading_maps_to_a_stable_module(self):
        module = summer_module_for("模块 3：Runtime：消息发送、转发、Category、KVO")
        self.assertIsNotNone(module)
        self.assertEqual(module["slug"], "03-runtime")

    def test_frontmatter_title_is_used_when_page_has_no_h1(self):
        with tempfile.TemporaryDirectory() as directory:
            page = Path(directory) / "article.md"
            page.write_text(
                "---\ntitle: 'Objective-C Runtime 入门'\n---\n\n正文\n",
                encoding="utf-8",
            )
            self.assertEqual(title_from_path(page), "Objective-C Runtime 入门")

    def test_link_heading_is_rendered_as_plain_title(self):
        with tempfile.TemporaryDirectory() as directory:
            page = Path(directory) / "article.md"
            page.write_text(
                "# [Objective-C 引用计数原理](https://example.com)\n",
                encoding="utf-8",
            )
            self.assertEqual(title_from_path(page), "Objective-C 引用计数原理")

    def test_current_plan_modules_and_steps_are_parsed(self):
        text = """## 模块 1：对象模型

| 步骤 | 内容 | 产出 |
|---|---|---|
| 1.1 | 虚拟内存 | 内存图 |

- [资料](https://example.com/memory)

## 模块 8：操作系统基础

| 方向 | 必学内容 | 交付 |
|---|---|---|
| 操作系统 | 进程与线程 | 一句话定义 |

## 暑假结束时的总验收

- [不属于模块](https://example.com/audit)
"""
        self.assertEqual(
            parse_plan_text(text),
            [{"module": "模块 1：对象模型", "url": "https://example.com/memory"}],
        )
        self.assertEqual(
            parse_plan_steps_text(text),
            {
                "模块 1：对象模型": [("1.1", "虚拟内存", "内存图")],
                "模块 8：操作系统基础": [("操作系统", "进程与线程", "一句话定义")],
            },
        )

    def test_module_matching_honors_topic_and_title_pattern(self):
        module = summer_module_for("模块 3：Runtime")
        matching = {
            "topics": ("Objective-C Runtime",),
            "en_title": "Objective-C message dispatch",
            "zh_title": "",
            "title_alias": "",
        }
        unrelated = {
            "topics": ("Objective-C Runtime",),
            "en_title": "Objective-C language overview",
            "zh_title": "",
            "title_alias": "",
        }
        self.assertTrue(module_entry_matches(module, matching))
        self.assertFalse(module_entry_matches(module, unrelated))

    def test_github_links_to_both_vaults_resolve_locally(self):
        own = (
            "https://github.com/Biscoffee/apple-docs-vault/blob/main/"
            "blogs/zh/mikeash/key-value-observing-done-right.md"
        )
        archive = (
            "https://github.com/XiyouMobile3G-iOS/apple-developer-archive-vault/"
            "blob/main/documentation/Darwin/Kernel%20Programming%20Guide/"
            "Memory%20and%20Virtual%20Memory.md"
        )
        own_cat, own_file, _ = classify(own, {}, {})
        archive_cat, archive_file, _ = classify(archive, {}, {})
        self.assertEqual(own_cat, "本仓库资料")
        self.assertTrue(own_file.is_file())
        self.assertEqual(archive_cat, "Apple 旧归档")
        self.assertTrue(archive_file.is_file())

    def test_plan_material_is_sorted_before_other_articles(self):
        plan = {
            "source_url": "https://example.com/plan",
            "kind": "技术博客",
            "source_key": "other",
            "en_title": "Plan article",
            "zh_title": "",
            "title_alias": "",
        }
        official = {
            "source_url": "https://example.com/official",
            "kind": "Apple 文档",
            "source_key": "foundation",
            "en_title": "Official article",
            "zh_title": "",
            "title_alias": "",
        }
        self.assertLess(
            article_value_key(plan, {"example.com/plan"}),
            article_value_key(official, {"example.com/plan"}),
        )

    def test_table_text_escapes_markdown_column_separator(self):
        self.assertEqual(table_text("A | B"), r"A \| B")


if __name__ == "__main__":
    unittest.main()
