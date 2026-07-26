---
title: capInsets
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimage/capinsets
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/capinsets'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/capinsets.json'
content_hash: 'sha256:827c210071c294f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# capInsets

<sub>Instance Property</sub>

The end-cap insets.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var capInsets: UIEdgeInsets { get }
```

## Discussion

End caps specify the portion of an image that should not be resized when an image is stretched. This technique is used to implement buttons and other resizable image-based interface elements. When a button with end caps is resized, the resizing occurs only in the middle of the button, in the region between the end caps. The end caps themselves keep their original size and appearance.

This property specifies the sizes of all four end caps. The middle (stretchable) portion consists of all the pixels that are not included in the end caps. These pixels are tiled, left-to-right, top-to-bottom to fill the remaining space.

On a non-resizable image, this property is set to `UIEdgeInsetsZero`; the image does not use end caps and the entire image is subject to stretching. To create a new image with a nonzero value for this property, use the [- resizableImageWithCapInsets:](<resizableimage(withcapinsets_).md>) method. If your application specifies `UIEdgeInsetsZero` as the `capInsets` parameter, the entire image is tiled.

## See Also

### Accessing image attributes

- [imageOrientation](imageorientation.md) — The orientation of the receiver’s image.
- [Orientation](orientation.md) — Constants that specify the intended display orientation for an image.
- [flipsForRightToLeftLayoutDirection](flipsforrighttoleftlayoutdirection.md) — A Boolean value that indicates whether the image flips in a right-to-left layout.
- [resizingMode](resizingmode-swift.property.md) — The resizing mode of the image.
- [ResizingMode](resizingmode-swift.enum.md) — Constants that specify the possible resizing modes for an image.
- [duration](duration.md) — The time interval for displaying an animated image.
- [alignmentRectInsets](alignmentrectinsets.md) — The alignment metadata for positioning the image during layout.
- [symbolImage](issymbolimage.md) — A Boolean value that indicates whether the image is a symbol.
