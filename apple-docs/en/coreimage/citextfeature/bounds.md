---
title: bounds
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/citextfeature/bounds
source_url: 'https://developer.apple.com/documentation/coreimage/citextfeature/bounds'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/citextfeature/bounds.json'
content_hash: 'sha256:c6e80f51c92f630a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CITextFeature](../citextfeature.md)

# bounds

<sub>Instance Property</sub>

A rectangle that indicates the position and extent of the text feature in image coordinates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var bounds: CGRect { get }
```

## Discussion

This property identifies the rectangular region of the image containing the detected text, not necessarily the shape of the text box. A detected feature is rectangular in space, but may appear as a four-sided polygon in the image. Use the properties listed in `CITextFeature` to find the corners of the rectangle as it appears in perspective.
