# memory：documentation/Cocoa（iOS 40 份精选）

> 上级说明见 `/agent.md`（目录映射、翻译规范）。本文件只记录本模块进度。

## 范围口径

**注意**：`documentation/Cocoa/` 目录物理上有 120 份文档、约 1088 个页面，但本模块只覆盖其中被列入 `_indexes/by-platform/ios.md` → `Cocoa` 小节的 **40 份 / 344 页**精选文档。其余约 80 份 Cocoa 文档不在本模块范围内，归入 `documentation/memory.md`（documentation 其余部分）统一追踪。

## 进度

**344 / 344 页已译，100% 完成。** 已核实：`doc/TRANSLATION_PLAN.md` 表格里的状态与实际文件 frontmatter title 逐条比对，0 处缺文件、0 处状态与实际不符（核对时间：2026-07-27）。

详细的 40 份文档 × 344 页 checklist、每份文档的处理流程、术语约定，见 `doc/TRANSLATION_PLAN.md`。

## 完成批次

| 批次 | PR | 文档数 | 页数 |
| --- | --- | --- | --- |
| 1 | #2 | 2 | 15 |
| 2 | #3 | 2 | 38 |
| 3 | #4 | 6 | 44（含 1 份 Windows Views） |
| 4 | #5 | 4 | 40（含 2 份 Windows Views） |
| 5 | #6 | 5 | 46（含 2 份 Windows Views） |
| 6 | #7 | 4 | 44（含 1 份 Windows Views） |
| 7 | #8 | 7（含前人风格补齐） | 55（含 1 份 Windows Views）；补译遗漏的 Figure/Table/Listing 标签（35 处）后合并 |

（各批次同时也覆盖了 Windows Views 的文档，具体页数拆分见 `documentation/Windows Views/memory.md`）

## 无需处理

本模块已 100% 完成，无待办事项。如果发现某份"40 份名单"内的文档译文有质量问题（错译、术语不统一），直接修正并在 commit 里说明，不需要更新本文件的进度数字（数字仍是 344/344）。
