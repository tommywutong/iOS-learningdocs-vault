---
title: accessibilityIgnoresInvertColors
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/accessibilityignoresinvertcolors
source_url: 'https://developer.apple.com/documentation/uikit/uiview/accessibilityignoresinvertcolors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/accessibilityignoresinvertcolors.json'
content_hash: 'sha256:b173291a87b565d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# accessibilityIgnoresInvertColors

<sub>Instance Property</sub>

A Boolean value indicating whether the view ignores an accessibility request to invert its colors.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var accessibilityIgnoresInvertColors: Bool { get set }
```

## Discussion

Inverting colors is often used to help users with light or color sensitivities to make bright colors darker. However, this behavior can have a destructive impact on images and videos. If inverting the colors would have a negative impact on your view’s content, set this property to [true](../../swift/true.md) to prevent it from inverting its colors. Setting the property to [true](../../swift/true.md) prevents the system from inverting the colors of the view and all of its subviews.

## See Also

### Modifying the accessibility behavior

- [largeContentImage](largecontentimage.md) — An image that represents the view in the large content viewer.
- [largeContentImageInsets](largecontentimageinsets.md) — Insets to adjust the position of the view’s image so it appears centered in the large content viewer.
- [largeContentTitle](largecontenttitle.md) — A string that describes the view in the large content viewer.
- [scalesLargeContentImage](scaleslargecontentimage.md) — A Boolean value that indicates whether the large content viewer scales the item’s image to a larger size.
- [showsLargeContentViewer](showslargecontentviewer.md) — A Boolean value that indicates whether to show the view in the large content viewer.
