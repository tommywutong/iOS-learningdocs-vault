---
title: size
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimage/size
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/size'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/size.json'
content_hash: 'sha256:d6815d88d40abbf3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# size

<sub>Instance Property</sub>

The logical dimensions, in points, for the image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var size: CGSize { get }
```

## Discussion

This value reflects the logical size of the image and takes the image’s current orientation into account. Multiply the size values by the value in the [scale](scale.md) property to get the pixel dimensions of the image.

## See Also

### Getting the image size and scale

- [scale](scale.md) — The scale factor of the image.
