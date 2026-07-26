---
title: imageRestrictedToStandardDynamicRange()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimage/imagerestrictedtostandarddynamicrange()
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/imagerestrictedtostandarddynamicrange()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/imagerestrictedtostandarddynamicrange%28%29.json'
content_hash: 'sha256:24b27b8d332d1731'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# imageRestrictedToStandardDynamicRange()

<sub>Instance Method</sub>

Returns a new image that will render within the standard range.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func imageRestrictedToStandardDynamicRange() -> UIImage
```

## See Also

### Specifying the dynamic range

- [isHighDynamicRange](ishighdynamicrange.md) — Indicates that this image is tagged for display of high dynamic range content.
- [UIImageHEICRepresentation](<heicdata().md>) — Returns HEIC data representing the image, or nil if such a representation could not be generated. HEIC is recommended for efficiently storing all kinds of images, including those with high dynamic range content.
- [DynamicRange](dynamicrange.md)
