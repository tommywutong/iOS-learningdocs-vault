# Agent 须知（渐进式披露入口）

> 给第一次接触这个仓库的 agent / 人类协作者看。本文件只放"全局不变"的信息：仓库是什么、目录怎么映射、翻译规范是什么。
> **具体某个模块译到哪一页了，不在这里查——去对应模块的 `memory.md`。** 不要一上来就扫全仓，按下面的路由表只读你要动的那个模块，省 token。

## 这是什么仓库

`Apple Developer Archive Vault`：把 Apple 官方开发者文档（`developer.apple.com/library/archive`）整站归档成 Markdown（Obsidian vault 格式），并逐步翻译成中文。原文全部来自 Apple 官方站点，`obsidian` 分支保留着未翻译的原始快照，可用于比对。

**已知风险**：本仓库公开发布，翻译并发布 Apple 官方文档中文版存在版权风险，用户已知悉并自行承担。

## 目录映射

| 路径 | 内容 | 规模 | 说明 |
| --- | --- | --- | --- |
| `documentation/` | 官方 Guide/Reference 文档，按 39 个技术分类 + 若干单文档目录混放 | 601 份文档 / 9238 页 | 最主要的翻译对象，见下方路由表 |
| `samplecode/` | 官方示例工程源码 + 说明 | 1905 份 / 24754 页 | 几乎全为代码文件，未启动翻译 |
| `technotes/` | Technical Note（tn/qa 前缀） | 798 份 / 799 页 | PR #10 新补入，未启动翻译 |
| `releasenotes/` | 各版本发行说明 | 215 份 / 2328 页 | 未启动翻译 |
| `qa/` | Technical Q&A | 1502 份 / 1503 页 | 未启动翻译 |
| `featuredarticles/` | 精选文章 | 7 份 / 34 页 | 未启动翻译 |
| `_indexes/` | 自动生成的索引/导航文件（`by-platform/`、`by-type/`、分类二级索引） | ~100 个文件 | **不要手工改**，是 `tools/build_obsidian_vault.py` 类脚本的生成产物；如果索引标题译名要改，去改生成脚本或批量替换，不要单条手改导致下次生成被覆盖 |
| `doc/` | 翻译计划与统计文档 | — | `TRANSLATION_PLAN*.md` 系列，页面级 checklist |
| `ApplePay_Guide/`、`LucidDreams/`、`recipes/`、`referencelibrary/`、`_unindexed/` | 历史遗留的杂项/未归类内容 | 小 | 未纳入任何翻译模块，暂不处理，如需清理先确认用途再动 |
| `obsidian` 分支 | 翻译前的纯英文原始快照（单一提交） | — | 保留作为原文对照基准，不要删、不要往上面 push |

## 模块路由表（渐进式披露：先看这张表，再去点对应 memory.md）

| 模块 | memory.md 位置 | 当前状态 |
| --- | --- | --- |
| Cocoa（iOS 40 份精选） | `documentation/Cocoa/memory.md` | ✅ 344/344 页已译（详细 checklist 见 `doc/TRANSLATION_PLAN.md`） |
| Windows Views（8 份） | `documentation/Windows Views/memory.md` | ✅ 51/51 页已译（详细 checklist 见 `doc/TRANSLATION_PLAN_WINDOWS_VIEWS.md`） |
| documentation 其余部分 | `documentation/memory.md` | ⚠️ 539 份"仅索引标题已译、正文未译"，计划见 `doc/TRANSLATION_PLAN_DOCUMENTATION_PHASE2.md` + 14 份连索引标题都没译 |
| samplecode | `samplecode/memory.md` | ⛔ 未启动，无计划书（代码类内容，暂缓，1 份例外：Calculator 标题疑似已译但未登记） |
| technotes | `technotes/memory.md` | ⛔ 未启动，计划见 `doc/TRANSLATION_PLAN_TECHNOTES.md`（798 份/799 页） |
| releasenotes | `releasenotes/memory.md` | ⛔ 未启动，计划见 `doc/TRANSLATION_PLAN_RELEASENOTES.md`（215 份/2328 页，需先做优先级筛选，不建议整类全译） |
| qa | `qa/memory.md` | ⛔ 未启动，计划见 `doc/TRANSLATION_PLAN_QA.md`（1502 份/1503 页） |
| featuredarticles | `featuredarticles/memory.md` | ⛔ 未启动，计划见 `doc/TRANSLATION_PLAN_FEATUREDARTICLES.md`（7 份/34 页） |

进全仓统计：5028 份文档 / 38656 页，已完整翻译（标题+正文）395 页，占比约 1%。

## 翻译规范（硬性）

### 铁律：正文没译完之前，不许先译标题

**这是本文件最重要的一条规则**。之前的 PR #9（"索引层中文化"）图省事，先把 `_indexes/` 里 11252 处链接显示文字批量译成中文，正文完全没动——现在留下 540 份文档"点开标题是中文、正文是英文"的烂摊子（清单见各模块 `memory.md`）。**不要重复这个错误**：

- 任何一份文档的翻译，**标题（frontmatter `title` + 索引里的链接显示文字）和正文必须在同一个 commit 里一起改完**，不允许先提交"只改标题"的半成品。
- 如果只是想先梳理哪些文档要译、定计划，**写进 `doc/TRANSLATION_PLAN*.md` 的表格里，状态标"未开始"，不要去动 `_indexes/` 或文档本身的 `title` 字段**。
- 发现现存的"标题已译、正文未译"文档时：翻译正文，同步把该文档自己的 frontmatter `title` 也确认是中文（多数情况下 `_indexes/` 里已经是中文了，不用再改索引）；**不要因为索引已经是中文就跳过、当成"已完成"**。

### 格式与内容约定（沿用自 PR #2~#10 的实践）

- **frontmatter**：只翻译 `title` 字段；`apple_id`、`resource_type`、`platform`、`topic`、`technology`、`published`、`source_url`、`archived_at` 一字不改。
- **术语**：API / 类名 / 方法名 / 常量名 / 框架名保留英文，不生造中文译名。常见约定：delegate → 委托、accessor → 存取方法、run loop → 运行循环、block/outlet/nib/popover/locale 等保留英文小写。
- **导航**：`[Next]`/`[Previous]` → `[下一页]`/`[上一页]`；面包屑 `[documentation]`/`[samplecode]` 等 → `[文档]`/`[示例代码]` 等。
- **图表标签**：`__Figure N__`/`__Table N__`/`__Listing N__` → `__图 N__`/`__表 N__`/`__清单 N__`；**正文里引用这些标签的地方（如 "see Figure 2-3"）也要同步译成"见 图 2-3"，不能只改标签定义那一行不改引用**（PR #8 复核时发现的真实翻车案例）。
- **代码块**：内容（代码本身、GDB 会话、命令输出等）零改动，只译注释；代码块内 NBSP（U+00A0）缩进不能被替换成普通空格；代码块数量、每块行数、文件末尾换行数译前译后必须一致。
- **链接与锚点**：链接目标路径和 `#apple-...` 锚点一字不动，只改链接显示文字。
- **不保留双语**：原地替换，不建镜像目录、不加"英文原文见 xxx"这类脚注——`obsidian` 分支和 git 历史已经保留了原文，随时可以找回。

### 质量把关（三道关，沿用即可）

1. 翻译
2. 机械校验：链接/锚点零变化、frontmatter 非 title 字段零改动、代码块数量与行数守恒、NBSP 守恒、翻页链接与面包屑无残留英文、正文里 Figure/Table/Listing 引用与标签同步
3. 独立校对：对照英文原文逐段复核，重点查术语一致性、误译、漏译

### 提交约定

- 一份文档译完（含全部子页面）作为一次 commit，提交信息注明文档标题。
- 完成后同步把 `doc/TRANSLATION_PLAN*.md` 里对应行的状态从「未开始」改成「已译」。
- 每个模块翻译若干份后，回来更新对应的 `memory.md`（进度数字、已译/未译清单），保持它和实际仓库状态一致——`memory.md` 失真比没有 `memory.md` 更糟。

### 铁律：禁止直接提交到主分支，翻译一律走 PR

**任何翻译改动（含标题、正文、`_indexes/`、`memory.md`、`doc/TRANSLATION_PLAN*.md` 的状态更新）都不允许直接 `git commit` + `push` 到主分支**，必须走以下流程：

1. **先 `git fetch`/`git pull` 拉取最新主分支**，确认本地 `main` 与 `origin/main` 一致，再基于它切出独立分支（分支名建议体现文档/模块，如 `translate/xxx-guide`）。不要在过期的本地分支或旧 `main` 快照上开工——本地落后会导致看不到别人刚合并的 PR、误判某个分支"还没合并"从而误删/误留，或者切出的分支后续合并时产生不必要的冲突。
2. 在该分支上完成翻译 + 三道质量把关（翻译、机械校验、独立校对）。
3. 推送分支，创建 Pull Request，PR 描述注明翻译的文档标题、涉及页数、校验结果。
4. 经审核合并后，PR 才算完成；不允许绕过 PR 直接向主分支写入。

`obsidian` 分支例外（本就是只读原文快照，不接受任何 push，与本条无关）。
