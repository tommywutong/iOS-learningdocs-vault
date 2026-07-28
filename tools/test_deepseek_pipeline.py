#!/usr/bin/env python3
"""DeepSeek 翻译执行器的离线回归测试；不会访问网络。"""
from __future__ import annotations

import json
import asyncio
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import deepseek_pipeline as pipeline_module  # noqa: E402
from deepseek_pipeline import (  # noqa: E402
    AccountBalanceError,
    Completion,
    Pipeline,
    PipelineConfig,
    PipelineError,
    RunState,
    Usage,
    flatten_shard,
    flatten_shards,
    load_api_key,
    relevant_terms,
    unwrap_markdown,
    usage_cost,
    validate_candidate,
)


class FormattingTests(unittest.TestCase):
    def test_unwrap_outer_fence_without_touching_inner_fence(self):
        wrapped = """```markdown
---
title: 示例
---

```swift
let x = 1
```
```"""
        expected = """---
title: 示例
---

```swift
let x = 1
```
"""
        self.assertEqual(unwrap_markdown(wrapped), expected)

    def test_plain_markdown_only_gets_final_newline(self):
        self.assertEqual(unwrap_markdown("---\ntitle: 示例\n---"), "---\ntitle: 示例\n---\n")

    def test_relevant_terms_selects_only_present_terms(self):
        terms = """| 英文 | 中文 | 依据 |
|---|---|---|
| delegate | 委托 | 官方 |
| run loop | 运行循环 | 旧仓库 |
| actor | Actor | 官方 |
"""
        selected = relevant_terms("Use a delegate from the run loop.", terms)
        self.assertIn("delegate | 委托", selected)
        self.assertIn("run loop | 运行循环", selected)
        self.assertNotIn("actor | Actor", selected)


class UsageTests(unittest.TestCase):
    def test_missing_cache_breakdown_is_conservatively_cache_miss(self):
        usage = Usage.from_api({"prompt_tokens": 1000, "completion_tokens": 500})
        self.assertEqual(usage.cache_hit_input_tokens, 0)
        self.assertEqual(usage.cache_miss_input_tokens, 1000)

    def test_cost_uses_cache_breakdown(self):
        usage = Usage(
            prompt_tokens=1000,
            completion_tokens=500,
            cache_hit_input_tokens=250,
            cache_miss_input_tokens=750,
        )
        cost = usage_cost(
            usage,
            {
                "cache_hit_input": 1.0,
                "cache_miss_input": 2.0,
                "output": 4.0,
            },
        )
        self.assertAlmostEqual(cost, 0.00375)

    def test_api_key_prefers_environment(self):
        with patch.dict(
            pipeline_module.os.environ,
            {"DEEPSEEK_API_KEY": "test-key"},
            clear=False,
        ):
            self.assertEqual(load_api_key(), "test-key")


class ShardTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        source = self.root / "apple-docs/en/demo/example.md"
        source.parent.mkdir(parents=True)
        source.write_text("demo", encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def write_shard(self, item):
        path = self.root / "shard.json"
        path.write_text(
            json.dumps({"groups": [{"files": [item]}]}),
            encoding="utf-8",
        )
        return path

    def test_valid_shard(self):
        shard = self.write_shard(
            {
                "en": "apple-docs/en/demo/example.md",
                "zh": "apple-docs/zh/demo/example.md",
                "chars": 4,
            }
        )
        items, digest = flatten_shard(shard, self.root)
        self.assertEqual(len(items), 1)
        self.assertEqual(len(digest), 64)

    def test_rejects_path_traversal(self):
        shard = self.write_shard(
            {
                "en": "apple-docs/en/../../secret.md",
                "zh": "apple-docs/zh/../../secret.md",
            }
        )
        with self.assertRaises(PipelineError):
            flatten_shard(shard, self.root)

    def test_rejects_wrong_target_mapping(self):
        shard = self.write_shard(
            {
                "en": "apple-docs/en/demo/example.md",
                "zh": "blogs/zh/demo/example.md",
            }
        )
        with self.assertRaises(PipelineError):
            flatten_shard(shard, self.root)

    def test_rejects_duplicate_files_across_shards(self):
        item = {
            "en": "apple-docs/en/demo/example.md",
            "zh": "apple-docs/zh/demo/example.md",
        }
        first = self.write_shard(item)
        second = self.root / "shard-2.json"
        second.write_text(
            json.dumps({"groups": [{"files": [item]}]}),
            encoding="utf-8",
        )
        with self.assertRaises(PipelineError):
            flatten_shards([first, second], self.root)


class CandidateValidationTests(unittest.TestCase):
    EN = """---
title: Demo guide
translated: false
source_url: 'https://example.com'
---

# Demo guide

Read the [guide](guide.md) before continuing with the sample application.
"""
    GOOD = """---
title: 示例指南
translated: true
source_url: 'https://example.com'
---

# 示例指南

继续使用示例 App 前，请先阅读这份[指南](guide.md)。
"""

    def test_valid_candidate_passes(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            en = root / "en.md"
            en.write_text(self.EN, encoding="utf-8")
            self.assertEqual(validate_candidate(en, self.GOOD, root / "work"), [])

    def test_changed_link_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            en = root / "en.md"
            en.write_text(self.EN, encoding="utf-8")
            bad = self.GOOD.replace("(guide.md)", "(指南.md)")
            issues = validate_candidate(en, bad, root / "work")
            self.assertTrue(any("链接目标" in issue for issue in issues))


class FakeClient:
    def __init__(self, content):
        self.content = content
        self.calls = []

    async def complete(self, **kwargs):
        self.calls.append(kwargs)
        return Completion(
            content=self.content,
            finish_reason="stop",
            usage=Usage(prompt_tokens=10, completion_tokens=5, cache_miss_input_tokens=10),
            request_id=f"fake-{len(self.calls)}",
            model=kwargs["model"],
        )


class FakeBalanceClient:
    def __init__(self):
        self.calls = 0

    async def complete(self, **kwargs):
        self.calls += 1
        raise AccountBalanceError(
            'DeepSeek HTTP 402: {"error":{"message":"Insufficient Balance"}}'
        )


class PipelineIntegrationTests(unittest.TestCase):
    def test_two_independent_calls_then_atomic_target_write(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            en = root / "apple-docs/en/demo/example.md"
            en.parent.mkdir(parents=True)
            en.write_text(CandidateValidationTests.EN, encoding="utf-8")
            run_dir = root / ".staging/deepseek/test"
            config = PipelineConfig(
                translation_model="translate-model",
                review_model="review-model",
                translation_concurrency=2,
                review_concurrency=1,
                max_output_tokens=4096,
                validation_attempts=1,
                max_cost_usd=None,
                translation_pricing={
                    "cache_hit_input": 0,
                    "cache_miss_input": 1,
                    "output": 1,
                },
                review_pricing={
                    "cache_hit_input": 0,
                    "cache_miss_input": 1,
                    "output": 1,
                },
            )
            state = RunState(
                run_dir / "state.json",
                run_id="test",
                shard_path="meta/shards/test.json",
                shard_digest="a" * 64,
                config={},
            )
            client = FakeClient(CandidateValidationTests.GOOD)
            item = {
                "en": "apple-docs/en/demo/example.md",
                "zh": "apple-docs/zh/demo/example.md",
                "chars": len(CandidateValidationTests.EN),
            }
            with patch.object(pipeline_module, "ROOT", root):
                pipeline = Pipeline(
                    client=client,
                    state=state,
                    run_dir=run_dir,
                    config=config,
                    style_text="测试规范",
                    terms_text="| 英文 | 中文 |\n| guide | 指南 |",
                )
                result = asyncio.run(pipeline.process(item))
            target = root / item["zh"]
            self.assertEqual(result, "completed")
            self.assertEqual(target.read_text(encoding="utf-8"), CandidateValidationTests.GOOD)
            self.assertEqual(len(client.calls), 2)
            self.assertEqual(client.calls[0]["model"], "translate-model")
            self.assertEqual(client.calls[1]["model"], "review-model")
            saved = json.loads((run_dir / "state.json").read_text(encoding="utf-8"))
            self.assertEqual(saved["files"][item["en"]]["status"], "completed")
            self.assertEqual(len(saved["files"][item["en"]]["calls"]), 2)
            self.assertIn("translation_candidate", saved["files"][item["en"]])
            self.assertIn("review_candidate", saved["files"][item["en"]])

            # 模拟正式目标写入后、状态确认前发生中断：删掉目标但保留已经
            # 校验过的审校候选。恢复必须零 API 调用完成原子写入。
            target.unlink()
            resumed_client = FakeClient("不应被调用")
            with patch.object(pipeline_module, "ROOT", root):
                resumed = Pipeline(
                    client=resumed_client,
                    state=state,
                    run_dir=run_dir,
                    config=config,
                    style_text="测试规范",
                    terms_text="| 英文 | 中文 |\n| guide | 指南 |",
                )
                resumed_result = asyncio.run(resumed.process(item))
            self.assertEqual(resumed_result, "completed")
            self.assertEqual(resumed_client.calls, [])
            self.assertEqual(target.read_text(encoding="utf-8"), CandidateValidationTests.GOOD)

    def test_balance_error_stops_later_requests_and_preserves_resume_state(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            items = []
            for name in ("first", "second"):
                en = root / f"apple-docs/en/demo/{name}.md"
                en.parent.mkdir(parents=True, exist_ok=True)
                en.write_text(CandidateValidationTests.EN, encoding="utf-8")
                items.append(
                    {
                        "en": f"apple-docs/en/demo/{name}.md",
                        "zh": f"apple-docs/zh/demo/{name}.md",
                        "chars": len(CandidateValidationTests.EN),
                    }
                )
            run_dir = root / ".staging/deepseek/balance"
            config = PipelineConfig(
                translation_model="translate-model",
                review_model="review-model",
                translation_concurrency=2,
                review_concurrency=1,
                max_output_tokens=4096,
                validation_attempts=1,
                max_cost_usd=None,
                translation_pricing={
                    "cache_hit_input": 0,
                    "cache_miss_input": 1,
                    "output": 1,
                },
                review_pricing={
                    "cache_hit_input": 0,
                    "cache_miss_input": 1,
                    "output": 1,
                },
            )
            state = RunState(
                run_dir / "state.json",
                run_id="balance",
                shard_path="meta/shards/test.json",
                shard_digest="b" * 64,
                config={},
            )
            client = FakeBalanceClient()
            with patch.object(pipeline_module, "ROOT", root):
                pipeline = Pipeline(
                    client=client,
                    state=state,
                    run_dir=run_dir,
                    config=config,
                    style_text="测试规范",
                    terms_text="| 英文 | 中文 |",
                )
                first = asyncio.run(pipeline.process(items[0]))
                second = asyncio.run(pipeline.process(items[1]))
            self.assertEqual((first, second), ("balance-skip", "balance-skip"))
            self.assertEqual(client.calls, 1)
            saved = json.loads((run_dir / "state.json").read_text(encoding="utf-8"))
            self.assertEqual(
                saved["files"][items[0]["en"]]["status"],
                "deferred_balance",
            )
            self.assertEqual(
                saved["files"][items[1]["en"]]["status"],
                "deferred_balance",
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
