---
title: UIImage.Orientation.right
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimage/orientation/right
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/orientation/right'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/orientation/right.json'
content_hash: 'sha256:b5d48fe6f57d0336'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIImage](../../uiimage.md) · [Orientation](../orientation.md)

# UIImage.Orientation.right

<sub>Case</sub>

The image has been rotated 90° clockwise from the orientation of its original pixel data.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
case right
```

## Discussion

If an image is encoded with this orientation, then displayed by software unaware of orientation metadata, the image appears to be rotated 90° counter-clockwise. (That is, to present the image in its intended orientation, you must rotate it 90° clockwise.)

![To correct an image with right orientation for display, rotate it 90° clockwise.](../../../../../attachments/a4de8a358cbf9a76800cc595fceb8892/media-2948303@2x.png)

## See Also

### Related Documentation

- [CGImagePropertyOrientation.right](../../../imageio/cgimagepropertyorientation/right.md) — The encoded image data is rotated 90° counter-clockwise from the image’s intended display orientation.

### Image orientations

- [UIImageOrientationUp](up.md) — The original pixel data matches the image’s intended display orientation.
- [UIImageOrientationDown](down.md) — The image has been rotated 180° from the orientation of its original pixel data.
- [UIImageOrientationLeft](left.md) — The image has been rotated 90° counterclockwise from the orientation of its original pixel data.
- [UIImageOrientationUpMirrored](upmirrored.md) — The image has been horizontally flipped from the orientation of its original pixel data.
- [UIImageOrientationDownMirrored](downmirrored.md) — The image has been vertically flipped from the orientation of its original pixel data.
- [UIImageOrientationLeftMirrored](leftmirrored.md) — The image has been rotated 90° clockwise and flipped horizontally from the orientation of its original pixel data.
- [UIImageOrientationRightMirrored](rightmirrored.md) — The image has been rotated 90° counterclockwise and flipped horizontally from the orientation of its original pixel data.
