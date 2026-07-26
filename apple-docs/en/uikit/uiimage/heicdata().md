---
title: heicData()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimage/heicdata()
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/heicdata()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/heicdata%28%29.json'
content_hash: 'sha256:4bdb3bfd905a096f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# heicData()

<sub>Instance Method</sub>

Returns HEIC data representing the image, or nil if such a representation could not be generated. HEIC is recommended for efficiently storing all kinds of images, including those with high dynamic range content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func heicData() -> Data?
```

## See Also

### Specifying the dynamic range

- [isHighDynamicRange](ishighdynamicrange.md) — Indicates that this image is tagged for display of high dynamic range content.
- [- imageRestrictedToStandardDynamicRange](<imagerestrictedtostandarddynamicrange().md>) — Returns a new image that will render within the standard range.
- [DynamicRange](dynamicrange.md)
