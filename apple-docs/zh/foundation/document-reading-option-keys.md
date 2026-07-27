---
title: 文稿读取选项键
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/document-reading-option-keys
source_url: 'https://developer.apple.com/documentation/foundation/document-reading-option-keys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/document-reading-option-keys.json'
content_hash: 'sha256:88e7b83b5cf4be0d'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Foundation](../foundation.md) · [字符串与文本](strings-and-text.md) · [NSAttributedString](nsattributedstring.md)

# 文稿读取选项键

<sub>API 集合</sub>

用于从磁盘数据构建属性字符串的键。

## 概述

需要指定 [NSAttributedStringDocumentReadingOptionKey](../uikit/nsattributedstringdocumentreadingoptionkey.md) 类型的键时，请使用这些键。

## 主题

### 获取文稿选项

- [baseURL](nsattributedstring/documentreadingoptionkey/baseurl.md) — HTML 文稿的基础 URL。
- [characterEncoding](nsattributedstring/documentreadingoptionkey/characterencoding.md) — 字符串编码。
- [defaultAttributes](nsattributedstring/documentreadingoptionkey/defaultattributes.md) — 要应用于纯文本文件的默认属性。
- [documentType](nsattributedstring/documentreadingoptionkey/documenttype.md) — 文稿类型。
- [fileType](nsattributedstring/documentreadingoptionkey/filetype.md) — 文件类型。
- [readAccessURL](nsattributedstring/documentreadingoptionkey/readaccessurl.md) — WebKit 加载内容时可以访问的本地文件。
- [textEncodingName](nsattributedstring/documentreadingoptionkey/textencodingname.md) — 要使用的文本编码。
- [textSizeMultiplier](nsattributedstring/documentreadingoptionkey/textsizemultiplier.md) — 字体大小的缩放系数。
- [timeout](nsattributedstring/documentreadingoptionkey/timeout.md) — 等待文稿完成加载的时间，以秒为单位。
- [webPreferences](nsattributedstring/documentreadingoptionkey/webpreferences.md) — WebPreferences 对象。
- [webResourceLoadDelegate](nsattributedstring/documentreadingoptionkey/webresourceloaddelegate.md) — 用作网页资源加载委托（delegate）的对象。

### 获取字体缩放选项

- [sourceTextScaling](nsattributedstring/documentreadingoptionkey/sourcetextscaling.md) — 与文稿内容关联的文本缩放模式。
- [targetTextScaling](nsattributedstring/documentreadingoptionkey/targettextscaling.md) — 从磁盘读取文本后使用的文本缩放模式。

### 获取键类型

- [NSAttributedStringDocumentReadingOptionKey](../uikit/nsattributedstringdocumentreadingoptionkey.md) — 用于从磁盘读取的数据构建属性字符串的选项。

## 另请参阅

### 获取文稿范围的属性

- [NSAttributedStringDocumentAttributeKey](../uikit/nsattributedstringdocumentattributekey.md) — 应用于整个文稿的属性。
- [HTML 属性](html-attributes.md) — 控制所生成 HTML 形式的文稿范围属性。
- [NSAttributedStringDocumentType](../uikit/nsattributedstringdocumenttype.md) — 用作文稿类型文稿属性键的常量。
- [NSTextLayoutSectionKey](../uikit/nstextlayoutsectionkey.md) — 用作文稿属性键的文本布局节常量。
- [NSTextScalingType](../uikit/nstextscalingtype.md) — 指定文本缩放的常量。
