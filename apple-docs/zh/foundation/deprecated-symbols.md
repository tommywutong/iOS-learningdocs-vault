---
title: 已废弃符号
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/deprecated-symbols
source_url: 'https://developer.apple.com/documentation/foundation/deprecated-symbols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/deprecated-symbols.json'
content_hash: 'sha256:eb3174ad799c8b12'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Foundation](../foundation.md) · [字符串与文本](strings-and-text.md) · [NSAttributedString](nsattributedstring.md)

# 已废弃符号

<sub>API 集合</sub>

迁移代码，不再使用这些符号。

## 主题

### 已废弃的初始化方法

- [- initWithPath:documentAttributes:](<nsattributedstring/init(path_documentattributes_).md>) — 使用指定路径下文件中的 RTF 或 RTFD 数据初始化新的属性字符串对象。_(已废弃)_
- [- initWithURL:documentAttributes:](<nsattributedstring/init(url_documentattributes_).md>) — 使用指定 URL 中的数据初始化新的属性字符串对象。_(已废弃)_
- [- initWithFileURL:options:documentAttributes:error:](<nsattributedstring/init(fileurl_options_documentattributes_).md>) — 使用指定 URL 中的数据初始化新的属性字符串对象。_(已废弃)_

### 已废弃的属性

- [containsAttachments](nsattributedstring/containsattachments.md) — 一个布尔值，指示属性字符串是否包含任何附件属性。_(已废弃)_

### 已废弃的枚举

- [NSTextWritingDirection](../uikit/nstextwritingdirection.md) — 用于指定文本书写方向的选项。_(已废弃)_

### 已废弃的实例方法

- [- URLAtIndex:effectiveRange:](<nsattributedstring/url(at_effectiverange_).md>) — 返回用于自动链接检测的 URL；它来自链接属性，或来自指定位置处看起来像 URL 字符串的文本。_(已废弃)_
- [- drawWithRect:options:](<nsattributedstring/draw(with_options_).md>) — 使用指定选项，在当前图形上下文的指定矩形内绘制属性字符串。_(已废弃)_
- [- boundingRectWithSize:options:](<nsattributedstring/boundingrect(with_options_).md>) — 使用指定选项，为当前图形上下文中指定矩形内的属性字符串计算并返回边界矩形。_(已废弃)_
