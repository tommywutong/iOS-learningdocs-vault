---
title: bounds
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifeature/bounds
source_url: 'https://developer.apple.com/documentation/coreimage/cifeature/bounds'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifeature/bounds.json'
content_hash: 'sha256:03a92bb70f4b31ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFeature](../cifeature.md)

# bounds

<sub>Instance Property</sub>

The rectangle that holds discovered feature.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var bounds: CGRect { get }
```

## Discussion

The rectangle is in the coordinate system of the image.

## See Also

### Feature Properties

- [type](type.md) — The type of feature that was discovered.
