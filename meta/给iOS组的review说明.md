# Apple Developer Archive Vault 中文化 —— 六个 PR 的 review 说明

## 一句话

`doc/TRANSLATION_PLAN.md`（Cocoa 40 份 / 344 页）与 `doc/TRANSLATION_PLAN_WINDOWS_VIEWS.md`（Windows Views 8 份 / 51 页）里剩余的 **207 页正文全部译完**，外加索引层 documentation 分类的 11,252 处标题。两份计划表状态已归零（344/344、51/51）。

## 建议合并顺序

```
#4 → #5 → #6 → #7 → #8 → #9
```

六个分支互不冲突（已本地验证全部干净合并）。**#9 必须放最后**：索引里的中文译名取自前五个 PR 的正文译文，先合 #9 会短暂出现「索引已中文、点进去正文还是英文」（链接本身正常，只是内容没跟上）。

| PR | 内容 | 量 |
|---|---|---|
| #4 | 定时器 / 撤销架构 / Block / 动画类型与时间控制 / 流 / ObjC 运行时 / iOS 多显示屏 | 7 份 · 48 页 |
| #5 | 谓词 / 偏好与设置 / 属性列表 / Cocoa 编码规范 / iOS Scroll View / iOS 视图 | 6 份 · 44 页 |
| #6 | 资源 / 字符串 / ObjC 面向对象 / Bonjour / 高级内存管理 / Collection View / VC 一览 | 7 份 · 53 页 |
| #7 | Core Animation / ObjC 编程语言 / 用 ObjC 编程 / 多线程 / VC 编程指南（旧版） | 5 份 · 55 页 |
| #8 | Cocoa 基础指南（556 KB）+ 前人译文风格补齐 | 7 页 + 121 文件 |
| #9 | 索引层 documentation 分类中文化 | 11,252 处 · 55 文件 |

## 重点看这两个

**PR #8** —— 唯一大规模改动前人已合并成果的一个（121 个文件）：

- 前人译文里残留的 `[Next]`/`[Previous]` 改成 `[下一页]`/`[上一页]`（254 处）、`__Figure/Table/Listing N__` 改成中文（9 处）、「您」统一为「你」（33 处，改前全库「你」1602 : 「您」33）
- 13 份文档的 frontmatter `title` 与面包屑第三项此前仍是英文，已回填中文（112 页）。译名取自各文档入口页**已有的中文 H1**，没有另起译法
- 判定门槛是中文占比 30%，**未译页面一律没动**（否则会把英文页的 `[Next]` 也误改成中文）

**PR #6** —— Collection View 那一份动了前人已合并的 3 个页面，目的是消除同一文档内的分裂：那 3 页是全仓库 128 个已译页面里**仅有的**还用 `[documentation]` 面包屑的；代码注释也还是英文；图表标题分隔符用了全角空格，而原文实际是两个 NBSP。已统一，代码本体逐字符未动。

## 这些是约定，不是错漏

- **保留英文**：API / 类 / 方法 / 常量 / 框架名；`Collection View`、`Scroll View`、`View Controller`、`block`、`nib`、`outlet`、`locale`、`popover` 等惯例术语
- **页面 H1 整体就是保留术语时不强行中文化**（如 `# Split View Controller`、`# Tab Bar Controller`），并统一为单数
- **`delegate` 一律「委托」**，但设计模式 `Proxy` 译「代理」——两者在 `Cocoa Design Patterns.md` 同页出现，已确认没混淆
- **纯索引页（`Index.md`）的索引条目保留英文**，只译标题与导语，与 `Attributed String Programming Guide/Index.md` 的既有先例一致
- **索引里的标识符与类名保留英文**（`EOClassDescription`、`NSObject Additions`、`next.wo.client.Association` 等，3,271 处）
- **归档抓取时被截断的残缺标题保留英文**（`Build_and_R_Application`、`Creating_a__resentation` 等，134 处）—— 给残缺串编一个像样的中文标题等于凭空造信息

## 范围边界

- 索引层**只做了 documentation 分类**。qa（4,609 处）、samplecode（25,348 处）没动 —— 那两类正文永远是英文，且 samplecode 标题多是工程名（`AVCam-iOS`、`Reachability`）本就不该译
- 因此会看到 **204 条「索引中文 / 正文英文」**（Metal、OpenGL ES、Safari 参考这些），全部落在计划外文档，是已知取舍。**计划内 48 份文档的索引标题与 frontmatter title 逐条一致，0 条不符**

## 原始归档自带的问题（我们没改，只记录）

review 时如果看到这些，不是本次引入的：

- 大量图片行被截断成孤立的 `!` 或 `!!`
- 很多文档丢失了 Apple 原页面的二级/三级小节标题，导致页内 `#apple-...` 锚点指向不存在的标题
- `Defining a Class.md` 两个代码块被标成 ` ```swift ` 但内容是 Objective-C
- `Reading and Writing Property-List Data.md` 清单 6-1 代码缺右花括号（同段代码在另一页是对的）
- `About Threaded Programming.md`、`Key-Value Coding Extensions.md`、`Combined View Controller Interfaces.md` 各有一处交叉引用编号错位
- `Bonjour - FAQ` 的问题标题被整体剥离，只剩 13 段答案

## 质量把关方式

每份文档过两道：翻译 → **确定性脚本校验**。脚本查的是链接目标与锚点零变化、frontmatter 非 title 字段零改动、代码内 NBSP 守恒（含行内 `code`）、代码块行数守恒、文件末尾换行数一致、代码块数量一致、翻页链接无残留、疑似未译英文句。

这类硬指标是人工和自检最容易漏报的。实际捕获到的缺陷包括：`[Cocoa](url)` 链接退化成纯文本、XML 示例里 130 处 NBSP 缩进被换成普通空格、`Scanners.md` 里承载语义的 NBSP 丢失（那段正文讲的正是空格差异）、代码块注释 3 行被压成 2 行、两处面包屑漏改、一处 `outlet` 链接丢失。

PR #9 的索引回填另做了全量比对：**44,542 个 `](...)` 链接目标逐字节一致，文件行数未变**。
