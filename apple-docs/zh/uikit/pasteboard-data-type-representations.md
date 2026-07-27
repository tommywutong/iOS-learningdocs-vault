---
title: 粘贴板数据类型表示
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/pasteboard-data-type-representations
source_url: 'https://developer.apple.com/documentation/uikit/pasteboard-data-type-representations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/pasteboard-data-type-representations.json'
content_hash: 'sha256:2b943d9aecab3052'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [Documents, data, and pasteboard](documents-data-and-pasteboard.md) · [UIPasteboard](uipasteboard.md)

# 粘贴板数据类型表示

<sub>API 集合</sub>

针对某个给定对象值的粘贴板项目表示类型。

## 主题

### 常量

- [UIPasteboardTypeListString](uipasteboard/typeliststring.md) — 一个数组，包含字符串类型统一类型标识符（UTI）对应的粘贴板项目表示类型，包括 `kUTTypeUTF8PlainText` 和 `kUTTypeText` 类型。相关的 [UIPasteboard](uipasteboard.md) 属性有 [string](uipasteboard/string.md) 和 [strings](uipasteboard/strings.md)。
- [UIPasteboardTypeListURL](uipasteboard/typelisturl.md) — 一个数组，包含 URL 类型统一类型标识符（UTI）对应的粘贴板项目表示类型，包括 `kUTTypeURL`。相关的 [UIPasteboard](uipasteboard.md) 属性有 [URL](uipasteboard/url.md) 和 [URLs](uipasteboard/urls.md)。
- [UIPasteboardTypeListImage](uipasteboard/typelistimage.md) — 一个数组，包含图像类型统一类型标识符（UTI）对应的粘贴板项目表示类型，包括 `kUTTypePNG` 和 `kUTTypeJPEG`。相关的 [UIPasteboard](uipasteboard.md) 属性有 [image](uipasteboard/image.md) 和 [images](uipasteboard/images.md)。
- [UIPasteboardTypeListColor](uipasteboard/typelistcolor.md) — 一个数组，包含颜色对应的粘贴板项目表示类型。相关的 [UIPasteboard](uipasteboard.md) 属性有 [color](uipasteboard/color.md) 和 [colors](uipasteboard/colors.md)。
- [UIPasteboardTypeAutomatic](uipasteboard/typeautomatic.md) — 一个数组，包含统一类型标识符（UTI）自动确定的粘贴板项目表示类型。

## 另请参阅

### 常量

- [Name](uipasteboard/name-swift.struct.md) — 标识某个粘贴板名称的常量。
- [Pasteboard Names](pasteboard-names.md) — 标识各系统粘贴板的名称。
- [OptionsKey](uipasteboard/optionskey.md) — 用于描述粘贴板隐私的选项。
- [UserInfo Dictionary Keys](userinfo-dictionary-keys.md) — 使用这些键来访问你添加到粘贴板中、或从粘贴板中移除的粘贴板项目的表示类型。
