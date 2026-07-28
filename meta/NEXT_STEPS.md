# 后续计划与进度表

> 基线日期：2026-07-28
> 当前范围：高价值博客优先；官方材料只做暑期学习计划白名单
> 详细白名单：[`SUMMER_TRANSLATION_PLAN.md`](SUMMER_TRANSLATION_PLAN.md)

## 1. 当前结论

PR #17 已审核并合入 `main`：

- DeepSeek 新增 218 篇译文：Apple 207、WWDC 11；
- 每篇均有初译和独立 Pro 审校调用；
- 168 篇在审校阶段发生实质修改；
- 人工复核修正了 DocC 示例中的 `## Topics` / `## Overview`；
- Apple 967 / 967、WWDC 34 / 34 机械校验通过；
- 合并提交：`09f2f8563`。

用户已经取消“完整 A 方案”。旧计划中的 1,519 篇宽泛 core 和 2,053 篇全部英文博客，
不再是当前完成目标。

暑期定向目标和逐篇筛选的 B1 补强已经完成：

| 优先级 | 内容 | 完成 | 英文原文字节 | 状态 |
|---|---|---:|---:|---|
| B0 | 暑期计划点名的高价值英文博客 | 41 | 666,822 | 完成 |
| O1 | 暑期计划点名的 Apple 现行文档 | 24 | 280,211 | 完成 |
| O2 | 暑期计划点名的 WWDC | 4 | 139,289 | 完成 |
| B1 | 逐篇筛选的高价值博客补强 | 32 | 486,663 | 完成 |
| B2 | 与 iOS 学习直接相关的英文网页快照 | 28 | 488,119 | 完成 |
| — | **合计** | **129** | **2,061,104** | **完成** |

objc.io 另有 10 篇命中暑期计划，但已有 objccn 正式中文配对，不重译。

最早恢复的 36 篇 Claude 译文也已通过 `legacy-review-r01` 补齐独立审校证据：35 篇
发生实质修改，1 篇确认无需修改。这项既存质量债已经清零。

## 2. 下一步

当前可自动执行的翻译计划没有待执行项：

1. B1 补强与 36 篇补审已通过 PR #22 合入 `main`，全仓复验通过；
2. B2 的 28 篇计划内快照已经完成，计划内 WWDC18/415、WWDC19/423 幻灯片已经归档；
3. 只有学习计划出现新的明确缺口时，才逐篇追加新目标，不恢复宽泛 `core`。

其余 53 场已经找到官方 PDF 的 WWDC 幻灯片不属于当前翻译计划，不批量归档。另有
122 场没有找到官方 PDF，不从视频抽帧。两类任务都必须由用户明确扩大范围后才能执行。

学习计划仍有 22 个单页 URL 没有原文快照：17 个受 robots 明确限制，只能由用户在浏览器
中手动保存；4 个原站网络失效且 Web Archive 无快照；1 个原网址已经变成广告页。再次检索
没有找到这些文章的作者迁移原页，不用不明转载冒充原文。准确清单见
[`SNAPSHOT_REPORT.md`](SNAPSHOT_REPORT.md)。

以下分组是本轮已经完成的范围记录，不再是待领取任务。

### B0-R1：Runtime、对象模型与内存

- Always Processing：7 篇；
- Mike Ash：Runtime、消息转发、ARC、weak、Block、Tagged Pointer 等 12 篇。

本组已完成。技术术语、源码结构和链接已通过机械门禁。

### B0-R2：并发、UIKit 与性能

- GCD、dispatch queue、锁、Operation：5 篇；
- 滚动性能、主线程 watchdog、视图控制器加载、架构：4 篇。

### B0-R3：构建、启动、集合与序列化

- Mach-O、链接、order file、App 启动：4 篇；
- NSDictionary / NSMutableArray：2 篇；
- Protobuf wire format：2 篇；
- meta-class、关联对象、KVO、Method Swizzling：4 篇。

### O1：Apple 白名单

只做 [`SUMMER_TRANSLATION_PLAN.md`](SUMMER_TRANSLATION_PLAN.md) 列出的 24 篇。
不要按 Foundation、UIKit、Swift 或 Xcode 整个目录扩展。

### O2：WWDC 白名单

只做 4 场：

1. Advancements in the Objective-C runtime；
2. Behind the Scenes of the Xcode Build Process；
3. Link fast: Improve build and launch times；
4. Optimizing App Launch。

## 3. 明确暂停的旧任务

不得继续运行：

```bash
python3 tools/shard.py --scope core
python3 tools/deepseek_pipeline.py run \
  --run-id core-r04-all \
  --shard meta/shards/shard-*.json
```

原因：旧 `core` 以框架前缀选文件，混入大量与暑期计划无关的官方页面；其中
`swift` 前缀还会误命中 `swiftui`、`swiftdata` 等目录。旧 64 个分片和
`.staging/deepseek/core-r04-all/` 可保留为历史断点，但不能继续消费 Token。

新批次必须从白名单生成，并使用新 `run-id`。在调度器支持显式 `summer` 范围前，不要用
关键词或目录前缀替代白名单。当前调度器已支持 `summer`、`summer-b1`、
`summer-snapshots` 和 `legacy-review` 四个显式范围。

## 4. 每轮质量门

1. 按 [`TRANSLATION_STYLE.md`](TRANSLATION_STYLE.md) 和 [`TERMS.md`](TERMS.md) 初译；
2. 由没有参与初译的模型/AI 对照原文独立审校；
3. 逐篇运行 `validate.py` 底层 `check_pair`；
4. 全目录运行机械校验与术语一致性审计；
5. 人工抽查标题、摘要、否定/比较/版本条件、关键术语和代码示例；
6. 只提交合格文件的 PR；
7. 执行者不得自行合并，交给用户审核。

完整检查：

```bash
python3 tools/test_deepseek_pipeline.py
python3 tools/test_validate.py
python3 tools/validate.py apple-docs/zh
python3 tools/validate.py wwdc/zh
python3 tools/validate.py blogs/zh
python3 tools/audit_consistency.py apple-docs
python3 tools/audit_consistency.py wwdc
python3 tools/audit_consistency.py blogs
git diff --check
git status --short
```

## 5. Token 与费用记录

两轮新增译文共 101 篇、1,572,985 字节英文原文，流水线实际记录：

- API 调用：279 次；
- 输入 Token：2,622,144；
- 输出 Token：1,536,406；
- 按执行时价格估算：1.4344 美元。

计划内快照另有 28 篇：88 次调用、983,717 输入 Token、635,728 输出 Token，估算
0.5212 美元。129 篇新增译文合计估算 1.9556 美元。

另有 36 篇早期译文补审：37 次调用、215,748 输入 Token、137,577 输出 Token，估算
0.1579 美元。新增译文与补审合计估算 2.1135 美元。

控制规则：

- 每轮 8–15 篇，或 120K–180K 英文字符；
- 先 `--limit 3` 冒烟，人工确认后再放大；
- 博客保持一篇一组；
- 多个执行者不能领取同一文件；
- 只重做失败文件，不重做已落盘且通过校验的文件；
- 不把历史会话或整仓资料塞进提示词；
- Key、`.staging/`、分片和模型原始响应不得提交。

## 6. 记录表

| 日期 | 轮次 | 范围 | 新增译文 | 独立审校 | 机械校验 | 提交 |
|---|---|---|---:|---|---|---|
| 2026-07-27 | 恢复批次 | Foundation / Swift / UIKit / Xcode | 36 | 后由 `legacy-review-r01` 补齐 | Apple 991 / 991 | `9ee8b4b4e` |
| 2026-07-28 | core round 1–2 | Foundation / Swift / SwiftUI / UIKit / Xcode | 319 | 通过并修订 | 当时 760 / 760 | PR #2–#16 |
| 2026-07-28 | `core-r03` + `core-r04-all` 部分 | Apple / WWDC | 218 | DeepSeek Pro + 人工复核 | Apple 967 / 967；WWDC 34 / 34 | PR #17，`09f2f8563` |
| 2026-07-28 | `summer-all-r01` | 博客 41 / Apple 24 / WWDC 4 | 69 | DeepSeek Pro 独立审校 | Apple 991 / 991；WWDC 38 / 38；博客 102 / 102 | PR #20，`a817fcd43` |
| 2026-07-28 | `summer-b1-r01` | 高价值博客补强 | 32 | DeepSeek Pro 独立审校 | 博客 134 / 134 | PR #22，`7990b6eb5` |
| 2026-07-28 | `legacy-review-r01` | 最早恢复的 Apple 译文 | 0（补审 36） | 36 / 36，35 篇修改 | Apple 991 / 991 | PR #22，`7990b6eb5` |
| 2026-07-28 | WWDC 幻灯片样板 | Session 416 / 167 张 WebP | 不适用 | 不适用 | 幻灯片 1 / 1；链接 18,927 / 18,927 | PR #21，`87807c427` |
| 2026-07-28 | `summer-snapshots-r01` | 计划内英文网页快照 | 28 | DeepSeek Pro 独立审校 | 快照 28 / 28 | PR #24 |
| 2026-07-28 | 计划内 WWDC 幻灯片 | Session 415 / 423，共 419 张 WebP | 不适用 | 不适用 | 幻灯片 3 / 3 | PR #24 |

## 7. 完成定义

129 篇已取得原文的白名单已经通过三道质量关，36 篇早期译文的独立审校质量债也已清零。
自动化范围完成；上述 22 个原文取得障碍继续明确保留，不把“无法合法自动抓取”伪装成完成。
仓库中仍有数千篇英文资料没有中文版属于预期状态，不再作为“欠账”。

新增目标必须由用户明确要求，或先写入
[`SUMMER_TRANSLATION_PLAN.md`](SUMMER_TRANSLATION_PLAN.md) 并说明其与暑期计划的对应关系。
