# memory：documentation（Cocoa 40 份 + Windows Views 8 份之外的全部）

> 上级说明见 `/agent.md`（目录映射、翻译规范）。本文件只记录本模块进度。
> Cocoa 40 份精选、Windows Views 8 份已单独 100% 完成，见各自目录下的 `memory.md`，不在本文件统计范围内。

## 范围口径

`documentation/` 目录下除去已完成的 48 份（Cocoa 40 + Windows Views 8）之外的**全部**文档，包括：
- `documentation/Cocoa/` 剩余约 80 份未被列入精选名单的文档
- 39 个技术分类目录（Carbon、Darwin、Developer Tools、Legacy Technologies……）
- 若干直接躺在 `documentation/` 根目录下的单文档（如 `Accessibility Programming Guide for OS X`）

## 进度总览（核对时间：2026-07-27）

| 状态 | 文档数 | 页数 | 说明 |
| --- | --- | --- | --- |
| ✅ 已译（标题+正文） | 0 | 0 | 该做的都在 Cocoa/Windows Views 两个已完成模块里了 |
| ⚠️ **仅索引标题已译，正文未译** | 539 | 8794 | PR #9 只改了 `_indexes/` 显示文字，没碰正文，是技术债，**不算已完成** |
| ⛔ 完全未译（连索引标题都没译） | 14 | 49 | 见下方清单，大概率是 PR #10 补入的存档在 PR #9 跑索引翻译之后，没赶上那一批 |
| **合计待办** | **553** | **8843** | |

## ⚠️ 优先处理：标题已译、正文未译的 539 份

**完整清单、按 topic 分类分组、已排除 7 份体量过大/非叙述性文档，见 `doc/TRANSLATION_PLAN_DOCUMENTATION_PHASE2.md`**（该计划书统计口径为 533 份，因排除了 7 份 WebObjects/GCC Internals/自动生成 API 差异文档，共 4815 页，默认不纳入本轮翻译）。

处理这批文档时**不要只补正文就完事**——它们的索引标题已经是中文了，正文译完后要确认该文档自己的 frontmatter `title` 也同步改成中文（大部分情况下只是文档自身没跟上，`_indexes/` 那边不用再动）。

## ⛔ 完全未译的 14 份（含索引标题）

这批连索引标题都还是英文，翻译时按 `agent.md` 的铁律：**标题和正文一起译，同一个 commit**，包括对应 `_indexes/` 里的链接显示文字。

| 英文标题 | 页数 | topic | 物理路径 |
| --- | --- | --- | --- |
| Xcode Release Notes — Archive | 6 | Xcode | `documentation/Xcode/Xcode Release Notes — Archive` |
| Project Builder for Java | 10 | null | `documentation/Java/Project Builder for Java` |
| Video | 4 | null | `documentation/Cocoa/Video` |
| Search Fields | 6 | User Experience | `documentation/Cocoa/Search Fields` |
| iTunes Search API | 6 | Audio, Video, & Visual Effects | `documentation/Audio Video/iTunes Search API` |
| Interface Builder | 6 | null | `documentation/Developer Tools/Interface Builder` |
| QuickTime 7.1 Update Reference | 4 | null | `documentation/Quick Time/QuickTime 7.1 Update Reference` |
| QuickTime 6.3 + 3GPP | 1 | null | `documentation/Quick Time/QuickTime 6.3 + 3GPP.md` |
| QuickTime VR | 1 | null | `documentation/Quick Time/QuickTime VR.md` |
| QuickTime 6 | 1 | null | `documentation/Quick Time/QuickTime 6.md` |
| QuickTime 5 | 1 | null | `documentation/Quick Time/QuickTime 5.md` |
| PowerMac G4 | 1 | null | `documentation/Hardware/PowerMac G4.md` |
| iOS Manual Pages | 1 | null | `documentation/iOS Manual Pages` |
| Enterprise JavaBeans | 1 | Cross Platform | `documentation/Web Objects/Enterprise JavaBeans.md` |

## 已排除，暂不纳入（如需翻译请另行确认）

见 `doc/TRANSLATION_PLAN_DOCUMENTATION_PHASE2.md` 文末「排除清单」：WebObjects 4.0/4.5/5.0 Developer Documentation、GNU Compiler Collection (GCC) / (GCC) 4.2 Internals、Miscellaneous User Space API Reference、OS X v10.10 API Diffs，共 7 份 / 4815 页。

## 更新方式

每完成一批文档翻译，回来更新上面「进度总览」表格的数字，并从「完全未译的 14 份」清单里删掉已完成的行；「标题已译、正文未译」的进度仍以 `doc/TRANSLATION_PLAN_DOCUMENTATION_PHASE2.md` 里的状态列为准，不在本文件重复维护。
