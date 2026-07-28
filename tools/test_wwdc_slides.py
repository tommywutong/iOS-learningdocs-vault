#!/usr/bin/env python3
"""wwdc_slides.py 的纯本地单元测试。"""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import tools.wwdc_slides as slides


class WwdcSlidesTests(unittest.TestCase):
    def test_discover_and_link_are_deterministic(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            en = root / "wwdc/en/wwdc2018/416-demo.md"
            zh = root / "wwdc/zh/wwdc2018/416-demo.md"
            en.parent.mkdir(parents=True)
            zh.parent.mkdir(parents=True)
            body = """---
title: Demo
session_id: 416
collection: wwdc2018
source_url: 'https://developer.apple.com/videos/play/wwdc2018/416/'
---

## Resources

- [Presentation Slides (PDF)](https://example.com/416.pdf?dl=1)
"""
            en.write_text(body, encoding="utf-8")
            zh.write_text(body.replace("## Resources", "## 相关资源"), encoding="utf-8")
            with (
                patch.object(slides, "ROOT", root),
                patch.object(slides, "WWDC_EN", root / "wwdc/en"),
                patch.object(slides, "WWDC_ZH", root / "wwdc/zh"),
                patch.object(slides, "CACHE", root / ".cache/wwdc-slides"),
                patch.object(slides, "OUTPUT", root / "wwdc/slides"),
            ):
                sessions = slides.discover()
                self.assertEqual(len(sessions), 1)
                session = sessions[0]
                self.assertEqual(session.key, "wwdc2018/416")
                link = slides.transcript_link(session, chinese=False)
                self.assertTrue(slides.add_transcript_link(en, link))
                self.assertFalse(slides.add_transcript_link(en, link))
                self.assertEqual(en.read_text(encoding="utf-8").count(link), 1)

    def test_slides_markdown_lists_every_image_once(self):
        session = slides.Session(
            key="wwdc2018/416",
            collection="wwdc2018",
            session_id="416",
            title="Demo",
            source_url="https://example.com/session",
            pdf_url="https://example.com/slides.pdf",
            en_path=Path("en.md"),
            zh_path=None,
        )
        text = slides.build_slides_markdown(
            session,
            [
                {"file": "page-001.webp"},
                {"file": "page-002.webp"},
            ],
        )
        self.assertEqual(text.count("page-001.webp"), 1)
        self.assertEqual(text.count("page-002.webp"), 1)


if __name__ == "__main__":
    unittest.main()
