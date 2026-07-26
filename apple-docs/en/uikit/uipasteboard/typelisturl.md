---
title: typeListURL
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipasteboard/typelisturl
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/typelisturl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/typelisturl.json'
content_hash: 'sha256:ec2eaa6a57476d6a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteboard](../uipasteboard.md)

# typeListURL

<sub>Type Property</sub>

An array of pasteboard-item representation types for URL-type uniform type identifiers (UTIs), including `kUTTypeURL`. Related [UIPasteboard](../uipasteboard.md) properties are [URL](url.md) and [URLs](urls.md).

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class var typeListURL: NSArray
```

## See Also

### Constants

- [UIPasteboardTypeListString](typeliststring.md) — An array of pasteboard-item representation types for string-type uniform type identifiers (UTIs), including the `kUTTypeUTF8PlainText` and `kUTTypeText` types. Related [UIPasteboard](../uipasteboard.md) properties are [string](string.md) and [strings](strings.md).
- [UIPasteboardTypeListImage](typelistimage.md) — An array of pasteboard-item representation types for image-type uniform type identifiers (UTIs), including `kUTTypePNG` and `kUTTypeJPEG`. Related [UIPasteboard](../uipasteboard.md) properties are [image](image.md) and [images](images.md).
- [UIPasteboardTypeListColor](typelistcolor.md) — An array of pasteboard-item representation types for colors. Related [UIPasteboard](../uipasteboard.md) properties are [color](color.md) and [colors](colors.md).
- [UIPasteboardTypeAutomatic](typeautomatic.md) — An array of pasteboard-item representation types with automatically-determined uniform type identifiers (UTIs).
