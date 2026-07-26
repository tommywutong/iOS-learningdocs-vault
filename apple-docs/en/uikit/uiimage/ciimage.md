---
title: ciImage
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimage/ciimage
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/ciimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/ciimage.json'
content_hash: 'sha256:5b5926b812e3889f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# ciImage

<sub>Instance Property</sub>

The underlying Core Image data.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var ciImage: CIImage? { get }
```

## Discussion

If the `UIImage` object was initialized using a [CGImage](../../coregraphics/cgimage.md), the value of the property is `nil`.

## See Also

### Getting the image data

- [CGImage](cgimage.md) — The underlying Quartz image data.
- [images](images.md) — The complete array of image objects that compose the animation of an animated object.
- [imageAsset](imageasset.md) — The image asset (if any) for the image.
