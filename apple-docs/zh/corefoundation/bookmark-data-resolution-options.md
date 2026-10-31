---
title: 书签数据解析选项
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/bookmark-data-resolution-options
source_url: 'https://developer.apple.com/documentation/corefoundation/bookmark-data-resolution-options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/bookmark-data-resolution-options.json'
content_hash: 'sha256:b678b020db728dab'
translated: true
---

> 导航： [技术](../technologies.md) · [Core Foundation](../corefoundation.md) · [CFURL](cfurl.md)

# 书签数据解析选项

<sub>API 集合</sub>

解析书签数据时使用的选项。

## 概述

解析书签以获取 URL 时，使用按位 `OR` 运算符组合你要指定的选项，并将它们提供给 [CFURLCreateByResolvingBookmarkData](<cfurlcreatebyresolvingbookmarkdata(______________).md>) 函数的 `options` 参数。

### 版本说明

安全作用域书签在早于 OS X v10.7.3 的 macOS 版本中不可用。

## 主题

### 常量

- [kCFBookmarkResolutionWithoutUIMask](cfurlbookmarkresolutionoptions/cfbookmarkresolutionwithoutuimask.md) — 指定解析书签数据时不附带 UI 反馈。
- [kCFBookmarkResolutionWithoutMountingMask](cfurlbookmarkresolutionoptions/cfbookmarkresolutionwithoutmountingmask.md) — 指定解析书签数据期间不应挂载任何宗卷。
- [kCFURLBookmarkResolutionWithSecurityScope](cfurlbookmarkresolutionoptions/cfurlbookmarkresolutionwithsecurityscope.md) — 指定在解析书签数据期间应使用创建该书签时应用的安全作用域。

## 另请参阅

### 书签数据常量

- [书签数据创建选项](bookmark-data-creation-options.md) — 创建书签数据时使用的选项。
