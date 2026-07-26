---
title: UIImage.Orientation.upMirrored
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimage/orientation/upmirrored
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/orientation/upmirrored'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/orientation/upmirrored.json'
content_hash: 'sha256:9ffefd7cf29a788c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIImage](../../uiimage.md) · [Orientation](../orientation.md)

# UIImage.Orientation.upMirrored

<sub>Case</sub>

The image has been horizontally flipped from the orientation of its original pixel data.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
case upMirrored
```

## Discussion

If an image is encoded with this orientation, then displayed by software unaware of orientation metadata, the image appears horizontally mirrored.

![To correct an image with upMirrored orientation for display, flip it horizontally.](../../../../../attachments/3b93501e18e409bc3d6f779ae1e59673/media-2948304@2x.png)

## See Also

### Related Documentation

- [CGImagePropertyOrientation.upMirrored](../../../imageio/cgimagepropertyorientation/upmirrored.md) — The encoded image data is horizontally flipped from the image’s intended display orientation.

### Image orientations

- [UIImageOrientationUp](up.md) — The original pixel data matches the image’s intended display orientation.
- [UIImageOrientationDown](down.md) — The image has been rotated 180° from the orientation of its original pixel data.
- [UIImageOrientationLeft](left.md) — The image has been rotated 90° counterclockwise from the orientation of its original pixel data.
- [UIImageOrientationRight](right.md) — The image has been rotated 90° clockwise from the orientation of its original pixel data.
- [UIImageOrientationDownMirrored](downmirrored.md) — The image has been vertically flipped from the orientation of its original pixel data.
- [UIImageOrientationLeftMirrored](leftmirrored.md) — The image has been rotated 90° clockwise and flipped horizontally from the orientation of its original pixel data.
- [UIImageOrientationRightMirrored](rightmirrored.md) — The image has been rotated 90° counterclockwise and flipped horizontally from the orientation of its original pixel data.
