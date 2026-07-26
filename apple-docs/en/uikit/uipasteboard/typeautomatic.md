---
title: typeAutomatic
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipasteboard/typeautomatic
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/typeautomatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/typeautomatic.json'
content_hash: 'sha256:a4260ec8f79b099f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteboard](../uipasteboard.md)

# typeAutomatic

<sub>Type Property</sub>

An array of pasteboard-item representation types with automatically-determined uniform type identifiers (UTIs).

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class let typeAutomatic: String
```

## Discussion

Use this type in the [- setItems:options:](<setitems(__options_).md>) method to automatically insert appropriate UTIs for supported types. In iOS 10, supported types are [NSString](../../foundation/nsstring.md), [NSAttributedString](../../foundation/nsattributedstring.md), [NSURL](../../foundation/nsurl.md), [UIImage](../uiimage.md), and [UIColor](../uicolor.md).

## See Also

### Constants

- [UIPasteboardTypeListString](typeliststring.md) — An array of pasteboard-item representation types for string-type uniform type identifiers (UTIs), including the `kUTTypeUTF8PlainText` and `kUTTypeText` types. Related [UIPasteboard](../uipasteboard.md) properties are [string](string.md) and [strings](strings.md).
- [UIPasteboardTypeListURL](typelisturl.md) — An array of pasteboard-item representation types for URL-type uniform type identifiers (UTIs), including `kUTTypeURL`. Related [UIPasteboard](../uipasteboard.md) properties are [URL](url.md) and [URLs](urls.md).
- [UIPasteboardTypeListImage](typelistimage.md) — An array of pasteboard-item representation types for image-type uniform type identifiers (UTIs), including `kUTTypePNG` and `kUTTypeJPEG`. Related [UIPasteboard](../uipasteboard.md) properties are [image](image.md) and [images](images.md).
- [UIPasteboardTypeListColor](typelistcolor.md) — An array of pasteboard-item representation types for colors. Related [UIPasteboard](../uipasteboard.md) properties are [color](color.md) and [colors](colors.md).
