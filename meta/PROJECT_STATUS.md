# 项目状态与 AI 交接

> 状态日期：2026-07-28
> 历史 Claude 会话：`b6659196-95b7-4c6a-84df-44e94ea3d10d`
> 仓库：<https://github.com/Biscoffee/apple-docs-vault>（私有）

## 1. 一句话现状

**归档主体、暑期严格白名单和高价值博客补强均已完成并合入 `main`。** PR #20 已将
`summer-all-r01` 的 69 篇定向译文合入，合并提交为 `a817fcd43`。PR #22 又合入
`summer-b1-r01` 的 32 篇逐篇筛选博客，并为最早恢复的 36 篇 Claude 译文补齐独立审校，
合并提交为 `7990b6eb5`；其中 35 篇发生实质修改。旧大批次曾因 DeepSeek API 返回 402
暂停；用户现已改变范围，因此即使充值也不得恢复旧的 `core-r04-all`。

不要重新读取完整 Claude 会话来接手。它约 7.3 MB、3,479 条记录，绝大部分是抓取过程、
工具输出和已经落盘的工作。当前文件、本文和
[`NEXT_STEPS.md`](NEXT_STEPS.md) 才是事实来源。

## 2. 当前事实总账

### 2.1 现行资料仓库

| 来源 | 已归档 | 当前中文状态 |
|---|---:|---:|
| Apple 现行文档 | 95,634 页，其中成篇文章 3,746 篇 | 970 篇成篇译文；991 个中文配对文件 |
| WWDC 逐字稿 | 178 场 | 38 场译文 |
| 英文技术博客 | 2,263 篇 | 134 篇译文 |
| 原生中文博客 | 681 篇 | 原文即中文，不计入翻译进度 |
| 学习计划单篇快照 | 108 个目标，成功 86 个 | 56 中文、30 英文 |
| Apple / Swift 开源资料 | 25 个仓库 | 保持原文 |
| 图片附件 | 2,742 个，约 0.80 GB | — |

`python3 tools/translate_plan.py status` 当前统计的可翻译语料为：

| 来源 | 需译 | 已译 | 待译 | 待译字符 |
|---|---:|---:|---:|---:|
| Apple 现行文档 | 3,746 | 970 | 2,776 | 14,442,287 |
| WWDC | 178 | 38 | 140 | 3,919,613 |
| 英文博客 | 2,263 | 134 | 2,129 | 24,023,756 |
| **合计** | **6,187** | **1,142** | **5,045** | — |

这里的 1,142 只统计“英文文件旁边存在同路径中文译文”，不包含 681 篇原生中文博客。

### 2.2 用户当前选定的翻译范围：暑期定向

2026-07-28 的最新裁决取代历史 A 方案：

1. 暑期计划明确点名的高价值英文博客优先；
2. Apple 现行文档和 WWDC 只翻译暑期计划直接涉及的白名单；
3. objc.io 命中项继续使用 objccn 正式中文配对，不重译；
4. 不再追求全部 core 或全部英文博客完成。

白名单完成情况：

| 部分 | 已完成 | 英文原文字节 | 状态 |
|---|---:|---:|---|
| 高价值博客 | 41 | 666,822 | 完成 |
| Apple 现行文档 | 24 | 280,211 | 完成 |
| WWDC | 4 | 139,289 | 完成 |
| 高价值博客补强 | 32 | 486,663 | 完成 |
| **合计** | **101** | **1,572,985** | **完成** |

完整路径、批次顺序和排除规则见
[`SUMMER_TRANSLATION_PLAN.md`](SUMMER_TRANSLATION_PLAN.md)。旧 A 方案的 3,572 篇只是
历史估算，不再是当前欠账。

### 2.3 2026-07-28 暑期定向批次

`summer-all-r01` 从计划文件精确解析 69 篇白名单，先用 3 篇冒烟，再以初译 12 路、
独立审校 6 路执行。结果：

- 69 / 69 已完成，未覆盖任何既有译文，也未修改英文基线；
- DeepSeek API 共 191 次调用，输入 1,808,846 Token、输出 1,066,071 Token；
- 按状态文件记录的当时价格估算费用为 1.0022 美元；
- 全仓机械校验：Apple 991 / 991、WWDC 38 / 38、博客 102 / 102；
- 三类结构性术语一致性审计均通过，18,855 个导航本地链接全部有效；
- `.staging/`、分片、API Key 和模型原始输出均不进入 Git。

### 2.4 2026-07-28 高价值补强与早期译文补审

`summer-b1-r01` 以 16 路初译、8 路独立审校完成 32 篇博客补强：

- 88 次调用，813,298 输入 Token、470,335 输出 Token；
- 估算费用 0.4322 美元；
- 6 个连续破坏代码、frontmatter 或链接的候选被门禁拒绝；定点恢复原文结构后复用中文
  正文继续审校，没有重复支付整篇初译；
- 最终博客 134 / 134 通过机械校验。

`legacy-review-r01` 对恢复提交 `9ee8b4b4e` 中的 36 篇译文只做独立审校：

- 37 次调用，215,748 输入 Token、137,577 输出 Token；
- 估算费用 0.1579 美元；
- 35 篇发生实质修改，1 篇确认无需修改；
- 不重复初译，也没有把其他批次的审校证据套用到这 36 篇。

两项工作已经通过 PR #22 合入 `main`，合并提交为 `7990b6eb5`。合并后全仓复验结果为：

```text
Apple：991 / 991 通过
WWDC：38 / 38 通过
博客：134 / 134 通过
本地链接：18,927 / 18,927 有效
```

### 2.5 WWDC 幻灯片样板

PR #21 已将 WWDC18 Session 416《iOS Memory Deep Dive》的幻灯片样板合入 `main`，
合并提交为 `87807c427`：

- 官方源 PDF 共 167 页，渲染为 167 张 WebP；
- 图片总计 17,554,438 字节，参数为 72 dpi、WebP quality 78；
- 清单保存源 PDF 的 SHA-256：`5cf00044795358108e006c9c3f4fc9b0c08f271a6f9e449e54de2b95b15c75af`；
- 仓库没有提交 PDF、视频、播放列表或 DeepSeek 暂存数据；
- `tools/test_wwdc_slides.py` 2 / 2、`tools/wwdc_slides.py verify` 1 / 1 通过。

扫描结果共有 56 场能找到官方 PDF，目前只完成用户点名的 Session 416。其余 55 场不属于
当前翻译计划，不批量归档；另有 122 场没有官方 PDF，不从视频抽帧。仓库必须继续保持私有。

### 2.6 2026-07-28 core 合并批次

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

### 2.7 2026-07-28 DeepSeek 执行批次

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

PR #17 合并前，仓库所有者又核对了 218 个目标的状态记录：全部至少有一次初译和一次独立
审校调用，168 篇在审校阶段发生实质修改。人工抽检发现并修复了 DocC 示例代码关键字被
翻译的问题；最终 Apple 967 / 967、WWDC 34 / 34 通过机械校验。

`core-r04-all` 的旧 64 个分片覆盖原始 1,582 篇，范围明显过宽。它们以及本机
`.staging/deepseek/core-r04-all/` 只作为历史断点保留，不得继续执行。下一次必须按
[`SUMMER_TRANSLATION_PLAN.md`](SUMMER_TRANSLATION_PLAN.md) 重新生成白名单批次并使用
新的 `run-id`。

### 2.8 旧归档仓库

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

2026-07-28 的 `legacy-review-r01` 已逐篇对照英文原文补做独立审校，36 / 36 完成；
35 篇发生实质修改、1 篇无需修改。补审后重新运行全仓机械校验为零问题。

## 4. 质量边界

一篇译文只有经过以下三关，才应标记为“完全完成”：

1. 按 [`TRANSLATION_STYLE.md`](TRANSLATION_STYLE.md) 和 [`TERMS.md`](TERMS.md) 翻译；
2. 由没有参与初译的 AI 对照英文原文独立审校；
3. `tools/validate.py` 机械校验为零问题。

本轮恢复的 36 篇现已通过三关。其他历史译文仍沿用各自原会话记录的验收状态，不把本轮
补审证据扩大宣称到未列入 `legacy-review-r01` 的文件。

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
2. [`SUMMER_TRANSLATION_PLAN.md`](SUMMER_TRANSLATION_PLAN.md)；
3. [`NEXT_STEPS.md`](NEXT_STEPS.md)；
4. [`TRANSLATION_STYLE.md`](TRANSLATION_STYLE.md)；
5. [`TERMS.md`](TERMS.md)；
6. 领取到的白名单分片；
7. 对应的英文原文与已有相邻译文。

不要首先读取完整历史会话，不要全量扫描 95,634 篇 Apple 文档，也不要重新抓取已经归档的
内容。

## 7. 常用核对命令

```bash
# 总体翻译进度
python3 tools/translate_plan.py status

# DeepSeek 多路初译 + 独立审校（第一次必须 --limit 3）
python3 tools/deepseek_pipeline.py plan --shard meta/shards/shard-*.json
python3 tools/deepseek_pipeline.py status --run-id <run-id>

# 注意：不得继续 core-r04-all，也不得用 --scope core 生成新任务。
# 已完成的暑期白名单可由 --scope summer 精确复核；新增 B1 目标必须先写入计划，
# 再使用一个全新的 run-id。

# 三类译文的机械校验
python3 tools/validate.py apple-docs/zh
python3 tools/validate.py wwdc/zh
python3 tools/validate.py blogs/zh

# 校验器回归测试与术语一致性审计
python3 tools/test_validate.py
python3 tools/test_deepseek_pipeline.py
python3 tools/audit_consistency.py apple-docs
python3 tools/audit_consistency.py wwdc
python3 tools/audit_consistency.py blogs

# 刷新 README 与导航索引
python3 tools/indexes.py
```

## 8. 不要做的事

- 不要把仓库改成公开；
- 不要删除英文基线或覆盖 `en/`；
- 不要重译 objc.io 已配对的 149 篇；
- 不要恢复 `core-r04-all` 或把整个框架目录当作新范围；
- 不要把原生中文博客数量当成英文翻译完成量；
- 不要在未通过 `validate.py` 时提交译文；
- 不要把 `.cache/`、`.staging/`、`meta/shards/` 或 `*.orig` 提交；
- 不要把 DeepSeek API Key、状态文件或模型原始响应提交；
- 不要声称机械校验等同于独立语言审校；
- 不要为减少失败数而绕过 robots.txt。
