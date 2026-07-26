---
title: 粘贴板名称
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/pasteboard-names
source_url: 'https://developer.apple.com/documentation/uikit/pasteboard-names'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/pasteboard-names.json'
content_hash: 'sha256:b4dbbdc0862f5ef5'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [Documents, data, and pasteboard](documents-data-and-pasteboard.md) · [UIPasteboard](uipasteboard.md)

# 粘贴板名称

<sub>API 集合</sub>

标识各系统粘贴板的名称。

## 概述

你可以通过调用类方法 [+ pasteboardWithName:create:](<uipasteboard/init(name_create_).md>)、并将 `UIPasteboardNameGeneral` 常量作为第一个参数，来访问通用系统粘贴板。你也可以通过调用 [generalPasteboard](uipasteboard/general.md) 类方法来访问通用粘贴板。通用系统粘贴板在设备重启、App 卸载和 App 恢复期间都会持久保留。

## 主题

### Constants

- [UIPasteboardNameGeneral](uipasteboard/name-swift.struct/general.md) — 标识通用粘贴板的名称，你可将其用于一般的复制-剪切-粘贴操作。
- [UIPasteboardNameFind](uipasteboardnamefind.md) — 标识 Find 粘贴板的名称。_(已废弃)_

## 另请参阅

### Constants

- [Name](uipasteboard/name-swift.struct.md) — 标识某个粘贴板名称的常量。
- [OptionsKey](uipasteboard/optionskey.md) — 用于描述粘贴板隐私的选项。
- [Pasteboard Data Type Representations](pasteboard-data-type-representations.md) — 针对某个给定对象值的粘贴板项目表示类型。
- [UserInfo Dictionary Keys](userinfo-dictionary-keys.md) — 使用这些键来访问你添加到粘贴板中、或从粘贴板中移除的粘贴板项目的表示类型。
