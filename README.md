# Apple 文档与 iOS 底层知识归档

> 私有个人学习归档。生成于 2026-07-27，统计数字由 `tools/indexes.py` 实际扫描得出。

## 这是什么

把 iOS 底层学习需要的一手材料抓成本地 Markdown，放进 Obsidian 阅读，并翻译成中文。
四个来源：

| 来源 | 内容 | 数量 | 已译 |
|---|---|---:|---:|
| **Apple 现行文档** | `developer.apple.com/documentation`，282 个框架 | 95,634 页（成篇文章 3,746） | 0 |
| **WWDC 逐字稿** | 按主题筛选，9 个分组 | 178 场 | 0 |
| **第三方技术博客** | 经甄别的一手来源 | 1,736 篇 | 595 |
| **Apple 开源** | objc4 / dyld / CF / libdispatch 等 | 18 个仓库 | — |

图片附件 2,536 个 / 1.02 GB（超过 1 MB 的已按最长边压缩，见 `meta/shrink_report.json`）。

## 怎么用

| 我想… | 去哪 |
|---|---|
| **按学习计划找材料** | [`_indexes/study-plan.md`](_indexes/study-plan.md) —— 把 2026 暑假学习计划的每个外链映射到本地文件，按周次和 Day 组织 |
| 按框架浏览 Apple 文档 | [`_indexes/apple-docs.md`](_indexes/apple-docs.md) |
| 找 WWDC session | [`_indexes/wwdc.md`](_indexes/wwdc.md) |
| 看博客归档与授权 | [`_indexes/blogs.md`](_indexes/blogs.md) |

## 目录结构

```
apple-docs/{en,zh}/<框架>/**.md    Apple 现行文档
wwdc/{en,zh}/<年份>/*.md           WWDC 逐字稿
blogs/{en,zh}/<源>/*.md            第三方博客
blogs/snapshots/<域名>/*.md        学习计划点名的单页快照
oss/<仓库>/                        Apple 开源与 Swift 一手资料
attachments/                       图片，各来源共用
_indexes/                          导航索引
meta/                              规范、术语表、清单、侦察报告
tools/                             抓取与渲染工具链
```

**英文原文在 `en/`，中文译文在 `zh/`，路径一一对应。** 不做原地替换——现行文档是
Apple 在维护的活内容，留着英文基线才能靠 frontmatter 里的 `content_hash` 做增量
diff、只重译变化的部分。中文来源的博客只有 `zh/`。

## 翻译

- 规范：[`meta/TRANSLATION_STYLE.md`](meta/TRANSLATION_STYLE.md)
- 术语表：[`meta/TERMS.md`](meta/TERMS.md) —— 按 **Apple 官方简体中文优先**裁决，
  187 条有官方依据。与旧仓库 `apple-developer-archive-vault` 的术语选择**有意分歧**，
  不要互相「纠正」。
- 三道关：译者 → 独立审校 → `tools/validate.py` 机械校验（13 类错误注入测试，零漏检零误报）

## 版权

Apple 文档与 WWDC 逐字稿为 Apple 版权所有。第三方博客逐源授权见
[`_indexes/blogs.md`](_indexes/blogs.md)，其中仅 `onevcat`（CC BY 4.0）与
`saagarjha`（CC BY-SA 4.0）明确允许再分发。Apple 开源代码为 APSL 2.0 / Apache-2.0，
源码目录保持逐字节原样，笔记一律写在 `oss/notes/`。

**本仓库为私有个人学习归档，不得转为公开。**
