---
title: UIImage.Orientation.leftMirrored
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimage/orientation/leftmirrored
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/orientation/leftmirrored'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/orientation/leftmirrored.json'
content_hash: 'sha256:ef147eaaf550de6e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIImage](../../uiimage.md) · [Orientation](../orientation.md)

# UIImage.Orientation.leftMirrored

<sub>Case</sub>

The image has been rotated 90° clockwise and flipped horizontally from the orientation of its original pixel data.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
case leftMirrored
```

## Discussion

If an image is encoded with this orientation, then displayed by software unaware of orientation metadata, the image appears to be horizontally mirrored, then rotated 90° counter-clockwise. (That is, to present the image in its intended orientation, you can rotate it 90° clockwise, then flip horizontally.)

![To correct an image with leftMirrored orientation for display, rotate it 90° clockwise then flip it horizontally.](../../../../../attachments/ed7462784881f7d23e39b968a2ecefff/media-2948307@2x.png)

## See Also

### Related Documentation

- [CGImagePropertyOrientation.leftMirrored](../../../imageio/cgimagepropertyorientation/leftmirrored.md) — The encoded image data is horizontally flipped and rotated 90° counter-clockwise from the image’s intended display orientation.

### Image orientations

- [UIImageOrientationUp](up.md) — The original pixel data matches the image’s intended display orientation.
- [UIImageOrientationDown](down.md) — The image has been rotated 180° from the orientation of its original pixel data.
- [UIImageOrientationLeft](left.md) — The image has been rotated 90° counterclockwise from the orientation of its original pixel data.
- [UIImageOrientationRight](right.md) — The image has been rotated 90° clockwise from the orientation of its original pixel data.
- [UIImageOrientationUpMirrored](upmirrored.md) — The image has been horizontally flipped from the orientation of its original pixel data.
- [UIImageOrientationDownMirrored](downmirrored.md) — The image has been vertically flipped from the orientation of its original pixel data.
- [UIImageOrientationRightMirrored](rightmirrored.md) — The image has been rotated 90° counterclockwise and flipped horizontally from the orientation of its original pixel data.
