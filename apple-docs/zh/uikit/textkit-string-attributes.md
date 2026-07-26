---
title: TextKit 字符串属性
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/textkit-string-attributes
source_url: 'https://developer.apple.com/documentation/uikit/textkit-string-attributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/textkit-string-attributes.json'
content_hash: 'sha256:724df6c752357e37'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [TextKit](textkit.md)

# TextKit 字符串属性

<sub>API 集合</sub>

用于显示文本和管理文稿的 UIKit 专属键与值。

## 概述

UIKit 定义了这些属性和属性键，供你在 [NSAttributedString](../foundation/nsattributedstring.md) 和 [NSMutableAttributedString](../foundation/nsmutableattributedstring.md) 中指定属性值时使用。

## 主题

### Getting text content attributes

- [TextKit string attribute keys](textkit-string-attribute-keys.md) — 用于为属性字符串中的字符范围应用属性的 UIKit 专属键。
- [NSTextHighlightStyle](nstexthighlightstyle.md) — 指定要应用于文本的高亮类型的常量。
- [NSTextHighlightColorScheme](nstexthighlightcolorscheme.md) — 指定要用于文本的高亮颜色的常量。
- [NSTextEffectStyle](nstexteffectstyle.md) — 指定要应用于文本的效果类型的常量。
- [NSUnderlineStyle](nsunderlinestyle.md) — 用于下划线样式和删除线样式属性键的常量。
- [NSWritingDirectionFormatType](nswritingdirectionformattype.md) — 用于书写方向属性键的常量。

### Getting document-wide attributes

- [NSAttributedStringDocumentAttributeKey](nsattributedstringdocumentattributekey.md) — 你应用于整个文稿的属性。
- [Document reading option keys](document-reading-option-keys.md) — 用于从磁盘上的数据构建属性字符串的键。
- [NSAttributedStringDocumentType](nsattributedstringdocumenttype.md) — 用于文稿类型这一文稿属性键的常量。
- [NSTextLayoutSectionKey](nstextlayoutsectionkey.md) — 用于文本布局分区这一文稿属性键的常量。
- [NSTextScalingType](nstextscalingtype.md) — 指定文本缩放方式的常量。

### Deprecated constants

- [NSTextWritingDirection](nstextwritingdirection.md) — 用于指定文本书写方向的选项。_(已废弃)_

## 另请参阅

### Text management

- [NSTextContentStorage](nstextcontentstorage.md) — 一个具体对象，用于管理你视图的文本内容，并生成布局所需的文本元素。
- [NSTextContentManager](nstextcontentmanager.md) — 一个抽象类，定义了管理文本文稿内容的接口和默认实现。
- [NSAttributedString](../foundation/nsattributedstring.md) — 一段文本字符串，为字符范围管理数据、布局和样式信息，以支持渲染。
- [NSMutableAttributedString](../foundation/nsmutableattributedstring.md) — 一个可变字符串，其文本各部分带有关联属性（例如视觉样式、超链接或辅助功能数据）。
