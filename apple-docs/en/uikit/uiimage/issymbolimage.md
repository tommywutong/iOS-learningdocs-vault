---
title: isSymbolImage
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimage/issymbolimage
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/issymbolimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/issymbolimage.json'
content_hash: 'sha256:5b2e53223528bea8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# isSymbolImage

<sub>Instance Property</sub>

A Boolean value that indicates whether the image is a symbol.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var isSymbolImage: Bool { get }
```

## Discussion

Symbol images are vector-based images that you use for your app’s iconography. The value of this property is [true](../../swift/true.md) if the image is either a system-provided symbol image or a custom symbol image that you supplied in your asset catalog. The value is [false](../../swift/false.md) for all other image types.

## See Also

### Accessing image attributes

- [imageOrientation](imageorientation.md) — The orientation of the receiver’s image.
- [Orientation](orientation.md) — Constants that specify the intended display orientation for an image.
- [flipsForRightToLeftLayoutDirection](flipsforrighttoleftlayoutdirection.md) — A Boolean value that indicates whether the image flips in a right-to-left layout.
- [resizingMode](resizingmode-swift.property.md) — The resizing mode of the image.
- [ResizingMode](resizingmode-swift.enum.md) — Constants that specify the possible resizing modes for an image.
- [duration](duration.md) — The time interval for displaying an animated image.
- [capInsets](capinsets.md) — The end-cap insets.
- [alignmentRectInsets](alignmentrectinsets.md) — The alignment metadata for positioning the image during layout.
