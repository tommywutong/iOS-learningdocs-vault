---
title: url
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipasteboard/url
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/url'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/url.json'
content_hash: 'sha256:b6b9afa7c20f4e50'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteboard](../uipasteboard.md)

# url

<sub>Instance Property</sub>

The URL object of the first pasteboard item.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var url: URL? { get set }
```

## Discussion

The value stored in this property is an [NSURL](../../foundation/nsurl.md) object. The associated array of representation types is [UIPasteboardTypeListURL](typelisturl.md), which includes type `kUTTypeURL`. Setting this property replaces all current items in the pasteboard with the new item.  If the first item has no value of the indicated type, `nil` is returned.

> [!note] Note
> Do not use this property to determine if a pasteboard contains URL data. Instead, use the [hasURLs](hasurls.md) property.

## See Also

### Getting and setting pasteboard items of standard data types

- [string](string.md) — The string value of the first pasteboard item.
- [strings](strings.md) — An array of strings in all pasteboard items.
- [image](image.md) — The image object of the first pasteboard item.
- [images](images.md) — An array of image objects in all pasteboard items.
- [URLs](urls.md) — An array of URL objects in all pasteboard items.
- [color](color.md) — The color object of the first pasteboard item.
- [colors](colors.md) — An array of color objects in all pasteboard items.
