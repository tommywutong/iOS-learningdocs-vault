---
title: UIImage.Orientation.downMirrored
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimage/orientation/downmirrored
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/orientation/downmirrored'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/orientation/downmirrored.json'
content_hash: 'sha256:f737090e93e99422'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIImage](../../uiimage.md) · [Orientation](../orientation.md)

# UIImage.Orientation.downMirrored

<sub>Case</sub>

The image has been vertically flipped from the orientation of its original pixel data.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
case downMirrored
```

## Discussion

If an image is encoded with this orientation, then displayed by software unaware of orientation metadata, the image appears vertically flipped. (Alternatively, the image is rotated 180° and then flipped horizontally.)

![To correct an image with downMirrored orientation for display, flip it vertically.](../../../../../attachments/8170a1cc20c32b7a29544fc6e92a7f74/media-2948309@2x.png)

## See Also

### Related Documentation

- [CGImagePropertyOrientation.downMirrored](../../../imageio/cgimagepropertyorientation/downmirrored.md) — The encoded image data is vertically flipped from the image’s intended display orientation.

### Image orientations

- [UIImageOrientationUp](up.md) — The original pixel data matches the image’s intended display orientation.
- [UIImageOrientationDown](down.md) — The image has been rotated 180° from the orientation of its original pixel data.
- [UIImageOrientationLeft](left.md) — The image has been rotated 90° counterclockwise from the orientation of its original pixel data.
- [UIImageOrientationRight](right.md) — The image has been rotated 90° clockwise from the orientation of its original pixel data.
- [UIImageOrientationUpMirrored](upmirrored.md) — The image has been horizontally flipped from the orientation of its original pixel data.
- [UIImageOrientationLeftMirrored](leftmirrored.md) — The image has been rotated 90° clockwise and flipped horizontally from the orientation of its original pixel data.
- [UIImageOrientationRightMirrored](rightmirrored.md) — The image has been rotated 90° counterclockwise and flipped horizontally from the orientation of its original pixel data.
