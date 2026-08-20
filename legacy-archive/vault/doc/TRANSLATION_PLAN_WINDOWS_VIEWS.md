# Windows Views 文档翻译计划

## Context

本计划是 `doc/TRANSLATION_PLAN.md`（iOS Cocoa 40 份文档翻译计划）的延续，范围、流程、约定全部仿照该计划，只换目标分类。

`Apple Developer Archive Vault`（已发布在 `XiyouMobile3G-iOS/apple-developer-archive-vault` 公开仓库，`main` 分支为标准 Markdown 可读版）的 iOS Cocoa 40 份文档正在按原计划逐份翻译。本计划把 `documentation` 下的 **Windows Views** 分类整体纳入翻译：该分类共 8 份文档、51 个页面文件，正文目前全部是英文原文。

翻译采用原地替换（不保留双语、不建镜像目录）。vault 是 git 仓库，`obsidian` 分支和历史提交完整保留英文原文，原地替换不会真的丢失原文，可随时通过 git 找回。

已知风险并经用户确认（沿用原计划）：该仓库是公开仓库，翻译并发布 Apple 官方文档的完整中文版本存在版权风险，用户已知悉并选择自行承担，继续公开发布。

## 范围口径（重要，避免走错目录）

- **"8 份文档"** = `_indexes/documentation/WindowsViews.md` 里列出的全部 8 份文档，对应 51 个页面文件（以磁盘实际文件核对过，与索引页数一致）。
- 实际要动的文档物理文件都在 `documentation/Windows Views/<文档目录>/*.md` 下（注意物理目录名是带空格的 `Windows Views`，索引文件名是不带空格的 `WindowsViews.md`）。
- 8 份名单以 `_indexes/documentation/WindowsViews.md` 当前的实际列出顺序为准（按标题字母排序生成，直接照此顺序推进，不再另行排序）。
- 其中 `Collection View Programming Guide for OS X`（3 页）是 macOS / AppKit 专属文档。因为它属于 Windows Views 分类、且体量很小，经用户确认一并纳入本计划翻译，不单独排除。
- 各文档目录下的 `attachments/` 子目录是图片等附件，只引用、不改动。

## 阶段一：翻译索引层

**范围**：`_indexes/documentation/WindowsViews.md`（该文件的文档标题目前仍是英文；`README.md`、`by-platform/*.md` 等其余索引文件在原计划阶段一已处理，如发现引用 Windows Views 文档标题的地方仍是英文，一并顺手统一）。

**翻译内容**：
- 索引文件里的文档标题链接文字（如 `[View Programming Guide for iOS](...)` → 译成中文标题，保留链接目标路径不变）
- 子页面链接文字（每份文档下面缩行列出的页面名）同样译成中文，路径不动
- 已经是中文的结构性文字（导航面包屑、"共 8 份文档"、标题行等）不用动

**产出物**：同步整理 8 份文档的**中英文标题对照表**（英文标题 ↔ 拟定中文译名 ↔ 对应物理路径），作为阶段二翻译正文时统一标题译法的依据。可直接作为提交信息或附带 Markdown 表格产出，不需要额外建独立文件。

## 阶段二：翻译 8 份文档正文（51 页）

**顺序**：严格按 `_indexes/documentation/WindowsViews.md` 当前列出的顺序（字母序），逐份文档、逐页翻译。

**每份文档的处理流程**（以文档为单位，不是以页面为单位提交）：
1. 定位该文档在 `documentation/Windows Views/<文档目录>/` 下的全部页面文件（入口页 + 子章节页 + Document Revision History / RevisionHistory / Glossary 等，按磁盘实际文件为准）。
2. 逐页把正文英文替换成中文翻译，原地写回同一文件（不新建双语版本、不新建镜像目录）。
3. **翻译时顺手检查并修复**：
   - 代码块缺失语言标注（裸 ` ``` ` 起始块，补 `objc`/`swift`/`c` 等；这批文档以 Objective-C 为主，人工确认后手动补标；注意区分代码块结束符，结束符本来就该是裸 ` ``` `，不要误改）
   - 表格错位（如缺 `| --- |` 分隔行）、残留 HTML 等格式问题，发现即修
   - 不在这个阶段引入新的结构性改动（不改文件名、不改目录结构、不动 `attachments/`），只改正文内容和代码块语言标注
4. 译名约定：代码、API/类/方法名、框架名、常量名保持英文原文；`UIKit`、`AppKit`、`Collection View`、`Scroll View`、`View Controller` 等专有名词/框架名保留英文，不生造中文译名；页面导航链接 `[Next]`/`[Previous]` 显示文字译作「下一页」/「上一页」。
5. 该文档全部页面译完后，作为一个 git 提交提交到 `main` 分支（提交信息里注明文档标题，方便按提交追溯翻译进度）。

## 验证方式

- 每份文档翻译提交后，用 grep 确认该文档内部相对链接、图片引用路径没有因为翻译误改（可用 `git diff` 提取改动行逐一比对链接目标）。
- 代码块语言标注修复后，确认该文档范围内裸 ` ``` ` 起始块数量为 0（结束符除外）。
- 阶段一索引翻译完成后，抽查 `_indexes/documentation/WindowsViews.md` 在 GitHub 网页上直接预览，确认中文标题渲染正常、链接可跳转。
- 阶段二全部 8 份文档译完后，回到 `_indexes/documentation/WindowsViews.md`，确认索引里的标题文字与阶段一确定的中文标题对照表一致。

## 关于范围的现实提醒

8 份文档共 51 页，体量比原计划（344 页）小很多，但同样要求"边译边查格式问题"，仍是逐文档推进的人工翻译工作。每次会话/每次调用完成其中若干份，按文档为单位持续推进，直到 8 份全部完成。

## 子 agent 领取任务的方式

1. 认领附录清单里**尚未开始**的某一份完整文档（不要跨文档拆页面认领，保持"一份文档一次提交"的粒度）。
2. 翻译该文档目录下列出的全部页面文件，原地替换正文为中文，同时按阶段二的要求顺手修代码块语言标注、格式问题。
3. 完成后把该文档在附录里对应的所有页面状态从「未开始」改成「已译」，提交一次 git commit（只 add 该文档目录下的文件，不要把仓库里其他无关改动卷进提交）。
4. 领取下一份「未开始」的文档，重复上述流程，直到 8 份全部变成「已译」。

下面附录里的路径都是相对 vault 根目录（即 `Apple Developer Archive Vault/` 目录）的相对路径。

## 附：8 份文档 × 51 页 分阶段任务清单

状态统一初始为「未开始」；子 agent 领取任务后应把对应行改成「进行中」，完成后改成「已译」。每份文档一张小表，按 `_indexes/documentation/WindowsViews.md` 的原始顺序排列（与阶段二执行顺序一致）。

### 1. Adopting Multitasking Enhancements on iPad

目录：`documentation/Windows Views/Adopting Multitasking Enhancements on iPad/`　共 4 页

| 页面文件 | 状态 |
|---|---|
| `index.md` | 已译 |
| `QuickStartForPictureInPicture.md` | 已译 |
| `QuickStartForSlideOverAndSplitView.md` | 已译 |
| `RevisionHistory.md` | 已译 |

### 2. Collection View Programming Guide for iOS

目录：`documentation/Windows Views/Collection View Programming Guide for iOS/`　共 8 页

| 页面文件 | 状态 |
|---|---|
| `About iOS Collection Views.md` | 已译 |
| `Collection View Basics.md` | 已译 |
| `Creating Custom Layouts.md` | 已译 |
| `Custom Layouts- A Worked Example.md` | 已译 |
| `Designing Your Data Source and Delegate.md` | 已译 |
| `Document Revision History.md` | 已译 |
| `Incorporating Gesture Support.md` | 已译 |
| `Using the Flow Layout.md` | 已译 |

### 3. Collection View Programming Guide for OS X

目录：`documentation/Windows Views/Collection View Programming Guide for OS X/`　共 3 页

| 页面文件 | 状态 |
|---|---|
| `About Collection Views.md` | 已译 |
| `Document Revision History.md` | 已译 |
| `Quick Start.md` | 已译 |

### 4. Multiple Display Programming Guide for iOS

目录：`documentation/Windows Views/Multiple Display Programming Guide for iOS/`　共 4 页

| 页面文件 | 状态 |
|---|---|
| `Document Revision History.md` | 已译 |
| `Presenting Content on an External Display.md` | 已译 |
| `Understanding Windows and Screens.md` | 已译 |
| `Using Windows to Present Content on Multiple Displays.md` | 已译 |

### 5. Scroll View Programming Guide for iOS

目录：`documentation/Windows Views/Scroll View Programming Guide for iOS/`　共 8 页

| 页面文件 | 状态 |
|---|---|
| `About Scroll View Programming.md` | 已译 |
| `Basic Zooming Using the Pinch Gestures.md` | 已译 |
| `Creating and Configuring Scroll Views.md` | 已译 |
| `Document Revision History.md` | 已译 |
| `Nesting Scroll Views.md` | 已译 |
| `Scrolling the Scroll View Content.md` | 已译 |
| `Scrolling Using Paging Mode.md` | 已译 |
| `Zooming by Tapping.md` | 已译 |

### 6. View Controller Catalog for iOS

目录：`documentation/Windows Views/View Controller Catalog for iOS/`　共 8 页

| 页面文件 | 状态 |
|---|---|
| `About View Controllers.md` | 已译 |
| `Combined View Controller Interfaces.md` | 已译 |
| `Document Revision History.md` | 已译 |
| `Navigation Controllers.md` | 已译 |
| `Page View Controllers.md` | 已译 |
| `Popovers.md` | 已译 |
| `Split View Controllers.md` | 已译 |
| `Tab Bar Controllers.md` | 已译 |

### 7. View Controller Programming Guide for iOS (Legacy)

目录：`documentation/Windows Views/View Controller Programming Guide for iOS (Legacy)/`　共 10 页

| 页面文件 | 状态 |
|---|---|
| `About View Controllers.md` | 已译 |
| `Combined View Controller Interfaces.md` | 已译 |
| `Custom View Controllers.md` | 已译 |
| `Document Revision History.md` | 已译 |
| `Glossary.md` | 已译 |
| `iPad-Specific Controllers.md` | 已译 |
| `Modal View Controllers.md` | 已译 |
| `Navigation Controllers.md` | 已译 |
| `Tab Bar Controllers.md` | 已译 |
| `View Controller Basics.md` | 已译 |

### 8. View Programming Guide for iOS

目录：`documentation/Windows Views/View Programming Guide for iOS/`　共 6 页

| 页面文件 | 状态 |
|---|---|
| `About Windows and Views.md` | 已译 |
| `Animations.md` | 已译 |
| `Document Revision History.md` | 已译 |
| `View and Window Architecture.md` | 已译 |
| `Views.md` | 已译 |
| `Windows.md` | 已译 |

（共计 8 份文档，51 个页面文件，与索引页数及磁盘实际文件核对一致。所有路径均需加上 `documentation/Windows Views/<对应目录>/` 前缀，与上方"目录"字段拼接后才是相对 vault 根目录的完整路径。）
