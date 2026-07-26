---
title: resizingMode
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimage/resizingmode-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/resizingmode-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/resizingmode-swift.property.json'
content_hash: 'sha256:000049f7db44c193'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# resizingMode

<sub>Instance Property</sub>

The resizing mode of the image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var resizingMode: UIImage.ResizingMode { get }
```

## Discussion

The default value for this property is [UIImageResizingModeTile](resizingmode-swift.enum/tile.md). However, [UIImage](../uiimage.md) will implement the resizing mode the fastest way possible while still retaining the desired visual appearance. This means that if the region to be resized is a 1-pixel region and this property is set to [UIImageResizingModeTile](resizingmode-swift.enum/tile.md), the region will be stretched instead because the two are virtually indistinguishable for a region of that size and stretching is dramatically faster than tiling. To set the value of this property, you need to call either [+ animatedResizableImageNamed:capInsets:resizingMode:duration:](<animatedresizableimagenamed(__capinsets_resizingmode_duration_).md>) or [- resizableImageWithCapInsets:resizingMode:](<resizableimage(withcapinsets_resizingmode_).md>) and specify the resizing mode using the `resizingMode` parameter. For a list of possible values for this property, see [ResizingMode](resizingmode-swift.enum.md).

## See Also

### Accessing image attributes

- [imageOrientation](imageorientation.md) — The orientation of the receiver’s image.
- [Orientation](orientation.md) — Constants that specify the intended display orientation for an image.
- [flipsForRightToLeftLayoutDirection](flipsforrighttoleftlayoutdirection.md) — A Boolean value that indicates whether the image flips in a right-to-left layout.
- [ResizingMode](resizingmode-swift.enum.md) — Constants that specify the possible resizing modes for an image.
- [duration](duration.md) — The time interval for displaying an animated image.
- [capInsets](capinsets.md) — The end-cap insets.
- [alignmentRectInsets](alignmentrectinsets.md) — The alignment metadata for positioning the image during layout.
- [symbolImage](issymbolimage.md) — A Boolean value that indicates whether the image is a symbol.
