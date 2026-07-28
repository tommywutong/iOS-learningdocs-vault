# 后续计划与进度表

> 基线日期：2026-07-28
> 适用范围：用户已确认的 A 方案（core + 全部第三方英文博客）
> 事实来源：译文是否存在以 `zh/` 文件为准；分片 JSON 只是可重建的派生状态。

## 1. 当前里程碑

| 阶段 | 工作 | 状态 | 验收条件 |
|---|---|---|---|
| P0 | Apple 现行文档全量归档 | 已完成 | 95,634 页可在本地索引访问 |
| P0 | WWDC 精选逐字稿归档 | 已完成 | 178 场 |
| P0 | 第三方博客与学习计划快照归档 | 已完成主体 | 站点归档完成；快照 86 / 108 |
| P0 | Apple / Swift 开源仓库归档 | 已完成 | 25 个仓库及溯源信息在库 |
| P0 | 旧归档缺口补齐 | 已合并主体 | PR #10 合并，950 / 1,098 |
| P1 | 恢复 Claude 中断前的 36 篇译文 | 已完成机械验收 | Apple 译文 441 / 441 机械校验通过 |
| P1 | 独立语言审校这 36 篇 | 待办 | 另一 AI 对照原文复核并记录问题 |
| P2 | core Apple 文档 + WWDC | 进行中、等待 API 充值 | DeepSeek 新增 218 篇；剩余 1,519 篇全部通过三道质量关 |
| P3 | 第三方英文博客 | 待办 | 剩余 2,053 篇全部通过三道质量关 |
| P4 | 全仓一致性、索引与最终报告 | 待办 | 校验、索引、数字、版权边界全部对账 |

## 2. 推荐执行顺序

### P1：先给当前成果补独立审校

范围是本次恢复的 36 篇。不要因为机械校验全绿就跳过。

审校者逐篇检查：

- 标题和摘要是否忠实；
- 专有名词是否符合 `TERMS.md`；
- “may / should / must”、否定词、比较关系和版本条件是否丢失；
- API、类型名、方法名、命令、代码、路径是否被误译；
- 链接文字是否自然，链接目标是否保持；
- 是否存在看似中文但语义不完整的段落。

审校修改后重新运行：

```bash
python3 tools/validate.py apple-docs/zh
python3 tools/audit_consistency.py
```

### P2：完成 core

当前剩余 1,519 篇、9,204,757 字符。在**当前这台 Mac 的工作区**中，64 个互不重叠
分片已经生成，并绑定到 `core-r04-all`；**本机完成前不要重新运行 `shard.py` 覆盖这些
分片**。

```bash
python3 tools/deepseek_pipeline.py plan --shard meta/shards/shard-*.json
python3 tools/deepseek_pipeline.py status --run-id core-r04-all
```

充值后直接恢复：

python3 tools/deepseek_pipeline.py run \
  --shard meta/shards/shard-*.json \
  --run-id core-r04-all \
  --concurrency 64 \
  --review-concurrency 32 \
  --retries 8 \
  --max-cost-usd 100
```

恢复时会跳过 63 篇已完成译文，并复用仍然有效的阶段候选。HTTP 402
`Insufficient Balance` 会触发全局熔断；这不是限流，必须先充值。基于已完成批次的真实
消耗，建议余额至少补到 **20 美元**，为 Pro 审校和失败重试留余量；这是运行估算，不是
DeepSeek 的计费承诺。

如果是在朋友的电脑或全新 clone 中接手，不能复用本机的精确断点：`.staging/` 和
`meta/shards/` 包含请求状态与派生任务清单，按安全规则不会提交 Git。应先检出 PR #17
的分支，再重新生成只包含剩余文件的分片，并使用新的 `run-id`：

```bash
git fetch origin
git switch --track origin/translate/deepseek-core-checkpoint
python3 tools/shard.py --shards 64 --scope core
python3 tools/deepseek_pipeline.py run \
  --shard meta/shards/shard-*.json \
  --run-id core-r05-remote \
  --concurrency 64 \
  --review-concurrency 32
```

新 clone 无法复用尚未落盘的模型候选，但 PR #17 中已经完成的 218 篇会因目标文件存在而
自动跳过，不会重译。

后续仍按以下质量流水线执行：

1. 初译使用 DeepSeek Flash，独立审校使用新的 DeepSeek Pro 请求；
2. 候选只写入 `.staging/deepseek/`，不得改英文原文、术语表或已有译文；
3. 初译与审校输出各自通过 `validate.py` 的底层 `check_pair` 后才写入 `zh/`；
4. 运行目标目录的 `validate.py` 和 `audit_consistency.py`；
5. 人工抽查并只把合格译文提交 PR，不得由脚本自动合并；
6. Flash 连续失败的少量文件改用 Pro 兜底，不降低机械校验标准。

Key 不得进入仓库。完整说明见
[`DEEPSEEK_RUNBOOK.md`](DEEPSEEK_RUNBOOK.md)。

优先级：

1. Foundation / Objective-C / Swift 内存与并发；
2. Dispatch / Operation / RunLoop / UIKit 响应链；
3. QuartzCore / Core Animation / 性能；
4. Xcode / Mach-O / 启动 / 调试；
5. WWDC。

### P3：翻译第三方英文博客

当前剩余 2,053 篇、22,404,127 字符，已经排除 objc.io 的 149 篇。

博客不要按整个来源聚成巨型分片。`mikeash` 等单一来源可能达到数百万字符，应保持
“一篇一组、按字符预算装箱”的现有策略。

建议优先：

1. mikeash；
2. belkadan；
3. cocoawithlove；
4. sealiesoftware；
5. maskray；
6. 其他与学习计划直接相关的文章；
7. 与 iOS 底层关系较弱的内容最后处理。

每篇必须保留 `source_url`、作者信息和原文链接。仓库私有并不产生再分发权，不得据此移除
版权说明。

### P4：收尾

所有目标完成后执行：

```bash
python3 tools/validate.py apple-docs/zh
python3 tools/validate.py wwdc/zh
python3 tools/validate.py blogs/zh
python3 tools/test_validate.py
python3 tools/test_deepseek_pipeline.py
python3 tools/audit_consistency.py
python3 tools/indexes.py
python3 tools/studyplan.py
git diff --check
```

然后核对：

- README 数字与磁盘实测一致；
- `translate_plan.py status` 与 `zh/` 文件数一致；
- 所有索引链接存在；
- 不存在 `.cache/`、`.staging/`、分片 JSON、备份文件或密钥进入 Git；
- 远端仍为私有；
- 当前分支与 `origin/main` 一致。

## 3. Token 预算与可选策略

### 完整 A 方案

剩余 31,608,884 个源文件字符。考虑初译、中文输出、独立审校、重读原文、失败重试和公共
上下文，预计总消耗约 **3,000 万到 6,000 万 Token**。这是数量级估算，不是计费承诺。

### 节省 Token 的三个挡位

| 挡位 | 范围 | 预计影响 |
|---|---|---|
| 按需阅读 | 每次只翻译当前学习日真正要读的 10–20 篇 | 最省 Token，整体完成时间最长 |
| core 优先 | 只先做 P2，博客随读随译 | 保住学习主线，约比完整 A 少三分之二源字符 |
| 完整 A | P2 + P3 全部执行 | 覆盖最完整，Token 与审校成本最高 |

用户当前选择仍记录为“完整 A”。如果未来用户改变预算，应更新本表，不要从旧会话猜测。

### 控制消耗的规则

- 每个新会话只读项目状态、计划、术语表、自己的分片和相邻少量译文；
- 不把 7.3 MB 历史会话放进提示词；
- 不让多个 AI 领取同一文件；
- 机械检查交给脚本，不让模型反复数链接和代码行；
- 分片失败时保留已经通过校验的文件，只重做失败文件；
- DeepSeek 运行必须复用同一个 `run-id` 才能读到断点和费用记录；
- 每轮提交后再切下一轮，避免分片清单过时。

## 4. 每轮记录模板

完成一轮后在本表底部追加一行：

| 日期 | 轮次 | 范围 | 分片数 | 新增译文 | 字符数 | 独立审校 | 机械校验 | 提交 |
|---|---|---|---:|---:|---:|---|---|---|
| 2026-07-27 | 恢复批次 | Foundation / Swift / UIKit / Xcode | — | 36 | 约 133K 文件字节 | 待补 | 441 / 441 通过 | `9ee8b4b4e` |
| 2026-07-28 | core round 1–2 | Foundation / Swift / SwiftUI / UIKit / Xcode | 15 PR | 319 | 1,790,900 源字符 | 通过并修订 | 760 / 760 通过 | PR #2–#16 |
| 2026-07-28 | `core-r03` | Apple / WWDC | 8 | 155 | 1,037,571 源字符 | DeepSeek Pro 通过；人工抽查 3 篇 | Apple 912 / 912；WWDC 26 / 26 | PR #17 |
| 2026-07-28 | `core-r04-all` 部分 | Apple / WWDC | 64 | 63 | 378,805 源字符 | DeepSeek Pro 通过 | Apple 967 / 967；WWDC 34 / 34 | 余额不足暂停；PR #17 |

“独立审校”只能填写“通过”“部分”或“待补”，不得用机械校验结果代替。

## 5. 边缘情况

- 某些 API 集合页很短，但只要 `translate_plan.py` 判定为长文范围，就仍应保持中英文路径配对；
- Apple 文档更新后 `content_hash` 会变化，必须只重译变化文件；
- macOS 文件系统不区分大小写，Linux / GitHub 区分，路径规范必须通过 `tools/paths.py`；
- Swift 符号路径可能包含冒号或超长文件名，不得手工重命名破坏链接；
- 原生中文博客没有 `en/` 对应文件，不能拿来冲抵英文博客翻译进度；
- objc.io 149 篇通过 objccn 配对满足中文阅读需求，但不是本仓库新翻译；
- robots 禁止、原站消失和无 Wayback 快照必须保留为失败，不能臆造内容；
- 某个 agent 被中断时，先检查已经落盘的文件并运行校验，不要整批盲目重做。
