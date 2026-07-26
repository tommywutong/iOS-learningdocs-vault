---
title: UIImage.Orientation.up
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimage/orientation/up
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/orientation/up'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/orientation/up.json'
content_hash: 'sha256:a81008705f1f707a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIImage](../../uiimage.md) · [Orientation](../orientation.md)

# UIImage.Orientation.up

<sub>Case</sub>

The original pixel data matches the image’s intended display orientation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
case up
```

## Discussion

If an image is encoded with this orientation, then displayed by software unaware of orientation metadata, the image appears correctly “right side up”. That is, this orientation is an identity value.

![An image in up orientation can be presented for display without rotating or flipping.](../../../../../attachments/08b6857053beb92301df7ceb36ab8175/media-2948308@2x.png)

## See Also

### Related Documentation

- [CGImagePropertyOrientation.up](../../../imageio/cgimagepropertyorientation/up.md) — The encoded image data matches the image’s intended display orientation.

### Image orientations

- [UIImageOrientationDown](down.md) — The image has been rotated 180° from the orientation of its original pixel data.
- [UIImageOrientationLeft](left.md) — The image has been rotated 90° counterclockwise from the orientation of its original pixel data.
- [UIImageOrientationRight](right.md) — The image has been rotated 90° clockwise from the orientation of its original pixel data.
- [UIImageOrientationUpMirrored](upmirrored.md) — The image has been horizontally flipped from the orientation of its original pixel data.
- [UIImageOrientationDownMirrored](downmirrored.md) — The image has been vertically flipped from the orientation of its original pixel data.
- [UIImageOrientationLeftMirrored](leftmirrored.md) — The image has been rotated 90° clockwise and flipped horizontally from the orientation of its original pixel data.
- [UIImageOrientationRightMirrored](rightmirrored.md) — The image has been rotated 90° counterclockwise and flipped horizontally from the orientation of its original pixel data.
