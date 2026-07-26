---
title: imageAsset
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimage/imageasset
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/imageasset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/imageasset.json'
content_hash: 'sha256:6c57467d7f210bd6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# imageAsset

<sub>Instance Property</sub>

The image asset (if any) for the image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var imageAsset: UIImageAsset? { get }
```

## Discussion

For images loaded from an image assets, this property contains an image asset object that you can use to fetch the other variants of the image. If you did not create the image object using an image asset, the value of this property is `nil`. This property is always `nil` for images created using a [CIImage](ciimage.md) object.

## See Also

### Getting the image data

- [CGImage](cgimage.md) — The underlying Quartz image data.
- [CIImage](ciimage.md) — The underlying Core Image data.
- [images](images.md) — The complete array of image objects that compose the animation of an animated object.
