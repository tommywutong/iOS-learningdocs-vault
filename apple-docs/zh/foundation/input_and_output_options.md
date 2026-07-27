---
title: 输入与输出选项
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/input_and_output_options
source_url: 'https://developer.apple.com/documentation/foundation/input_and_output_options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/input_and_output_options.json'
content_hash: 'sha256:1b496b7c1c887acc'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Foundation](../foundation.md) · [Archives and Serialization](archives-and-serialization.md) · [XML Processing and Modeling](xml-processing-and-modeling.md) · [XMLDocument](xmldocument.md)

# 输入与输出选项

<sub>API 集合</sub>

专门用于 `NSXMLDocument` 对象的输入与输出选项。

## 概述

由于 `NSXMLDocument` 是 [XMLNode](xmlnode.md) 的子类，你也可以使用 `NSXMLNode` 类参考中「Constants」一节所描述的相关输入与输出选项。你可以在 `NSXMLDocument` 的 [- initWithContentsOfURL:options:error:](<xmldocument/init(contentsof_options_).md>)、[- initWithData:options:error:](<xmldocument/init(data_options_).md>)、[- initWithXMLString:options:error:](<xmldocument/init(xmlstring_options_)-65m2r.md>) 方法中指定输入选项。[- XMLDataWithOptions:](<xmldocument/xmldata(options_).md>) 方法则接受输出选项。

## 主题

### 常量

- [NSXMLDocumentTidyHTML](xmlnode/options/documenttidyhtml.md) — 在处理文档期间将 HTML 格式化为有效的 XHTML。
- [NSXMLDocumentTidyXML](xmlnode/options/documenttidyxml.md) — 在处理文档期间将格式错误的 XML 转换为有效的 XML。
- [NSXMLDocumentValidate](xmlnode/options/documentvalidate.md) — 根据文档的 DTD（内部或外部）或 XML Schema 对其进行验证。
- [NSXMLDocumentXInclude](xmlnode/options/documentxinclude.md) — 将文档中所有 XInclude 节点替换为其所引用的节点。
- [NSXMLDocumentIncludeContentTypeDeclaration](xmlnode/options/documentincludecontenttypedeclaration.md) — 在文档的输出中包含 HTML 或 XHTML 的内容类型声明。

## 另请参阅

### 常量

- [ContentKind](xmldocument/contentkind.md) — 用于定义文档内容种类的类型。
- [Document Content Types](document-content-types.md) — 定义文档类型。
</content>
