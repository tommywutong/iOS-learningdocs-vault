#!/usr/bin/env python3
"""网页快照图片本地化工具的离线测试。"""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

from snapshot_assets import article_key, extension, remote_targets, replace_target  # noqa: E402


class SnapshotAssetTests(unittest.TestCase):
    def test_extracts_only_remote_markdown_images(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "example.md"
            path.write_text(
                "![A](https://cdn.example/a.png)\n![B](../../../local.webp)\n",
                encoding="utf-8",
            )
            self.assertEqual(remote_targets(path), ["https://cdn.example/a.png"])

    def test_replaces_only_image_target_form(self):
        source = "![A](https://cdn.example/a.png)\n"
        self.assertEqual(
            replace_target(source, "https://cdn.example/a.png", "../../../a.png"),
            "![A](../../../a.png)\n",
        )

    def test_content_type_controls_extension(self):
        self.assertEqual(extension("image/webp; charset=binary", "https://x/a"), ".webp")
        self.assertIsNone(extension("text/html", "https://x/a"))

    def test_article_key_uses_source_url(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "example.md"
            path.write_text(
                "---\nsource_url: 'https://example.com/post'\n---\n",
                encoding="utf-8",
            )
            self.assertEqual(len(article_key(path)), 12)


if __name__ == "__main__":
    unittest.main()
