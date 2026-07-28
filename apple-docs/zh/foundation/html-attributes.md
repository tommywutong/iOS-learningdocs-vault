---
title: HTML 属性
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/html-attributes
source_url: 'https://developer.apple.com/documentation/foundation/html-attributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/html-attributes.json'
content_hash: 'sha256:0e7b7bb44a1345a2'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [字符串与文本](strings-and-text.md) · [NSAttributedString](nsattributedstring.md)

# HTML 属性

<sub>API 集合</sub>

对所生成 HTML 的形式提供控制的文稿范围属性。

## 概述

这些属性仅用于写入 HTML。[excludedElements](nsattributedstring/documentattributekey/excludedelements.md) 可用于控制所使用的标签。[excludedElements](nsattributedstring/documentattributekey/excludedelements.md) 数组中可识别的值包括不区分大小写的 HTML 标签，以及 DOCTYPE（表示 doctype 声明）和 XML（表示 XML 声明）。默认情况下，如果不存在此属性，排除的元素将包括 HTML 4 中已废弃的元素（APPLET、BASEFONT、CENTER、DIR、FONT、ISINDEX、MENU、S、STRIKE 和 U）以及 XML。如果列表中包含 XML，则使用 HTML 形式；如果列表中不包含 XML，则在存在差异之处使用 XHTML 形式。可以使用 [characterEncoding](nsattributedstring/documentattributekey/characterencoding.md) 或 [textEncodingName](nsattributedstring/documentattributekey/textencodingname.md) 控制生成 HTML 时使用的编码；无法用指定编码表示的字符会使用字符实体。[prefixSpaces](nsattributedstring/documentattributekey/prefixspaces.md) 可用于对格式进行一定程度的控制。

## 主题

### 获取属性

- [excludedElements](nsattributedstring/documentattributekey/excludedelements.md) — 要从生成的 HTML 中排除的 HTML 元素。
- [textEncodingName](nsattributedstring/documentattributekey/textencodingname.md) — 要使用的文本编码名称。
- [prefixSpaces](nsattributedstring/documentattributekey/prefixspaces.md) — 用于缩进嵌套 HTML 元素的空格数。

## 另请参阅

### 获取文稿范围属性

- [DocumentAttributeKey](nsattributedstring/documentattributekey.md) — 应用于整个文稿的属性。
- [DocumentReadingOptionKey](nsattributedstring/documentreadingoptionkey.md) — 从磁盘读取的数据构造属性字符串时使用的选项。
- [DocumentType](nsattributedstring/documenttype.md) — 文稿类型文稿属性键的常量。
- [TextLayoutSectionKey](nsattributedstring/textlayoutsectionkey.md) — 文本布局区段文稿属性键的常量。
- [NSTextScalingType](../uikit/nstextscalingtype.md) — 指定文本缩放方式的常量。
