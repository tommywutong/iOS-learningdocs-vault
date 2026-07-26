---
title: showsLargeContentViewer
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/showslargecontentviewer
source_url: 'https://developer.apple.com/documentation/uikit/uiview/showslargecontentviewer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/showslargecontentviewer.json'
content_hash: 'sha256:da3af072c5baf831'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# showsLargeContentViewer

<sub>Instance Property</sub>

A Boolean value that indicates whether to show the view in the large content viewer.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var showsLargeContentViewer: Bool { get set }
```

## Discussion

For this property to take effect, the view must have a [UILargeContentViewerInteraction](../uilargecontentviewerinteraction.md).

## See Also

### Modifying the accessibility behavior

- [accessibilityIgnoresInvertColors](accessibilityignoresinvertcolors.md) — A Boolean value indicating whether the view ignores an accessibility request to invert its colors.
- [largeContentImage](largecontentimage.md) — An image that represents the view in the large content viewer.
- [largeContentImageInsets](largecontentimageinsets.md) — Insets to adjust the position of the view’s image so it appears centered in the large content viewer.
- [largeContentTitle](largecontenttitle.md) — A string that describes the view in the large content viewer.
- [scalesLargeContentImage](scaleslargecontentimage.md) — A Boolean value that indicates whether the large content viewer scales the item’s image to a larger size.
