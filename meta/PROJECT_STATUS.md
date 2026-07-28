# 项目状态与 AI 交接

> 状态日期：2026-07-28
> 历史 Claude 会话：`b6659196-95b7-4c6a-84df-44e94ea3d10d`
> 仓库：<https://github.com/Biscoffee/apple-docs-vault>（私有）

## 1. 一句话现状

**归档主体已经完成，翻译仍只完成了一部分。** Claude 会话中断前留下的 36 篇
Apple 文档译文已恢复；随后 PR #2–#16 又新增并审校了 319 篇 core 译文。DeepSeek
流水线已真实运行并新增 218 篇译文（Apple 207、WWDC 11），每篇均经过模型初译
（默认 Flash，少量失败文件由 Pro 兜底）、独立 Pro 审校和机械校验。当前大批次因
DeepSeek API 返回 402 `Insufficient Balance` 暂停；充值后可从同一 `run-id` 继续。

不要重新读取完整 Claude 会话来接手。它约 7.3 MB、3,479 条记录，绝大部分是抓取过程、
工具输出和已经落盘的工作。当前文件、本文和
[`NEXT_STEPS.md`](NEXT_STEPS.md) 才是事实来源。

## 2. 当前事实总账

### 2.1 现行资料仓库

| 来源 | 已归档 | 当前中文状态 |
|---|---:|---:|
| Apple 现行文档 | 95,634 页，其中成篇文章 3,746 篇 | 967 篇译文 |
| WWDC 逐字稿 | 178 场 | 34 场译文 |
| 英文技术博客 | 2,263 篇 | 61 篇译文 |
| 原生中文博客 | 681 篇 | 原文即中文，不计入翻译进度 |
| 学习计划单篇快照 | 108 个目标，成功 86 个 | 56 中文、30 英文 |
| Apple / Swift 开源资料 | 25 个仓库 | 保持原文 |
| 图片附件 | 2,742 个，约 0.80 GB | — |

`python3 tools/translate_plan.py status` 当前统计的可翻译语料为：

| 来源 | 需译 | 已译 | 待译 | 待译字符 |
|---|---:|---:|---:|---:|
| Apple 现行文档 | 3,746 | 967 | 2,779 | 14,456,182 |
| WWDC | 178 | 34 | 144 | 4,058,902 |
| 英文博客 | 2,263 | 61 | 2,202 | 25,177,241 |
| **合计** | **6,187** | **1,062** | **5,125** | — |

这里的 1,062 只统计“英文文件旁边存在同路径中文译文”，不包含 681 篇原生中文博客。

### 2.2 用户已选定的翻译范围：A

历史会话最后确认的 A 方案是：

1. 翻译 `core`：与八周 iOS 底层学习计划直接相关的 Apple 框架，加全部 WWDC；
2. 翻译第三方英文博客；
3. 永久排除 objc.io 的 149 篇，因为仓库里已有 objccn 的正式中文译文，并已完成
   149 / 149 配对。

截至本文更新，A 方案剩余：

| 部分 | 待译 | 待译字符 |
|---|---:|---:|
| core Apple 文档 + WWDC | 1,519 篇 | 9,204,757 |
| 第三方英文博客（排除 objc.io 149 篇） | 2,053 篇 | 22,404,127 |
| **A 方案合计** | **3,572 篇** | **31,608,884** |

这是真正需要大量 Token 的部分。完整翻译加独立审校的数量级预计为
**3,000 万到 6,000 万 Token**，具体取决于模型、重试次数和审校深度。恢复上下文本身
不需要这个量级。

### 2.3 2026-07-28 core 合并批次

PR #2–#16 共新增 319 篇 Apple 译文，且文件互不重叠：

| 框架 | 新增译文 |
|---|---:|
| Xcode | 127 |
| Foundation | 97 |
| UIKit | 69 |
| Swift | 25 |
| SwiftUI | 1 |
| **合计** | **319** |

这些 PR 已逐个完成审校修订、分支机械校验、批准与合并。最终 `main` 重新运行：

```text
校验 760 篇译文：通过 760，有问题 0
没有发现译法不一致的结构性文字
```

校验器同时修复了 DocC `markdown` 代码围栏内 `## Topics` / `## Overview` 被误当成
页面正文标题的问题，并加入正反回归测试。不要为消除误报而翻译代码示例。

### 2.4 2026-07-28 DeepSeek 执行批次

已完成并机械复验的新增译文：

| 批次 | Apple | WWDC | 合计 | 状态 |
|---|---:|---:|---:|---|
| `core-r03` + Pro 兜底 | 152 | 3 | 155 | 完成 |
| `core-r04-all` | 55 | 8 | 63 | 余额不足前完成 |
| **合计** | **207** | **11** | **218** | 均已初译、独立审校、校验 |

当前正式目录复验结果：

```text
Apple：967 / 967 通过
WWDC：34 / 34 通过
```

`core-r04-all` 的 64 个分片覆盖原始 1,582 篇；已完成 63 篇，剩余 1,519 篇、
9,204,757 字符。状态位于 `.staging/deepseek/core-r04-all/state.json`，该目录被
Git 忽略。余额不足前实际出现的 `failed` 主要是同一批 HTTP 402，不代表内容校验失败；
充值后同一命令会重新处理这些目标。执行器现已增加 402 全局熔断，后续不会再让排队文件
批量变成普通失败。

### 2.5 旧归档仓库

旧仓库：<https://github.com/XiyouMobile3G-iOS/apple-developer-archive-vault>

补缺工作已经通过
[PR #10](https://github.com/XiyouMobile3G-iOS/apple-developer-archive-vault/pull/10)
合并到 `main`：

- 补入 950 / 1,098 份文档，覆盖率 86.5%；
- 新增 3,743 页、1,145 张插图；
- 新增完整的 `technotes` 分类；
- 旧仓库总量从 4,121 份文档增至 5,071 份；
- 剩余 148 份为抓取失败、404 或不属于 `/library/archive` 的 URL。

本仓库中的旧状态曾写着“.staging 尚未移入旧仓库”，该信息已经失效，不要据此重复搬运。

## 3. 本次恢复出的 36 篇译文

Claude 的并行翻译任务因组织禁用 Claude Code 订阅而中断。中断时工作区留下 36 个
未跟踪译文，分布如下：

恢复提交：`9ee8b4b4e`（`中文译文：恢复中断前的 36 篇 Apple 文档`）。

| 框架 | 数量 |
|---|---:|
| Foundation | 5 |
| Swift | 7 |
| UIKit | 6 |
| Xcode | 18 |
| **合计** | **36** |

恢复后执行：

```bash
python3 tools/validate.py apple-docs/zh
```

最初发现 14 个问题：9 个标题未翻译、5 个 `Navigation:` 未按固定译法处理。修复后结果：

```text
校验 441 篇译文：通过 441，有问题 0
```

这个结果能证明 frontmatter、代码、链接、图片、标题层级、列表、表格、callout 和明显残留
英文符合校验规则；它**不能证明语言自然度和技术表述已经由第二名审校者逐篇确认**。

## 4. 质量边界

一篇译文只有经过以下三关，才应标记为“完全完成”：

1. 按 [`TRANSLATION_STYLE.md`](TRANSLATION_STYLE.md) 和 [`TERMS.md`](TERMS.md) 翻译；
2. 由没有参与初译的 AI 对照英文原文独立审校；
3. `tools/validate.py` 机械校验为零问题。

本轮恢复的 36 篇已通过第 1、3 关，第 2 关待后续抽查。此前已提交的译文沿用原会话记录的
验收状态，不在本次恢复中重新宣称已经审校。

## 5. 学习计划快照

权威报告是 [`SNAPSHOT_REPORT.md`](SNAPSHOT_REPORT.md)：

- 目标 108 条；
- 成功 86 条；
- 失败 22 条；
- 其中 robots 明确禁止 17 条、网络或无可用快照 4 条、内容并非目标文章 1 条。

robots 禁止的条目不得通过更换 User-Agent、代理或其他方式绕过。需要时只能由用户在浏览器
中手动保存。

## 6. 接手时先读什么

新的 AI 按以下顺序读取即可：

1. 本文件；
2. [`NEXT_STEPS.md`](NEXT_STEPS.md)；
3. [`TRANSLATION_STYLE.md`](TRANSLATION_STYLE.md)；
4. [`TERMS.md`](TERMS.md)；
5. 领取到的 `meta/shards/shard-XX.json`；
6. 对应的英文原文与已有相邻译文。

不要首先读取完整历史会话，不要全量扫描 95,634 篇 Apple 文档，也不要重新抓取已经归档的
内容。

## 7. 常用核对命令

```bash
# 总体翻译进度
python3 tools/translate_plan.py status

# 查看当前分片完成度
python3 tools/shard.py --status

# DeepSeek 多路初译 + 独立审校（第一次必须 --limit 3）
python3 tools/deepseek_pipeline.py plan --shard meta/shards/shard-*.json
python3 tools/deepseek_pipeline.py status --run-id <run-id>

# 当前 64 个 core 分片必须保留到 core-r04-all 完成，不要重新生成
python3 tools/shard.py --status

# 充值后恢复当前全部 core 批次
python3 tools/deepseek_pipeline.py run \
  --shard meta/shards/shard-*.json \
  --run-id core-r04-all \
  --concurrency 64 \
  --review-concurrency 32 \
  --retries 8 \
  --max-cost-usd 100

# 三类译文的机械校验
python3 tools/validate.py apple-docs/zh
python3 tools/validate.py wwdc/zh
python3 tools/validate.py blogs/zh

# 校验器回归测试与术语一致性审计
python3 tools/test_validate.py
python3 tools/test_deepseek_pipeline.py
python3 tools/audit_consistency.py

# 刷新 README 与导航索引
python3 tools/indexes.py
```

## 8. 不要做的事

- 不要把仓库改成公开；
- 不要删除英文基线或覆盖 `en/`；
- 不要重译 objc.io 已配对的 149 篇；
- 不要把原生中文博客数量当成英文翻译完成量；
- 不要在未通过 `validate.py` 时提交译文；
- 不要把 `.cache/`、`.staging/`、`meta/shards/` 或 `*.orig` 提交；
- 不要把 DeepSeek API Key、状态文件或模型原始响应提交；
- 不要声称机械校验等同于独立语言审校；
- 不要为减少失败数而绕过 robots.txt。
