#!/usr/bin/env python3
"""暑期强相关 B 类白名单的离线测试。"""
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import summer_related_b as scope  # noqa: E402


class SummerRelatedBScopeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # B 类范围一经人工批准就以冻结清单为准。不能用动态“待译集合”
        # 作为测试基线，否则文件翻译完成后会从集合消失，反而导致范围测试失败。
        cls.data = json.loads(scope.MANIFEST.read_text(encoding="utf-8"))
        cls.paths = {item["en"] for item in cls.data["files"]}

    def test_scope_is_bounded_but_substantial(self):
        self.assertGreater(len(self.paths), 100)
        self.assertLess(len(self.paths), 1000)
        self.assertEqual(len(self.paths), self.data["file_count"])

    def test_required_smoke_documents_are_included(self):
        required = set(scope.SMOKE_FILES)
        self.assertTrue(required <= self.paths)
        self.assertEqual(list(scope.SMOKE_FILES), self.data["smoke_files"])

    def test_existing_or_off_topic_content_is_excluded(self):
        self.assertFalse(any("/storekit/" in path for path in self.paths))
        self.assertFalse(any("/objcio/" in path for path in self.paths))
        self.assertNotIn(
            "blogs/en/oleb/is-it-immoral-to-not-block-ads.md",
            self.paths,
        )

    def test_paths_exist_and_targets_match(self):
        for item in self.data["files"]:
            self.assertTrue((ROOT / item["en"]).is_file(), item["en"])
            self.assertEqual(
                item["en"].replace("/en/", "/zh/", 1),
                item["zh"],
            )
            self.assertTrue(item["themes"], item["en"])

    def test_frozen_manifest_is_valid(self):
        scope.validate_frozen_manifest(self.data)


if __name__ == "__main__":
    unittest.main()
