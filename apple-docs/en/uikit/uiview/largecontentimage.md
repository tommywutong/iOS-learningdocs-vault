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
doc_path: /documentation/uikit/uiview/largecontentimage
source_url: 'https://developer.apple.com/documentation/uikit/uiview/largecontentimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/largecontentimage.json'
content_hash: 'sha256:e0642a1bc0e27ca8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# largeContentImage

<sub>Instance Property</sub>

An image that represents the view in the large content viewer.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var largeContentImage: UIImage? { get set }
```

## Discussion

To present content in the large content viewer, you can provide either [largeContentTitle](largecontenttitle.md) or [largeContentImage](largecontentimage.md), or both.

This property defaults to an appropriate value for UIKit classes; otherwise, it’s `nil`.

## See Also

### Modifying the accessibility behavior

- [accessibilityIgnoresInvertColors](accessibilityignoresinvertcolors.md) — A Boolean value indicating whether the view ignores an accessibility request to invert its colors.
- [largeContentImageInsets](largecontentimageinsets.md) — Insets to adjust the position of the view’s image so it appears centered in the large content viewer.
- [largeContentTitle](largecontenttitle.md) — A string that describes the view in the large content viewer.
- [scalesLargeContentImage](scaleslargecontentimage.md) — A Boolean value that indicates whether the large content viewer scales the item’s image to a larger size.
- [showsLargeContentViewer](showslargecontentviewer.md) — A Boolean value that indicates whether to show the view in the large content viewer.
