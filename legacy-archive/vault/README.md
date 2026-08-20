# Apple Developer Documentation Archive（Obsidian 版）

本 vault 由 Apple Developer Documentation Archive 本地归档生成，供 Obsidian 直接打开阅读。文档与文件已按标题重命名，文档间链接为 wiki 链接，可在反向链接面板与关系图谱中查看双向关联。

## 统计

- 文档：5183 份
- 页面：40090 个 Markdown 文件
- 来源：https://developer.apple.com/library/archive/navigation/

## 当前完整性状态

本仓库保存 Apple 旧版官方文档及其翻译工作成果，但“原文已入库”和“中文已翻译”是两种
不同状态，不能混为一谈。

- 旧归档上一轮留下的 148 个精确缺口，本轮已恢复 114 个，其中 112 份为净新增英文原文，
  另 2 份为既有正文的 Apple ID / 标题修复；
- 仍有 34 份没有找到可验证的旧正文，因此当前**不能宣称全部英文原文已经就绪**；
- 本轮审计 969 个唯一配图文件：324 个已有或已恢复，20 个确认无有效图片回放，
  另有 625 个因 Wayback 传输错误待重试；这些不改变正文恢复数，但意味着附件尚未全齐；
- 新增的 112 份目前仍是原文，后续翻译必须按计划单独领取、审校和提交；
- 外部学习计划中的 338 个链接不属于本仓库的抓取分母、原文缺口或翻译欠账。

逐条来源、34 份未恢复清单、复现命令和 AI 交接计划见
[Archive Gap Phase 2](doc/ARCHIVE_GAP_PHASE2.md)；翻译批次与协作规则见
[翻译计划](doc/TRANSLATION_PLAN.md)。

## 协作与 AI 接手

接手者应先阅读上面两份文档，再从最新 `main` 创建独立功能分支。固定工作流为：

> 翻译 → 独立审校 → 机械校验 → 提 PR → 由仓库所有者审核合并

必须保持既有术语、标题、frontmatter、导航、分页和 Markdown 风格一致。执行者禁止直接
推送 `main`，禁止自行合并 PR；一个 PR 只处理明确领取的一批文档，不夹带抓取、改名、
目录迁移或无关索引重排。

## 按归档分类浏览

- [ApplePay_Guide](_indexes/ApplePay_Guide.md)（1 份）
- [LucidDreams](_indexes/LucidDreams.md)（1 份）
- [documentation](_indexes/documentation.md)（650 份）
- [featuredarticles](_indexes/featuredarticles.md)（8 份）
- [qa](_indexes/qa.md)（1517 份）
- [recipes](_indexes/recipes.md)（3 份）
- [referencelibrary](_indexes/referencelibrary.md)（39 份）
- [releasenotes](_indexes/releasenotes.md)（221 份）
- [samplecode](_indexes/samplecode.md)（1933 份）
- [technotes](_indexes/technotes.md)（810 份）

## 按资源类型浏览

- [Guide](_indexes/by-type/guide.md)（701 份）
- [QA](_indexes/by-type/qa.md)（1517 份）
- [Release Note](_indexes/by-type/release-note.md)（222 份）
- [Sample Code](_indexes/by-type/sample-code.md)（1934 份）
- [Technical Note](_indexes/by-type/technical-note.md)（809 份）

## 按平台浏览

- [CloudKit JS](_indexes/by-platform/cloudkit-js.md)（2 份）
- [iOS](_indexes/by-platform/ios.md)（873 份）
- [Java](_indexes/by-platform/java.md)（36 份）
- [macOS](_indexes/by-platform/macos.md)（4073 份）
- [Safari](_indexes/by-platform/safari.md)（13 份）
- [tvOS](_indexes/by-platform/tvos.md)（19 份）
- [watchOS](_indexes/by-platform/watchos.md)（28 份）
- [Xcode Developer Tools](_indexes/by-platform/xcode-developer-tools.md)（139 份）

## 使用提示

- 每页顶部有导航面包屑：总目录 → 分类索引 → 所属文档。
- 打开右侧「反向链接」面板可查看哪些页面引用了当前页。
- 「关系图谱」可浏览整个归档的链接结构。
- 图片保存在每份文档目录下的 attachments/ 中，离线可读。
