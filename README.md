# Apple 文档与 iOS 底层知识归档

> 一个以中文阅读为优先的 Apple / iOS 技术资料库，收录 Apple 现行文档、WWDC 逐字稿、
> 高质量技术博客、网页快照及其中英文译文。它是阅读与翻译协作仓库，不是 Apple 官方项目。

仓库中的 Apple 和第三方材料仍受各自版权、许可和网站条款约束。请把这里当作个人学习与
研究索引，不要在没有相应授权的情况下重新分发原文、图片、视频或译文。

## 30 秒了解仓库

如果你第一次打开这里，先记住三件事：

1. **想直接读中文**：打开[阅读入口](_indexes/reader-guide.md)，再进入[中文技术博客](_indexes/chinese-blogs.md)。
2. **想系统学一个主题**：从[iOS 底层知识地图](_indexes/topics.md)或[暑期计划知识地图](_indexes/summer.md)开始。
3. **想查一篇具体资料**：使用[文章目录](_indexes/articles.md)，再按 Apple 文档、WWDC 或博客来源筛选。

仓库内容可以按四类理解：

| 内容 | 适合什么场景 | 入口 |
|---|---|---|
| Apple 现行文档 | 查 API、框架概念和官方指南 | [Apple 文档索引](_indexes/apple-docs.md) |
| WWDC 逐字稿 | 按 session 学习系统机制和工程实践 | [WWDC 索引](_indexes/wwdc.md) |
| 技术博客与网页快照 | 补充 Runtime、内存、并发、性能等深度文章 | [博客索引](_indexes/blogs.md) |
| 学习计划与旧版归档 | 按路线学习，或查找已下线的 Apple 资料 | [暑期计划](_indexes/summer.md) · [旧版归档](legacy-archive/vault/README.md) |

## 推荐入口

| 我想做什么 | 入口 |
|---|---|
| 不知道从哪里开始 | [阅读入口](_indexes/reader-guide.md) |
| 优先阅读已有中文正文的技术博客 | [可直接中文阅读](_indexes/chinese-blogs.md) |
| 按 Runtime、内存、并发等知识点浏览 | [iOS 底层知识地图](_indexes/topics.md) |
| 按中文目录标题查找其他英文文章 | [技术博客索引](_indexes/blogs.md) |
| 查找 Apple 文档、WWDC 或全部资料 | [文章目录](_indexes/articles.md) |
| 查看哪些已经翻译 | [翻译状态](_indexes/translation-status.md) |
| 按暑期计划学习 | [暑期计划知识地图](_indexes/summer.md) |
| 按 Apple 框架浏览 | [Apple 文档索引](_indexes/apple-docs.md) |
| 阅读旧版 Apple 资料 | [完整旧版归档](legacy-archive/vault/README.md) |
| 按主题浏览 WWDC | [WWDC 索引](_indexes/wwdc.md) |
| 参与翻译或继续工程任务 | [贡献指南](CONTRIBUTING.md) |

在 Obsidian 中使用时，直接把仓库根目录作为 Vault 打开。GitHub 上的所有导航也使用普通
Markdown 相对链接，不依赖 Obsidian 专属语法。

## 怎样找到一篇资料

最省事的入口是[阅读入口](_indexes/reader-guide.md)：它先展示有完整中文正文的文章，再展示
只有中文目录标题、正文仍为英文的文章。分页、标签、归档和站点首页等误抓页面仍保留在原始
归档中，但不会混入读者目录。

目录记录会明确区分以下状态：

- **中文正文**：仓库中有可直接阅读的中文内容；
- **原生中文**：来源本身就是中文，不计入翻译完成数；
- **仅标题中文，正文待翻译**：只翻译了目录标题，正文链接仍指向英文原文；
- **未翻译**：只有英文原文，尚未建立中文配对。

英文原文与中文译文通常保持相同相对路径，只把 `en/` 替换为 `zh/`。文章目录已经提供原文
和译文入口，不需要手工猜路径。

### 按文章标题

[文章目录](_indexes/articles.md) 将资料按 Apple 文档、WWDC、技术博客分流到逐篇目录。
每篇记录都显示：

```text
中文标题｜英文标题｜作者/来源｜主题｜原文｜译文｜翻译状态
```

“仅标题中文，正文待翻译”表示只翻译了目录标题，点击后仍是英文正文；它不会计入译文完成数。
API、类型名、编译参数和产品名可能保持英文，避免为了出现汉字而误译专有名称。

“学习计划模块”只存在于独立的学习计划索引中，不属于通用文章元数据。

### 按主题

[主题目录](_indexes/topics.md) 提供 Objective-C Runtime、内存与 ARC、Block、RunLoop、
并发、性能、启动与链接、UI 渲染、网络安全等入口。同一篇文章可能属于多个主题；
进入主题后再按子主题或“全部资料”浏览。

主题由文章标题、Apple 框架和 WWDC 人工分组生成，适合围绕一个知识点完整浏览。

### 按暑期计划

[暑期计划知识地图](_indexes/summer.md) 按本地 Obsidian 计划的九个模块组织资料。
每个模块页保留原计划的学习步骤和指定材料，再补充全库相关文章；中文正文优先，
其后是未翻译资料，计划直接点名的材料和 Apple/WWDC 官方资料会排在前面。
若只想看计划原始模块和外链，可进入[材料索引](_indexes/study-plan.md)。

### 按来源

- Apple 文档：先选框架，再进入“逐篇查看”。
- WWDC：可以按九个技术分组浏览，也可以打开文章级总目录。
- 技术博客：先选作者或站点，再查看该来源的全部文章，不需要从截断文件名猜标题。

## 内容结构

```text
apple-docs/{en,zh}/<框架>/**.md       Apple 现行文档
wwdc/{en,zh}/<年份>/*.md              WWDC 逐字稿
blogs/{en,zh}/<来源>/*.md             英文博客及其译文
blogs/snapshots/<域名>/*.md           单页网页快照
blogs/snapshots-zh/<域名>/*.md        英文单页快照的中文译文
legacy-archive/vault/                 组织仓库的完整旧版归档快照
legacy-archive/{en,zh}/               高价值旧版文档的英文基线与中文译文
oss/<仓库>/                           Apple 开源与 Swift 一手资料
attachments/                          已本地化附件
_indexes/                             自动生成的阅读导航
meta/                                 项目状态、规范、术语和任务清单
tools/                                抓取、翻译、校验和索引工具
```

英文原文与中文译文通常保持相同相对路径，只把 `en/` 替换为 `zh/`。阅读时不需要手工
替换路径，文章目录已经提供直接入口。

## 图片现状

- Apple 现行文档图片已经下载到 `attachments/`，中英文共用同一份文件。
- 第三方博客目前多数仍引用原站图片；计划内英文快照的 77 个远程引用已本地化 64 个，
  另 13 个因资源域名 robots 禁止而保留原链接。
- WWDC 不保存视频。目前已把计划相关的 Session 415、416、423 官方 PDF 渲染为逐页
  WebP；其余场次只保留逐字稿和官方资源链接。

## 翻译原则

翻译采用三道质量关：

1. 按[翻译规范](meta/TRANSLATION_STYLE.md)和[术语表](meta/TERMS.md)翻译；
2. 由独立上下文进行语言和技术审校；
3. 运行机械校验，确保 frontmatter、链接、图片、代码和 Markdown 结构不被破坏。

当前项目采用[暑期定向翻译计划](meta/SUMMER_TRANSLATION_PLAN.md)，并不要求翻译仓库内
全部英文资料。强相关 B 类和受控 C1 试点的历史范围也记录在 `meta/` 中；新任务必须有
明确清单，不要根据目录前缀自行扩大范围。准确进度以[项目状态](meta/PROJECT_STATUS.md)和
[翻译状态索引](_indexes/translation-status.md)为准。

## 参与贡献

贡献从[贡献指南](CONTRIBUTING.md)开始。最小闭环是：确认范围 → 从 `main` 建分支 → 保持
英文/中文配对 → 独立审校 → 运行结构和链接检查 → 提交一个可独立审查的 PR。新 PR 也会
自动带上检查清单，便于维护者快速判断范围、质量门和未解决问题。

## 维护导航

新增、移动或翻译资料后运行：

```bash
python3 tools/title_aliases.py check
python3 tools/studyplan.py
python3 tools/indexes.py
python3 tools/check_links.py
```

`README.md` 是人工维护的稳定入口；`_indexes/` 下的来源目录、主题目录和状态统计由脚本
生成，不应手工修改。

更完整的抓取、翻译、审校、WWDC 幻灯片和 PR 要求见[贡献指南](CONTRIBUTING.md)。
