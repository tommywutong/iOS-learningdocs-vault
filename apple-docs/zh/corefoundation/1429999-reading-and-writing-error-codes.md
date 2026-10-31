---
title: 读写错误码
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/1429999-reading-and-writing-error-codes
source_url: 'https://developer.apple.com/documentation/corefoundation/1429999-reading-and-writing-error-codes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/1429999-reading-and-writing-error-codes.json'
content_hash: 'sha256:e55e1bc0ebdd321f'
translated: true
---

> 导航： [技术](../technologies.md) · [Core Foundation](../corefoundation.md) · [CFPropertyList](cfpropertylist.md)

# 读写错误码

<sub>API 集合</sub>

用于属性列表读写函数（例如 [CFPropertyListCreateWithData](<cfpropertylistcreatewithdata(__________).md>)）的错误码。

## 主题

### 常量

- [kCFPropertyListReadCorruptError](kcfpropertylistreadcorrupterror.md) — 表示解析属性列表时出错。
- [kCFPropertyListReadUnknownVersionError](kcfpropertylistreadunknownversionerror.md) — 表示属性列表中的版本号未知。
- [kCFPropertyListReadStreamError](kcfpropertylistreadstreamerror.md) — 表示读取属性列表时发生流错误。
- [kCFPropertyListWriteStreamError](kcfpropertylistwritestreamerror.md) — 表示写入属性列表时发生流错误。

## 另请参阅

### 常量

- [CFPropertyListFormat](cfpropertylistformat.md) — 指定属性列表的格式。
- [属性列表可变性选项](property_list_mutability_options.md) — 用于确定新创建属性列表可变程度的选项标志。
