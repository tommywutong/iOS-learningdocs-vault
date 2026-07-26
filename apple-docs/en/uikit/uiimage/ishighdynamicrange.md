---
title: isHighDynamicRange
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimage/ishighdynamicrange
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/ishighdynamicrange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/ishighdynamicrange.json'
content_hash: 'sha256:577dca7d27b7a0e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# isHighDynamicRange

<sub>Instance Property</sub>

Indicates that this image is tagged for display of high dynamic range content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var isHighDynamicRange: Bool { get }
```

## See Also

### Specifying the dynamic range

- [- imageRestrictedToStandardDynamicRange](<imagerestrictedtostandarddynamicrange().md>) — Returns a new image that will render within the standard range.
- [UIImageHEICRepresentation](<heicdata().md>) — Returns HEIC data representing the image, or nil if such a representation could not be generated. HEIC is recommended for efficiently storing all kinds of images, including those with high dynamic range content.
- [DynamicRange](dynamicrange.md)
