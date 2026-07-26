---
title: scale
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimage/scale
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/scale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/scale.json'
content_hash: 'sha256:0c1f31cf75a9569c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# scale

<sub>Instance Property</sub>

The scale factor of the image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var scale: CGFloat { get }
```

## Discussion

If you load an image from a file whose name includes the `@2x` modifier, the scale is set to `2.0`. You can also specify an explicit scale factor when initializing an image from a Core Graphics image. All other images are assumed to have a scale factor of `1.0`.

If you multiply the logical size of the image (stored in the [size](size.md) property) by the value in this property, you get the dimensions of the image in pixels.

## See Also

### Getting the image size and scale

- [size](size.md) — The logical dimensions, in points, for the image.
