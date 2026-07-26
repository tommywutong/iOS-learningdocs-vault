---
title: imageOrientation
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimage/imageorientation
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/imageorientation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/imageorientation.json'
content_hash: 'sha256:95057fe38ebe4a5e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# imageOrientation

<sub>Instance Property</sub>

The orientation of the receiver’s image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var imageOrientation: UIImage.Orientation { get }
```

## Discussion

Image orientation affects the way the image data is displayed when drawn. By default, images are displayed in the “up” orientation. If the image has associated metadata (such as EXIF information), however, this property contains the orientation indicated by that metadata. For a list of possible values for this property, see [Orientation](orientation.md).

## See Also

### Accessing image attributes

- [Orientation](orientation.md) — Constants that specify the intended display orientation for an image.
- [flipsForRightToLeftLayoutDirection](flipsforrighttoleftlayoutdirection.md) — A Boolean value that indicates whether the image flips in a right-to-left layout.
- [resizingMode](resizingmode-swift.property.md) — The resizing mode of the image.
- [ResizingMode](resizingmode-swift.enum.md) — Constants that specify the possible resizing modes for an image.
- [duration](duration.md) — The time interval for displaying an animated image.
- [capInsets](capinsets.md) — The end-cap insets.
- [alignmentRectInsets](alignmentrectinsets.md) — The alignment metadata for positioning the image during layout.
- [symbolImage](issymbolimage.md) — A Boolean value that indicates whether the image is a symbol.
