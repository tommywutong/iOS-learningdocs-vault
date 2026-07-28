---
title: 创建方法
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/creation-methods
source_url: 'https://developer.apple.com/documentation/foundation/creation-methods'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/creation-methods.json'
content_hash: 'sha256:c61b55e51cecd773'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [字符串与文本](strings-and-text.md) · [NSAttributedString](nsattributedstring.md)

# 创建方法

<sub>API 集合</sub>

从现有内容或原始文本创建属性字符串，并应用初始属性（attribute）。

## 主题

### 从另一个字符串创建

- [- initWithString:](<nsattributedstring/init(string_).md>) — 使用指定文本创建不含属性信息的属性字符串。
- [- initWithString:attributes:](<nsattributedstring/init(string_attributes_).md>) — 使用指定文本和属性创建属性字符串。
- [- initWithAttributedString:](<nsattributedstring/init(attributedstring_).md>) — 使用另一个属性字符串的内容创建新的属性字符串。

### 创建格式化字符串

- [init(_:)](<nsattributedstring/init(__).md>) — 使用指定的值类型（value type）属性字符串创建引用类型（reference type）属性字符串。
- [init(_:including:)](<nsattributedstring/init(__including_)-9gogq.md>) — 使用指定的值类型属性字符串创建引用类型属性字符串，并包含一个属性作用域。
- [init(_:including:)](<nsattributedstring/init(__including_)-8iy4i.md>) — 使用指定的值类型属性字符串创建引用类型属性字符串，并包含由键路径（key path）标识的属性作用域。

### 从数据文件创建

- [- initWithData:options:documentAttributes:error:](<nsattributedstring/init(data_options_documentattributes_).md>) — 使用指定数据对象的内容创建属性字符串。
- [- initWithDocFormat:documentAttributes:](<nsattributedstring/init(docformat_documentattributes_).md>) — 使用指定数据对象中的 Microsoft Word 格式数据创建属性字符串。
- [- initWithURL:options:documentAttributes:error:](<nsattributedstring/init(url_options_documentattributes_).md>) — 使用指定 URL 的内容创建属性字符串。

### 从 HTML 创建

- [- initWithHTML:documentAttributes:](<nsattributedstring/init(html_documentattributes_).md>) — 使用指定数据对象中的 HTML 创建属性字符串。
- [- initWithHTML:baseURL:documentAttributes:](<nsattributedstring/init(html_baseurl_documentattributes_).md>) — 使用指定数据对象和基础 URL 中的 HTML 创建属性字符串。
- [- initWithHTML:options:documentAttributes:](<nsattributedstring/init(html_options_documentattributes_).md>) — 使用指定数据对象中的 HTML 创建属性字符串。
- [+ loadFromHTMLWithRequest:options:completionHandler:](<nsattributedstring/loadfromhtml(request_options_completionhandler_).md>) — 转换指定 HTML URL 请求的内容来创建属性字符串。
- [+ loadFromHTMLWithFileURL:options:completionHandler:](<nsattributedstring/loadfromhtml(fileurl_options_completionhandler_).md>) — 转换指定 URL 处本地 HTML 文件的内容来创建属性字符串。
- [+ loadFromHTMLWithString:options:completionHandler:](<nsattributedstring/loadfromhtml(string_options_completionhandler_).md>) — 使用指定的 HTML 字符串创建属性字符串。
- [+ loadFromHTMLWithData:options:completionHandler:](<nsattributedstring/loadfromhtml(data_options_completionhandler_).md>) — 使用指定的 HTML 数据创建属性字符串。
- [CompletionHandler](nsattributedstring/completionhandler.md) — 用于获取异步属性字符串的完成处理程序（completion handler）。

### 从 RTF 创建

- [- initWithRTF:documentAttributes:](<nsattributedstring/init(rtf_documentattributes_).md>) — 解码指定数据对象中的 RTF 命令和数据流来创建属性字符串。
- [- initWithRTFD:documentAttributes:](<nsattributedstring/init(rtfd_documentattributes_).md>) — 解码指定数据对象中的 RTFD 命令和数据流来创建属性字符串。
- [- initWithRTFDFileWrapper:documentAttributes:](<nsattributedstring/init(rtfdfilewrapper_documentattributes_).md>) — 使用包含 RTFD 文稿的指定文件包装器创建属性字符串。

### 从 Markdown 创建

- [init(markdown:options:baseURL:)](<nsattributedstring/init(markdown_options_baseurl_)-m9n.md>) — 使用提供的选项，从 Markdown 格式字符串创建属性字符串。
- [init(markdown:options:baseURL:)](<nsattributedstring/init(markdown_options_baseurl_)-5nru2.md>) — 使用提供的选项，从 Markdown 格式数据创建属性字符串。
- [init(contentsOf:options:baseURL:)](<nsattributedstring/init(contentsof_options_baseurl_).md>) — 使用提供的选项，从包含 Markdown 格式数据的指定 URL 内容创建属性字符串。

### 创建带附件的字符串

- [+ attributedStringWithAttachment:](<nsattributedstring/init(attachment_).md>) — 创建带附件的属性字符串。
- [+ attributedStringWithAttachment:attributes:](<nsattributedstring/init(attachment_attributes_).md>) — 创建带附件的属性字符串，并对其应用指定属性。
- [+ attributedStringWithAdaptiveImageGlyph:attributes:](<nsattributedstring/init(adaptiveimageglyph_attributes_).md>) — 创建带自适应图像字形的属性字符串，并对其应用指定属性。
