---
title: images
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimage/images
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/images'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/images.json'
content_hash: 'sha256:1e1fa8c4f6d71772'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# images

<sub>Instance Property</sub>

The complete array of image objects that compose the animation of an animated object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var images: [UIImage]? { get }
```

## Discussion

For a non-animated image, the value of this property is `nil`.

## See Also

### Getting the image data

- [CGImage](cgimage.md) — The underlying Quartz image data.
- [CIImage](ciimage.md) — The underlying Core Image data.
- [imageAsset](imageasset.md) — The image asset (if any) for the image.
