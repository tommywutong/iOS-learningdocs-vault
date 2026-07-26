---
title: Pasteboard Data Type Representations
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
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [Documents, data, and pasteboard](documents-data-and-pasteboard.md) · [UIPasteboard](uipasteboard.md)

# Pasteboard Data Type Representations

<sub>API Collection</sub>

Pasteboard-item representation types, as for a given object value.

## Topics

### Constants

- [UIPasteboardTypeListString](uipasteboard/typeliststring.md) — An array of pasteboard-item representation types for string-type uniform type identifiers (UTIs), including the `kUTTypeUTF8PlainText` and `kUTTypeText` types. Related [UIPasteboard](uipasteboard.md) properties are [string](uipasteboard/string.md) and [strings](uipasteboard/strings.md).
- [UIPasteboardTypeListURL](uipasteboard/typelisturl.md) — An array of pasteboard-item representation types for URL-type uniform type identifiers (UTIs), including `kUTTypeURL`. Related [UIPasteboard](uipasteboard.md) properties are [URL](uipasteboard/url.md) and [URLs](uipasteboard/urls.md).
- [UIPasteboardTypeListImage](uipasteboard/typelistimage.md) — An array of pasteboard-item representation types for image-type uniform type identifiers (UTIs), including `kUTTypePNG` and `kUTTypeJPEG`. Related [UIPasteboard](uipasteboard.md) properties are [image](uipasteboard/image.md) and [images](uipasteboard/images.md).
- [UIPasteboardTypeListColor](uipasteboard/typelistcolor.md) — An array of pasteboard-item representation types for colors. Related [UIPasteboard](uipasteboard.md) properties are [color](uipasteboard/color.md) and [colors](uipasteboard/colors.md).
- [UIPasteboardTypeAutomatic](uipasteboard/typeautomatic.md) — An array of pasteboard-item representation types with automatically-determined uniform type identifiers (UTIs).

## See Also

### Constants

- [Name](uipasteboard/name-swift.struct.md) — Constants that identify the name of a pasteboard.
- [Pasteboard Names](pasteboard-names.md) — Names identifying the system pasteboards.
- [OptionsKey](uipasteboard/optionskey.md) — Options for describing pasteboard privacy.
- [UserInfo Dictionary Keys](userinfo-dictionary-keys.md) — Use these keys to access the representation types of pasteboard items that you add to, or remove from, a pasteboard.
