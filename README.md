# Apple 文档与 iOS 底层知识归档

> 私有个人学习归档，收录 Apple 现行文档、WWDC 逐字稿、第三方技术博客及其中英文译文。
> 仓库包含受版权保护的材料，**不得直接转为公开仓库或重新分发**。

## 从这里开始

| 我想做什么 | 入口 |
|---|---|
| 不知道从哪里开始 | [阅读入口](_indexes/reader-guide.md) |
| 优先阅读已有中文正文的技术博客 | [可直接中文阅读](_indexes/chinese-blogs.md) |
| 按 Runtime、内存、并发等知识点浏览 | [iOS 底层知识地图](_indexes/topics.md) |
| 按中文目录标题查找其他英文文章 | [技术博客索引](_indexes/blogs.md) |
| 查找 Apple 文档、WWDC 或全部资料 | [文章目录](_indexes/articles.md) |
| 查看哪些已经翻译 | [翻译状态](_indexes/translation-status.md) |
| 按暑期计划学习 | [学习计划材料索引](_indexes/study-plan.md) |
| 按 Apple 框架浏览 | [Apple 文档索引](_indexes/apple-docs.md) |
| 按主题浏览 WWDC | [WWDC 索引](_indexes/wwdc.md) |
| 参与翻译或继续工程任务 | [贡献指南](CONTRIBUTING.md) |

在 Obsidian 中使用时，直接把仓库根目录作为 Vault 打开。GitHub 上的所有导航也使用普通
Markdown 相对链接，不依赖 Obsidian 专属语法。

## 怎样找到一篇资料

最省事的入口是[阅读入口](_indexes/reader-guide.md)：它先展示有完整中文正文的文章，再展示
只有中文目录标题、正文仍为英文的文章。分页、标签、归档和站点首页等误抓页面仍保留在原始
归档中，但不会混入读者目录。

### 按文章标题

[文章目录](_indexes/articles.md) 将资料按 Apple 文档、WWDC、技术博客分流到逐篇目录。
每篇记录都显示：

```text
中文标题｜英文标题｜作者/来源｜主题｜原文｜译文｜翻译状态
```

“仅标题中文，正文待翻译”表示只翻译了目录标题，点击后仍是英文正文；它不会计入译文完成数。
API、类型名、编译参数和产品名可能保持英文，避免为了出现汉字而误译专有名称。

“学习计划周次”只存在于独立的学习计划索引中，不属于通用文章元数据。

### 按主题

[主题目录](_indexes/topics.md) 提供 Objective-C Runtime、内存与 ARC、Block、RunLoop、
并发、性能、启动与链接、UI 渲染、网络安全等入口。同一篇文章可能属于多个主题。

主题由标题、WWDC 人工分组和来源元数据生成，适合发现资料，但不能代替全文搜索。

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
全部英文资料。准确进度以[项目状态](meta/PROJECT_STATUS.md)和
[翻译状态索引](_indexes/translation-status.md)为准。

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
