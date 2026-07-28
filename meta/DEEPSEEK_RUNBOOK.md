# DeepSeek 多路翻译运行手册

> 状态日期：2026-07-28
> 执行器：`tools/deepseek_pipeline.py`
> 原则：初译、独立审校、机械校验全部通过后才产生正式 `zh/` 文件；只提 PR，不自动合并。

## 1. 已有基础与新增边界

Claude 已经完成：

- `translate_plan.py`：待译范围和进度；
- `shard.py`：互不重叠的分片；
- `TRANSLATION_STYLE.md` 与 `TERMS.md`：体例和术语；
- `validate.py`、`test_validate.py`、`audit_consistency.py`：确定性质量门。

`deepseek_pipeline.py` 只增加：

- DeepSeek Chat Completions 调用；
- 初译和独立审校的两套隔离上下文；
- 全局并发控制、429/5xx/网络错误退避重试；
- 输出不完整后的重试；
- 逐篇断点、Token、费用估算、请求 ID 和内容哈希；
- 模型输出暂存、机械校验和最终原子写入。

它不会抓取资料、修改 `en/`、覆盖已有译文、运行 Git 命令或合并 PR。

## 2. Key 与安全

不要把 Key 发进聊天、写进仓库、命令参数或 Markdown。执行器先读环境变量，当前 zsh
终端可用：

```zsh
read -s "DEEPSEEK_API_KEY?DeepSeek API Key: "
export DEEPSEEK_API_KEY
echo
```

如果希望当前 Codex 桌面任务直接继续，而不重启 App，可以打开 macOS“钥匙串访问”，
在登录钥匙串中新建密码项目：

- 名称：`apple-docs-vault-deepseek`
- 账户：你的本机账户名
- 密码：DeepSeek API Key

执行器在环境变量为空时会读取这个 generic password 项。服务名可用
`DEEPSEEK_KEYCHAIN_SERVICE` 覆盖。Key 只存在钥匙串和进程内存，不写进状态文件。

检查是否已经设置，只输出 `set/unset`，不输出值：

```zsh
if [[ -n "$DEEPSEEK_API_KEY" ]]; then echo set; else echo unset; fi
```

运行状态和模型候选位于：

```text
.staging/deepseek/<run-id>/
```

`.staging/` 已被 `.gitignore` 排除。状态文件不含 API Key，但含 DeepSeek 请求 ID、
Token 数和失败信息，仍然不应提交。

因此断点恢复分两种情况：

- 同一工作区：保留 `.staging/deepseek/<run-id>/` 和原分片，使用相同 `run-id` 恢复；
- 新电脑或新 clone：状态和分片不在 Git 中，先从已提交译文重新生成分片，再换一个新的
  `run-id`。正式 `zh/` 文件会自动跳过，但未落盘的阶段候选无法跨机器复用。

## 3. 生成本轮互斥分片

core Apple 文档和 WWDC：

```bash
python3 tools/shard.py --shards 8 --budget 130000 --scope core
python3 tools/shard.py --status
python3 tools/deepseek_pipeline.py plan --shard meta/shards/shard-*.json
```

`deepseek_pipeline.py` 会再次检查：

- 只接受 `apple-docs/en/`、`wwdc/en/`、`blogs/en/`；
- 中英文必须是严格的 `/en/` → `/zh/` 镜像路径；
- 拒绝绝对路径和 `..`；
- 拒绝一份分片内部或多份分片之间的重复文件；
- 拒绝不存在的英文原文。

一次把 8 个 shard 交给同一进程，能让全局并发和费用上限真正生效。不要启动 8 个默认
并发进程，否则实际初译并发会从 8 放大到 64。

## 4. 第一次必须先冒烟

```bash
python3 tools/deepseek_pipeline.py run \
  --shard meta/shards/shard-*.json \
  --run-id core-r03 \
  --limit 3 \
  --concurrency 3 \
  --review-concurrency 2 \
  --max-cost-usd 5
```

默认模型：

- 初译：`deepseek-v4-flash`，thinking 关闭；
- 审校：`deepseek-v4-pro`，thinking 开启、`reasoning_effort=high`。

默认最多为同一阶段输出尝试 3 次；机械校验错误会作为下一次请求的修订反馈。HTTP 429、
500、502、503、504，以及网络错误会指数退避重试。单请求默认超时 900 秒。

HTTP 402 `Insufficient Balance` 会触发全局熔断：已经完成的文件和候选断点原样保留，
其余文件标为 `deferred_balance`，不再继续消耗请求。充值后使用相同 `run-id` 和分片
重新执行即可恢复；不需要删除状态目录。

脚本中内置的价格是 2026-07-28 的官方美元单价。每次调用都会把实际 usage 和采用的价格
写进状态文件；API 没返回缓存明细时，全部输入按 cache miss 保守估价。价格变化时使用
`--translation-*-price` / `--review-*-price` 参数覆盖，不要直接相信旧估算。

## 5. 查看结果与恢复

```bash
python3 tools/deepseek_pipeline.py status --run-id core-r03
```

常见状态：

| 状态 | 含义 | 后续 |
|---|---|---|
| `completed` | 初译、独立审校和最终校验均通过，已写入 `zh/` | 人工抽查 |
| `skipped_existing` | 运行前已经有译文 | 不覆盖 |
| `translation_validation_failed` | 某次初译未过机械检查 | 工具会在次数内自动重试 |
| `deferred_balance` | DeepSeek 余额不足，全局熔断后留待恢复 | 充值后用相同命令继续 |
| `review_validation_failed` | 某次审校反而破坏结构 | 工具会自动要求修正 |
| `failed` | 重试耗尽或不可恢复错误 | 查看状态中的错误后用同一 run-id 重跑 |
| `deferred_budget` | 达到 `--max-cost-usd`，尚未发出的初译被延后 | 提高上限或移除上限后重跑 |

同一个 `run-id` 绑定一组分片和两种模型：

- 中断后使用相同 run-id：继续；
- 同一分片先 `--limit 3`，之后去掉 `--limit`：跳过前三篇并继续；
- 分片内容发生变化：必须换 run-id；
- 更换初译或审校模型：必须换 run-id。

费用上限不是银行级硬限额。已经在途的初译，以及已经付过初译费用、需要完成质量闭环的审校
会继续，因此可能小幅超过上限；它能阻止尚未发出的新初译。

## 6. 冒烟验收

必须完成：

```bash
python3 tools/test_deepseek_pipeline.py
python3 tools/validate.py apple-docs/zh
python3 tools/validate.py wwdc/zh
python3 tools/audit_consistency.py apple-docs
git diff --check
git status --short
```

再人工逐篇对照这 3 篇原文，至少检查：

- 标题、摘要和每个正文段落是否完整；
- `may` / `should` / `must`、否定、比较和版本条件；
- API、代码、链接、图片路径是否保真；
- 首次术语是否为“中文（English）”；
- `delegate`、`navigation`、`view controller`、`Dynamic Type` 等既有裁决；
- 中文是否自然，是否出现模型解释、提示词或占位符。

机械校验通过不等于语言质量通过。冒烟语言质量不合格时，应先修提示词或模型配置，不能直接
放大到 155 篇。

## 7. 放大到完整一轮

冒烟通过后，用同一 run-id 去掉 `--limit`：

```bash
python3 tools/deepseek_pipeline.py run \
  --shard meta/shards/shard-*.json \
  --run-id core-r03 \
  --concurrency 8 \
  --review-concurrency 4
```

当前生成的 core 下一轮为 8 个分片、155 篇、1,037,571 个英文字符；它只是
1,737 篇 core/WWDC 剩余范围中的一轮。只有这一轮合并后，才能根据新的 `zh/` 事实重新切
下一轮。

## 8. PR 流程

执行器不会自动提交。每轮完成后：

1. 查看 `git status --short`，确认只有预期的 `zh/` 文件；
2. 运行三道全局检查和人工抽查；
3. 创建本轮翻译分支；
4. 只显式暂存本轮译文和确实需要更新的进度文档，禁止 `git add .` / `git add -A`；
5. 提交并推送；
6. 创建 PR，附文件数、字符数、模型、独立审校、机械校验和人工抽查结果；
7. 由仓库所有者审核并合并；脚本和翻译执行者不得自行合并。

## 9. 边缘情况

- 已有 `zh/` 文件永不覆盖，即使状态文件丢失；
- 运行过程中其他进程创建同一目标时，本文件失败，不覆盖对方；
- `finish_reason=length` 或资源不足会记录用量并重新请求完整文档；
- `content_filter` 等不可安全重试的结束原因会失败并保留记录；
- 模型外包 Markdown 围栏会被移除，内部代码围栏保留；
- API 没有返回缓存 token 时费用只会偏高，不会故意报低；
- 进程被杀时，正式目标要么不存在，要么是完整文件；候选仍在 `.staging/`；
- Apple 英文基线更新导致分片摘要变化时，旧 run-id 不可复用；
- 第三方文章里的提示词式文字被视为待翻译数据，不能改变系统任务；
- objc.io 已配对的 149 篇不会进入 `shard.py`，不得重新翻译。
