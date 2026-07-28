---
title: 文稿内容类型
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/document-content-types
source_url: 'https://developer.apple.com/documentation/foundation/document-content-types'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/document-content-types.json'
content_hash: 'sha256:c0f5d199b27a615c'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [归档与序列化](archives-and-serialization.md) · [XML 处理与建模](xml-processing-and-modeling.md) · [XMLDocument](xmldocument.md)

# 文稿内容类型

<sub>API 集合</sub>

定义文稿类型。

## 概述

在 [documentContentKind](xmldocument/documentcontentkind.md) 中指定一个 NSXMLDocumentContentKind 常量，以指明文稿输出所需的内容种类。

## 主题

### 常量

- [NSXMLDocumentXMLKind](xmldocument/contentkind/xml.md) — 默认的文稿内容类型，即 XML。
- [NSXMLDocumentXHTMLKind](xmldocument/contentkind/xhtml.md) — 文稿输出为 XHTML。
- [NSXMLDocumentHTMLKind](xmldocument/contentkind/html.md) — 以 HTML 形式输出没有结束标签的空标签，例如 `<br>`。
- [NSXMLDocumentTextKind](xmldocument/contentkind/text.md) — 从所有文本节点提取字符串值，以输出文稿的字符串值。

## 另请参阅

### 常量

- [输入和输出选项](input_and_output_options.md) — 专门用于 `NSXMLDocument` 对象的输入和输出选项。
- [ContentKind](xmldocument/contentkind.md) — 用于定义文稿内容种类的类型。
