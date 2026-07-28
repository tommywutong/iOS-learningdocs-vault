# 贡献指南

本仓库是私有个人学习归档。贡献包括翻译、独立审校、索引维护、图片归档和抓取工具改进。
所有变更必须通过 Pull Request 提交，由仓库所有者审核后合并。

## 一、开始之前

先同步最新主分支，并创建独立分支：

```bash
git fetch origin
git switch main
git pull --ff-only origin main
git switch -c <类型>/<简短任务名>
```

按顺序阅读：

1. [`meta/PROJECT_STATUS.md`](meta/PROJECT_STATUS.md)
2. [`meta/SUMMER_TRANSLATION_PLAN.md`](meta/SUMMER_TRANSLATION_PLAN.md)
3. [`meta/NEXT_STEPS.md`](meta/NEXT_STEPS.md)
4. [`meta/TRANSLATION_STYLE.md`](meta/TRANSLATION_STYLE.md)
5. [`meta/TERMS.md`](meta/TERMS.md)

不要恢复旧的 `core-r04-all`，也不要使用 `--scope core` 擅自扩大翻译范围。

## 二、通用边界

- 只能提交 PR，不得直接向 `main` 推送或自行合并。
- 一个 PR 只处理一个明确任务；翻译批次应保持可独立审查。
- 不删除英文原文，不改变原文与译文的相对路径配对。
- 不提交 API Key、`.env`、缓存、临时视频、下载中间文件或失败日志。
- 不把仓库改为公开；第三方博客和 Apple 材料的归档授权并不等于再发布授权。
- 不使用 `git add .` 或 `git add -A`；逐项暂存本次任务涉及的文件。

## 三、翻译工作流

### 领取范围

当前优先顺序以 [`meta/SUMMER_TRANSLATION_PLAN.md`](meta/SUMMER_TRANSLATION_PLAN.md) 为准：

1. 暑期计划涉及的高价值博客；
2. 暑期计划需要的 Apple 现行文档；
3. 暑期计划需要的 WWDC；
4. 其余英文资料暂不主动翻译。

已经存在官方或高质量中文配对的资料不要重复翻译。任务范围不清楚时，先在 PR 或任务说明
中列出拟处理的相对路径。

### 翻译

- 保持标题层级、段落、列表、表格、callout 和代码块结构。
- frontmatter 除 `title` 和 `translated` 外不得修改。
- 代码、API 名称、链接目标和图片路径不得改动。
- 图片 alt 和 `<sub>` 图注需要翻译。
- 术语以 [`meta/TERMS.md`](meta/TERMS.md) 为准，并保持现有译文风格一致。

### 独立审校

初译与审校必须由两个独立上下文完成。审校者需要同时阅读英文原文和中文译文，检查：

- 技术含义、否定、条件、因果和数量关系；
- 术语一致性以及首次出现的中英文标注；
- 生硬直译、错位修饰语和残留英文；
- 代码上下文、图片说明和段落结构是否对应。

### 机械校验

对本批译文运行：

```bash
python3 tools/validate.py <本批中文目录或文件>
```

机械校验必须零问题。它只证明结构保真，不代替语言和技术审校。

新增内容后还要刷新导航：

```bash
python3 tools/studyplan.py
python3 tools/indexes.py
python3 tools/check_links.py
```

### PR 要求

PR 描述至少包含：

- 本批处理范围和逐文件清单；
- 初译执行者与独立审校执行者；
- 机械校验命令及完整结果；
- 已知疑点、未解决问题和未纳入范围的内容；
- 索引是否已刷新、导航检查是否通过。

不要为了吞吐量合并未经独立审校的译文。发现问题时继续修改当前 PR，不要另开“修复前一批”
的堆叠 PR。

## 四、导航与目录维护

`README.md` 是人工维护的读者首页，`tools/indexes.py` 不会覆盖它。

以下内容由脚本生成：

- `_indexes/articles.md`
- `_indexes/apple-docs.md`
- `_indexes/blogs.md`
- `_indexes/wwdc.md`
- `_indexes/topics.md` 与 `_indexes/topics/`
- `_indexes/translation-status.md`
- `_indexes/sources/`

不要手工编辑生成文件。需要改变字段、分类或排序时修改 `tools/indexes.py`，再重新生成。

导航验收标准：

- `python3 tools/check_links.py` 返回零失效本地链接；
- 每篇目录记录能直接打开原文和已有译文；
- 通用文章目录字段固定为：
  `中文标题｜英文标题｜作者/来源｜主题｜原文｜译文｜翻译状态`；
- 学习计划周次只出现在 `_indexes/study-plan.md`，不进入通用文章目录。

## 五、图片归档

### Apple 文档

Apple DocC 图片登记在 `meta/assets.json`，保存到 `attachments/`。英文和中文使用相同文件，
译文只翻译 alt 或图注，不改变路径。

### 第三方博客

多数博客图片目前仍是远程 URL。后续本地化工具应：

1. 按来源和文章 URL 建立稳定目录；
2. 保存原始 URL、引用文章、内容哈希、媒体类型和下载状态；
3. 内容寻址去重，不按显示文件名判断是否同图；
4. 改写英文原文和中文译文中的相同目标；
5. 检查 robots、许可和私有归档边界；
6. 对失败、热链限制和动态图片 URL 给出可恢复报告。

建议目录：

```text
attachments/blogs/<来源>/<文章URL哈希>/<文件名>
attachments/snapshots/<域名>/<文章URL哈希>/<文件名>
```

学习计划单页快照的英文原文保存在 `blogs/snapshots/<域名>/`，对应译文保存在
`blogs/snapshots-zh/<域名>/`，相对路径必须一致。运行
`python3 tools/validate.py blogs/snapshots-zh` 检查快照译文结构。

## 六、WWDC 幻灯片工程

这是一项独立的中大型工程，不与普通翻译 PR 混在一起。

### 当前事实

- 本地有 178 场 WWDC 逐字稿；
- 其中 56 场的官方页面提供 Presentation Slides PDF；
- 122 场没有官方 PDF；
- 38 场已有中文译文；
- 2026-07-28 实测 56 份官方 PDF 均可访问，合计约 421.6 MB，中位数约 4.3 MB；
- 最大单份 PDF 约 152.3 MB，已经超过 GitHub 普通 Git 的 100 MB 单文件限制；
- 视频不需要长期保存，也不得提交到 Git；
- 已完成计划相关的 Session 415、416、423；其余 53 场有官方 PDF 的 session 暂停。

### 交付目标

为每场已处理 session 建立：

```text
wwdc/slides/<collection>/<session-id>/
├── manifest.json
├── slides.md
└── page-001.webp
```

`manifest.json` 至少记录：

- session ID、collection 和标题；
- Apple session 页面 URL；
- 官方 PDF URL（如有）；
- PDF 与每张图片的 SHA-256；
- PDF 页数、成功渲染页数和生成时间；
- 来源类型：`official-pdf` 或 `video-keyframe`；
- 失败原因和重试状态。

英文与中文逐字稿都链接同一份 `slides.md`，不复制图片。

### 阶段 A：有官方 PDF 的 56 场

先以 WWDC18 Session 416 `iOS Memory Deep Dive` 做端到端样板：

1. 从页面资源区解析官方 PDF URL；
2. 下载到忽略 Git 的临时缓存；
3. 校验 HTTP 状态、媒体类型、文件大小和 SHA-256；
4. 将每页渲染为 WebP，保留文字和细线可读性；
5. 生成 `manifest.json` 与 `slides.md`；
6. 在英文和中文逐字稿的 Resources 区链接幻灯片；
7. 验证 GitHub 与 Obsidian 均可阅读；
8. 只有用户明确扩大范围时，才处理其余 53 场。

默认只把渲染后的 WebP 和 manifest 提交到 Git。官方 PDF URL 与哈希写入 manifest，原始 PDF
留在忽略 Git 的缓存，避免 PDF 与逐页图片双重占用仓库。若确需提交 PDF，必须先统计总体积、
单文件大小和 GitHub 限制，并由仓库所有者单独确认。

### 阶段 B：没有官方 PDF 的 122 场

只优先处理已翻译或暑期计划需要的高价值 session。可以临时读取官方视频提取关键帧，但：

- 视频只作为临时输入，完成后删除，绝不进入 Git；
- 使用镜头变化检测找候选帧；
- 过滤演讲者、黑屏、转场和重复幻灯片；
- 保留动画前后确有不同技术信息的页面；
- OCR 只能用于重复检测和辅助命名，不能重绘或改写 Apple 幻灯片；
- 每场必须人工抽查顺序、缺页、可读性和重复率。

该阶段不能承诺从视频自动还原出与官方 PDF 完全相同的幻灯片集。

### 工具接口建议

已实现 `tools/wwdc_slides.py`：

```bash
python3 tools/wwdc_slides.py plan
python3 tools/wwdc_slides.py fetch --session wwdc2018/416
python3 tools/wwdc_slides.py render --session wwdc2018/416
python3 tools/wwdc_slides.py status
python3 tools/wwdc_slides.py verify
```

全局 `--dry-run` 放在子命令之前；需要有意重渲染已完成场次时使用 `render --force`。脚本
可断点续跑，默认不覆盖已经通过哈希校验的结果。

WWDC18 Session 416 样板已采用 72 DPI、WebP quality 78 跑通：官方 PDF 167 页、9,575,316
字节，正式 WebP 167 张、合计 17,554,438 字节。首页、包含终端细字的中间页和末页已经
视觉抽查，普通笔记本阅读清晰。后续批量仍需先由仓库所有者审核样板 PR。

### 验收标准

- 仓库中没有 MP4、MOV、HLS 分片或临时 PDF；
- 每张图片能追溯到 Apple session 页面和确定的来源方式；
- `manifest.json` 页数与输出图片数量一致；
- `slides.md` 图片顺序正确且零坏链；
- 单张图片在普通笔记本屏幕上文字可读；
- 重跑不会重复下载、重复写入或改变未变化文件；
- `python3 tools/check_links.py` 通过；
- PR 报告新增文件数、总字节数、失败场次和人工抽查结果。

## 七、提交前检查

```bash
git status --short
git diff --check
python3 tools/test_validate.py
python3 tools/check_links.py
```

只暂存本次任务文件，检查 staged diff 后再提交和推送分支。PR 由仓库所有者审核合并。
