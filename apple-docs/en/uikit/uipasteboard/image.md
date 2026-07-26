---
title: image
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipasteboard/image
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/image'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/image.json'
content_hash: 'sha256:448bbf0577cdcf96'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteboard](../uipasteboard.md)

# image

<sub>Instance Property</sub>

The image object of the first pasteboard item.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@NSCopying var image: UIImage? { get set }
```

## Discussion

The value stored in this property is a [UIImage](../uiimage.md) object. The associated array of representation types is [UIPasteboardTypeListImage](typelistimage.md), which includes types `kUTTypePNG` and `kUTTypeJPEG`. Setting this property replaces all current items in the pasteboard with the new item.  If the first item has no value of the indicated type, `nil` is returned.

> [!note] Note
> Do not use this property to determine if a pasteboard contains image data. Instead, use the [hasImages](hasimages.md) property.

## See Also

### Getting and setting pasteboard items of standard data types

- [string](string.md) — The string value of the first pasteboard item.
- [strings](strings.md) — An array of strings in all pasteboard items.
- [images](images.md) — An array of image objects in all pasteboard items.
- [URL](url.md) — The URL object of the first pasteboard item.
- [URLs](urls.md) — An array of URL objects in all pasteboard items.
- [color](color.md) — The color object of the first pasteboard item.
- [colors](colors.md) — An array of color objects in all pasteboard items.
