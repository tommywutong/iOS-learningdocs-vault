---
title: bounds
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciqrcodefeature/bounds-swift.property
source_url: 'https://developer.apple.com/documentation/coreimage/ciqrcodefeature/bounds-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciqrcodefeature/bounds-swift.property.json'
content_hash: 'sha256:e9c4b19b7aed7d3e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIQRCodeFeature](../ciqrcodefeature.md)

# bounds

<sub>Instance Property</sub>

A rectangle that indicates the position and extent of the QR code feature in image coordinates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var bounds: CGRect { get }
```

## Discussion

This property identifies the rectangular region of the image containing the detected QR code, not necessarily the shape of the QR code. A detected feature is square in space, but may appear as a four-sided polygon in the image. Use the properties listed in `CIQRCodeFeature` to find the corners of the QR code as it appears in perspective.
