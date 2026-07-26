---
title: largeContentImage
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilargecontentvieweritem/largecontentimage
source_url: 'https://developer.apple.com/documentation/uikit/uilargecontentvieweritem/largecontentimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilargecontentvieweritem/largecontentimage.json'
content_hash: 'sha256:7b85dbbc07c0908b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILargeContentViewerItem](../uilargecontentvieweritem.md)

# largeContentImage

<sub>Instance Property</sub>

An image that represents an item to display in the large content viewer.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var largeContentImage: UIImage? { get }
```

## Discussion

To present content in the large content viewer, you can provide either [largeContentTitle](largecontenttitle.md) or [largeContentImage](largecontentimage.md), or both.

This property defaults to an appropriate value for UIKit classes, otherwise `nil`.

## See Also

### Configuring display properties

- [largeContentTitle](largecontenttitle.md) — A string that describes an item to display in the large content viewer.
- [largeContentImageInsets](largecontentimageinsets.md) — Insets to adjust the position of the item’s image so it appears visually centered in the large content viewer.
- [scalesLargeContentImage](scaleslargecontentimage.md) — A Boolean value that indicates whether the view scales the item’s image to a larger size or not.
