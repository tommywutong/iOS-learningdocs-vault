---
title: UIImage.Orientation.left
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimage/orientation/left
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/orientation/left'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/orientation/left.json'
content_hash: 'sha256:e8a545ad3ea43a83'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIImage](../../uiimage.md) · [Orientation](../orientation.md)

# UIImage.Orientation.left

<sub>Case</sub>

The image has been rotated 90° counterclockwise from the orientation of its original pixel data.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
case left
```

## Discussion

If an image is encoded with this orientation, then displayed by software unaware of orientation metadata, the image appears to be rotated 90° clockwise. (That is, to present the image in its intended orientation, you must rotate 90° counter-clockwise.)

![To correct an image with left orientation for display, rotate it 90° counterclockwise.](../../../../../attachments/a33bb23b55f1eb490a0abf2b86b81f66/media-2948305@2x.png)

## See Also

### Related Documentation

- [CGImagePropertyOrientation.left](../../../imageio/cgimagepropertyorientation/left.md) — The encoded image data is rotated 90° clockwise from the image’s intended display orientation.

### Image orientations

- [UIImageOrientationUp](up.md) — The original pixel data matches the image’s intended display orientation.
- [UIImageOrientationDown](down.md) — The image has been rotated 180° from the orientation of its original pixel data.
- [UIImageOrientationRight](right.md) — The image has been rotated 90° clockwise from the orientation of its original pixel data.
- [UIImageOrientationUpMirrored](upmirrored.md) — The image has been horizontally flipped from the orientation of its original pixel data.
- [UIImageOrientationDownMirrored](downmirrored.md) — The image has been vertically flipped from the orientation of its original pixel data.
- [UIImageOrientationLeftMirrored](leftmirrored.md) — The image has been rotated 90° clockwise and flipped horizontally from the orientation of its original pixel data.
- [UIImageOrientationRightMirrored](rightmirrored.md) — The image has been rotated 90° counterclockwise and flipped horizontally from the orientation of its original pixel data.
