---
title: UIImage.Orientation.rightMirrored
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimage/orientation/rightmirrored
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/orientation/rightmirrored'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/orientation/rightmirrored.json'
content_hash: 'sha256:72f63b9557333a5c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIImage](../../uiimage.md) · [Orientation](../orientation.md)

# UIImage.Orientation.rightMirrored

<sub>Case</sub>

The image has been rotated 90° counterclockwise and flipped horizontally from the orientation of its original pixel data.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
case rightMirrored
```

## Discussion

If an image is encoded with this orientation, then displayed by software unaware of orientation metadata, the image appears to be horizontally mirrored, then rotated 90° clockwise. (That is, to present the image in its intended orientation, you can rotate  90° counter-clockwise, then flip horizontally.)

![](../../../../../attachments/6427cc1184994ac80c5119002426bac6/media-2948306@2x.png)

<sub>To correct an image with rightMirrored orientation for display, rotate it 90° counterclockwise then flip it horizontally.</sub>

## See Also

### Related Documentation

- [CGImagePropertyOrientation.rightMirrored](../../../imageio/cgimagepropertyorientation/rightmirrored.md) — The encoded image data is horizontally flipped and rotated 90° clockwise from the image’s intended display orientation.

### Image orientations

- [UIImageOrientationUp](up.md) — The original pixel data matches the image’s intended display orientation.
- [UIImageOrientationDown](down.md) — The image has been rotated 180° from the orientation of its original pixel data.
- [UIImageOrientationLeft](left.md) — The image has been rotated 90° counterclockwise from the orientation of its original pixel data.
- [UIImageOrientationRight](right.md) — The image has been rotated 90° clockwise from the orientation of its original pixel data.
- [UIImageOrientationUpMirrored](upmirrored.md) — The image has been horizontally flipped from the orientation of its original pixel data.
- [UIImageOrientationDownMirrored](downmirrored.md) — The image has been vertically flipped from the orientation of its original pixel data.
- [UIImageOrientationLeftMirrored](leftmirrored.md) — The image has been rotated 90° clockwise and flipped horizontally from the orientation of its original pixel data.
