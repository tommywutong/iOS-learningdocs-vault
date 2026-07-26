---
title: dimensions
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltensorreferencetype/dimensions
source_url: 'https://developer.apple.com/documentation/metal/mtltensorreferencetype/dimensions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltensorreferencetype/dimensions.json'
content_hash: 'sha256:5229c457a94b846c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTensorReferenceType](../mtltensorreferencetype.md)

# dimensions

<sub>Instance Property</sub>

The array of sizes, in elements, one for each dimension of this tensor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var dimensions: MTLTensorExtents? { get }
```

## Discussion

For shader-bound tensors with dynamic extents, the [rank](../mtltensorextents/rank.md) of `dimensions` corresponds to the rank the shader function specifies, and [extentAtDimensionIndex:](../mtltensorextents/extentatdimensionindex_.md) always returns a value of -1.
