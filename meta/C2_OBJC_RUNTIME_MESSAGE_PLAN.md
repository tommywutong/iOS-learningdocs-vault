# C2：Objective-C 消息机制与运行时数据批次

> 状态日期：2026-09-04
> 范围状态：执行中
> 执行边界：ZCode 并行子代理初译 + 独立子代理审校；不调用 DeepSeek，不恢复旧 `core` 分片

## 目标

暑期定向白名单（129 篇）、强相关 B 类（407 / 407）、C1 试点（4 篇）以及
`meta/translate_batch.json` 中 7 篇 KVC / KVO / 内存主题文章均已完成。用户于
2026-09-04 指示继续翻译工作。按 [`NEXT_STEPS.md`](NEXT_STEPS.md) 的要求先建立固定清单
再继续：本批次延续 C1 之后的 Objective-C 运行时主线，聚焦「消息发送与方法查找、方法
替换、方法签名、IMP、NSInvocation、ivar 布局、快速枚举、init/dealloc 中的存取方法」
一组互相衔接的底层主题；不以目录或关键词匹配结果批量扩张。

## 固定清单（8 篇，约 80 KB）

| 英文原文 | 中文目标 | 原文字节 |
|---|---|---:|
| `blogs/en/mikeash/friday-q-a-2013-10-25-nsobject-the-class-and-the-protocol.md` | `blogs/zh/mikeash/friday-q-a-2013-10-25-nsobject-the-class-and-the-protocol.md` | 7,042 |
| `blogs/en/mikeash/friday-q-a-2009-11-27-using-accessors-in-init-and-dealloc.md` | `blogs/zh/mikeash/friday-q-a-2009-11-27-using-accessors-in-init-and-dealloc.md` | 7,451 |
| `blogs/en/mikeash/friday-q-a-2010-01-29-method-replacement-for-fun-and-profit.md` | `blogs/zh/mikeash/friday-q-a-2010-01-29-method-replacement-for-fun-and-profit.md` | 11,299 |
| `blogs/en/mikeash/friday-q-a-2011-08-05-method-signature-mismatches.md` | `blogs/zh/mikeash/friday-q-a-2011-08-05-method-signature-mismatches.md` | 14,679 |
| `blogs/en/cocoawithlove/imp-of-the-current-method-cocoa-with-love.md` | `blogs/zh/cocoawithlove/imp-of-the-current-method-cocoa-with-love.md` | 9,164 |
| `blogs/en/cocoawithlove/construct-an-nsinvocation-for-any-message-just-by-sending-cocoa-with-love.md` | `blogs/zh/cocoawithlove/construct-an-nsinvocation-for-any-message-just-by-sending-cocoa-with-love.md` | 11,053 |
| `blogs/en/cocoawithlove/dynamic-ivars-solving-a-fragile-base-class-problem-cocoa-with-love.md` | `blogs/zh/cocoawithlove/dynamic-ivars-solving-a-fragile-base-class-problem-cocoa-with-love.md` | 13,491 |
| `blogs/en/cocoawithlove/implementing-countbyenumeratingwithstate-objects-count-cocoa-with-love.md` | `blogs/zh/cocoawithlove/implementing-countbyenumeratingwithstate-objects-count-cocoa-with-love.md` | 5,927 |

每篇均已核验：英文原文完整、无现成中文配对、未命中已冻结的
`meta/summer_related_b_allowlist.json`。这些文章与已完成批次同属一条主线：KVC / KVO、
零值弱引用、`Method Swizzling` 之后，下一步自然是方法查找与消息发送的完整链路。

## 质量门

1. 按 [`TRANSLATION_STYLE.md`](TRANSLATION_STYLE.md) 与 [`TERMS.md`](TERMS.md) 初译；
   frontmatter 只改 `title` 与 `translated` 两个字段。
2. 初译与审校由不同上下文完成；审校者对照英文原文逐段复核技术含义、否定、条件、
   因果、数量关系、术语一致性与首次出现的中英文标注。
3. 每篇通过 `python3 tools/validate.py --strict-identifiers` 零问题。
4. 全批再运行 `python3 tools/test_validate.py`、`python3 tools/check_links.py`、
   `python3 tools/indexes.py` 与 `python3 tools/title_aliases.py check`。
5. 只提交合格文件的 PR，交由仓库所有者审核，不自行合并。

## 完成记录

2026-09-05 执行完成，8 / 8 篇落盘：

- 初译：由 5 个并行 ZCode 子代理上下文完成 5 篇（其中 2 个上下文在返回报告前中断，
  产物完整落盘），主会话上下文完成 3 篇；
- 独立审校：主会话上下文交叉审校子代理初译的 5 篇；另一个独立子代理上下文对照
  英文原文逐段审校主会话初译的 3 篇，结论均为通过，共提出 1 条 [中]（invocation
  译法与全文「调用」不一致）与 10 条 [低] 修订建议，已逐条采纳修复；唯一保留项是
  mikeash 页脚样板，按 `plweakcompatibility-part-ii` 既有严格审校译文原样沿用，
  未按单条建议单独改动；
- 机械校验：8 篇全部通过 `python3 tools/validate.py --strict-identifiers` 零问题
  （mikeash 目录存量 9 条、cocoawithlove 目录存量 1 条均为 `main` 上既有的历史
  问题文件，与本批无关，已在 PR 中记录）；
- `python3 tools/test_validate.py` 8/8、`python3 tools/test_segmented_markdown.py`
  通过；`python3 tools/title_aliases.py check` 2,145 条 0 错误；
  `python3 tools/indexes.py`、`python3 tools/studyplan.py` 已刷新；
  `python3 tools/check_links.py` 30,654 个本地链接全部有效；
- 术语记录：swizzle 跟随存量主流译法「调配」（22 处 vs「混写」5 处）；
  setter 按存量主流保留英文（30 处）；「续体传递风格（Continuation Passing
  Style）」「动态分发（dynamic dispatch）」为本批新增标注译法。

