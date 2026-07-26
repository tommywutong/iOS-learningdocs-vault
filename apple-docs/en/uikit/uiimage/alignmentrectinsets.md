---
title: alignmentRectInsets
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimage/alignmentrectinsets
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/alignmentrectinsets'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/alignmentrectinsets.json'
content_hash: 'sha256:58d00278408af443'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# alignmentRectInsets

<sub>Instance Property</sub>

The alignment metadata for positioning the image during layout.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var alignmentRectInsets: UIEdgeInsets { get }
```

## Discussion

You can use the inset values as a hint for specifying the image contents more precisely. For example, if you have a 20 x 20 pixel icon that includes a glow effect, you might set the insets to {{2, 2}, {16, 16}} to indicate the position of the underlying icon without the glow effect.

Objects that incorporate images can use these insets to place the image properly within their content.

## See Also

### Accessing image attributes

- [imageOrientation](imageorientation.md) — The orientation of the receiver’s image.
- [Orientation](orientation.md) — Constants that specify the intended display orientation for an image.
- [flipsForRightToLeftLayoutDirection](flipsforrighttoleftlayoutdirection.md) — A Boolean value that indicates whether the image flips in a right-to-left layout.
- [resizingMode](resizingmode-swift.property.md) — The resizing mode of the image.
- [ResizingMode](resizingmode-swift.enum.md) — Constants that specify the possible resizing modes for an image.
- [duration](duration.md) — The time interval for displaying an animated image.
- [capInsets](capinsets.md) — The end-cap insets.
- [symbolImage](issymbolimage.md) — A Boolean value that indicates whether the image is a symbol.
