---
title: scalesLargeContentImage
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilargecontentvieweritem/scaleslargecontentimage
source_url: 'https://developer.apple.com/documentation/uikit/uilargecontentvieweritem/scaleslargecontentimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilargecontentvieweritem/scaleslargecontentimage.json'
content_hash: 'sha256:1044ab7c01e06f65'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILargeContentViewerItem](../uilargecontentvieweritem.md)

# scalesLargeContentImage

<sub>Instance Property</sub>

A Boolean value that indicates whether the view scales the item’s image to a larger size or not.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var scalesLargeContentImage: Bool { get }
```

## Discussion

If [false](../../swift/false.md), the viewer displays the image at its intrinsic size.

> [!tip] Tip
> For best results when scaling, use a PDF asset with the Preserve Vector Data checked in the asset catalog.

## See Also

### Configuring display properties

- [largeContentTitle](largecontenttitle.md) — A string that describes an item to display in the large content viewer.
- [largeContentImage](largecontentimage.md) — An image that represents an item to display in the large content viewer.
- [largeContentImageInsets](largecontentimageinsets.md) — Insets to adjust the position of the item’s image so it appears visually centered in the large content viewer.
