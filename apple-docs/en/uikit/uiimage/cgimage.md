---
title: cgImage
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimage/cgimage
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/cgimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/cgimage.json'
content_hash: 'sha256:c6637bf394c1f082'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# cgImage

<sub>Instance Property</sub>

The underlying Quartz image data.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var cgImage: CGImage? { get }
```

## Discussion

If the image data has been purged because of memory constraints, invoking this method forces that data to be loaded back into memory. Reloading the image data may incur a performance penalty.

If the `UIImage` object was initialized using a `CIImage` object, the value of the property is `NULL`.

## See Also

### Getting the image data

- [CIImage](ciimage.md) — The underlying Core Image data.
- [images](images.md) — The complete array of image objects that compose the animation of an animated object.
- [imageAsset](imageasset.md) — The image asset (if any) for the image.
