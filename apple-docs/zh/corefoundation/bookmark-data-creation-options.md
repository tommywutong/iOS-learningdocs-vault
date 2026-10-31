---
title: 书签数据创建选项
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/bookmark-data-creation-options
source_url: 'https://developer.apple.com/documentation/corefoundation/bookmark-data-creation-options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/bookmark-data-creation-options.json'
content_hash: 'sha256:978764520ef8cfe0'
translated: true
---

> 导航： [技术](../technologies.md) · [Core Foundation](../corefoundation.md) · [CFURL](cfurl.md)

# 书签数据创建选项

<sub>API 集合</sub>

创建书签数据时使用的选项。

## 概述

创建书签时，使用按位 `OR` 运算符组合你要指定的选项，并将它们提供给 [CFURLCreateBookmarkData](<cfurlcreatebookmarkdata(____________).md>) 方法的 `options` 参数。

### 版本说明

安全作用域书签在早于 OS X v10.7.3 的 macOS 版本中不可用。

## 主题

### 常量

- [kCFURLBookmarkCreationPreferFileIDResolutionMask](cfurlbookmarkcreationoptions/preferfileidresolutionmask.md) — 指定用该书签数据创建的别名优先以其嵌入的文件 ID 解析。 _(已废弃)_
- [kCFURLBookmarkCreationMinimalBookmarkMask](cfurlbookmarkcreationoptions/minimalbookmarkmask.md) — 指定用该书签数据创建的别名仅包含最少信息，这可能使其更小，但仍能以某些方式解析。
- [kCFURLBookmarkCreationSuitableForBookmarkFile](cfurlbookmarkcreationoptions/suitableforbookmarkfile.md) — 指定书签数据包含创建 Finder 别名文件所需的属性。
- [kCFURLBookmarkCreationWithSecurityScope](cfurlbookmarkcreationoptions/withsecurityscope.md) — 指定你要创建安全作用域书签；解析后会提供允许对文件系统资源进行读/写访问的安全作用域 URL；供采用 App Sandbox 的 App 使用。
- [kCFURLBookmarkCreationSecurityScopeAllowOnlyReadAccess](cfurlbookmarkcreationoptions/securityscopeallowonlyreadaccess.md) — 与 [kCFURLBookmarkCreationWithSecurityScope](cfurlbookmarkcreationoptions/withsecurityscope.md) 选项组合使用时，指定你要创建安全作用域书签；解析后会提供仅允许对文件系统资源进行只读访问的安全作用域 URL；供采用 App Sandbox 的 App 使用。

## 另请参阅

### 书签数据常量

- [书签数据解析选项](bookmark-data-resolution-options.md) — 解析书签数据时使用的选项。
