---
title: UserInfo 字典键
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/userinfo-dictionary-keys
source_url: 'https://developer.apple.com/documentation/uikit/userinfo-dictionary-keys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/userinfo-dictionary-keys.json'
content_hash: 'sha256:a60091ebbff92a42'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [文稿、数据与粘贴板](documents-data-and-pasteboard.md) · [UIPasteboard](uipasteboard.md)

# UserInfo 字典键

<sub>API 集合</sub>

使用这些键来访问你向粘贴板添加或从中移除的粘贴板条目的表示类型。

## 主题

### 常量

- [UIPasteboardChangedTypesAddedKey](uipasteboard/changedtypesaddeduserinfokey.md) — 对于名为 [UIPasteboardChangedNotification](uipasteboard/changednotification.md) 的通知，使用此键访问已添加的表示类型。这些类型以数组形式存储在通知的 `userInfo` 字典中。
- [UIPasteboardChangedTypesRemovedKey](uipasteboard/changedtypesremoveduserinfokey.md) — 对于名为 [UIPasteboardChangedNotification](uipasteboard/changednotification.md) 的通知，使用此键访问已移除的表示类型。这些类型以数组形式存储在通知的 `userInfo` 字典中。

## 另请参阅

### 常量

- [Name](uipasteboard/name-swift.struct.md) — 标识粘贴板名称的常量。
- [粘贴板名称](pasteboard-names.md) — 标识系统粘贴板的名称。
- [OptionsKey](uipasteboard/optionskey.md) — 用于描述粘贴板隐私的选项。
- [粘贴板数据类型表示](pasteboard-data-type-representations.md) — 粘贴板条目的表示类型，例如给定对象值的表示类型。
