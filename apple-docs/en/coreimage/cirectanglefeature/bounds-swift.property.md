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
doc_path: /documentation/coreimage/cirectanglefeature/bounds-swift.property
source_url: 'https://developer.apple.com/documentation/coreimage/cirectanglefeature/bounds-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cirectanglefeature/bounds-swift.property.json'
content_hash: 'sha256:6b462b72fcec04bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIRectangleFeature](../cirectanglefeature.md)

# bounds

<sub>Instance Property</sub>

A rectangle indicating the position and extent of the feature in image coordinates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var bounds: CGRect { get }
```

## Discussion

This property identifies the rectangular region _of the image_ containing the detected rectangle, not necessarily the shape of the rectangle. A detected feature is rectangular in space, but may appear in perspective in the image. Use the properties listed in [CIRectangleFeature](../cirectanglefeature.md) to find the corners of the rectangle as it appears in perspective.
