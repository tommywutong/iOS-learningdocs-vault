---
title: UIImage.Orientation.down
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimage/orientation/down
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/orientation/down'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/orientation/down.json'
content_hash: 'sha256:6fb92f4516c83462'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIImage](../../uiimage.md) · [Orientation](../orientation.md)

# UIImage.Orientation.down

<sub>Case</sub>

The image has been rotated 180° from the orientation of its original pixel data.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
case down
```

## Discussion

If an image is encoded with this orientation, then displayed by software unaware of orientation metadata, the image appears rotated 180°.

![To correct an image with down orientation for display, rotate it 180°.](../../../../../attachments/1530f2c9454d2a3fb9e99de9bee4fe01/media-2948301@2x.png)

## See Also

### Related Documentation

- [CGImagePropertyOrientation.down](../../../imageio/cgimagepropertyorientation/down.md) — The encoded image data is rotated 180° from the image’s intended display orientation.

### Image orientations

- [UIImageOrientationUp](up.md) — The original pixel data matches the image’s intended display orientation.
- [UIImageOrientationLeft](left.md) — The image has been rotated 90° counterclockwise from the orientation of its original pixel data.
- [UIImageOrientationRight](right.md) — The image has been rotated 90° clockwise from the orientation of its original pixel data.
- [UIImageOrientationUpMirrored](upmirrored.md) — The image has been horizontally flipped from the orientation of its original pixel data.
- [UIImageOrientationDownMirrored](downmirrored.md) — The image has been vertically flipped from the orientation of its original pixel data.
- [UIImageOrientationLeftMirrored](leftmirrored.md) — The image has been rotated 90° clockwise and flipped horizontally from the orientation of its original pixel data.
- [UIImageOrientationRightMirrored](rightmirrored.md) — The image has been rotated 90° counterclockwise and flipped horizontally from the orientation of its original pixel data.
