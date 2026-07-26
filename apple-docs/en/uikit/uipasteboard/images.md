---
title: images
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipasteboard/images
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/images'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/images.json'
content_hash: 'sha256:128ecd582a740cea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteboard](../uipasteboard.md)

# images

<sub>Instance Property</sub>

An array of image objects in all pasteboard items.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var images: [UIImage]? { get set }
```

## Discussion

The value stored in this property is an array of [UIImage](../uiimage.md) objects. The associated array of representation types is [UIPasteboardTypeListImage](typelistimage.md), which includes types `kUTTypePNG` and `kUTTypeJPEG`. Setting this property replaces all current items in the pasteboard with the new items. The returned array may have fewer objects than the number of pasteboard items; this happens if a pasteboard item does not have a value of the indicated type.

> [!note] Note
> Do not use this property to determine if a pasteboard contains image data. Instead, use the [hasImages](hasimages.md) property.

## See Also

### Getting and setting pasteboard items of standard data types

- [string](string.md) — The string value of the first pasteboard item.
- [strings](strings.md) — An array of strings in all pasteboard items.
- [image](image.md) — The image object of the first pasteboard item.
- [URL](url.md) — The URL object of the first pasteboard item.
- [URLs](urls.md) — An array of URL objects in all pasteboard items.
- [color](color.md) — The color object of the first pasteboard item.
- [colors](colors.md) — An array of color objects in all pasteboard items.
