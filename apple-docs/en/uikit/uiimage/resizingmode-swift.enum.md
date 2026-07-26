---
title: UIImage.ResizingMode
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimage/resizingmode-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/resizingmode-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/resizingmode-swift.enum.json'
content_hash: 'sha256:a8f9ca29f4e182e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# UIImage.ResizingMode

<sub>Enumeration</sub>

Constants that specify the possible resizing modes for an image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
enum ResizingMode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIImageResizingModeTile](resizingmode-swift.enum/tile.md) — The image is tiled when it is resized. In other words, the interior region of the original image will be repeated to fill in the interior region of the newly resized image.
- [UIImageResizingModeStretch](resizingmode-swift.enum/stretch.md) — The image is stretched when it is resized. In other words, the interior region of the original image will be scaled to fill in the interior region of the newly resized imaged.

### Initializers

- [init(rawValue:)](<resizingmode-swift.enum/init(rawvalue_).md>)

## See Also

### Accessing image attributes

- [imageOrientation](imageorientation.md) — The orientation of the receiver’s image.
- [Orientation](orientation.md) — Constants that specify the intended display orientation for an image.
- [flipsForRightToLeftLayoutDirection](flipsforrighttoleftlayoutdirection.md) — A Boolean value that indicates whether the image flips in a right-to-left layout.
- [resizingMode](resizingmode-swift.property.md) — The resizing mode of the image.
- [duration](duration.md) — The time interval for displaying an animated image.
- [capInsets](capinsets.md) — The end-cap insets.
- [alignmentRectInsets](alignmentrectinsets.md) — The alignment metadata for positioning the image during layout.
- [symbolImage](issymbolimage.md) — A Boolean value that indicates whether the image is a symbol.
