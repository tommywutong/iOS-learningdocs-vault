---
title: sourceSlice
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4copysparsetexturemappingoperation/sourceslice
source_url: 'https://developer.apple.com/documentation/metal/mtl4copysparsetexturemappingoperation/sourceslice'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4copysparsetexturemappingoperation/sourceslice.json'
content_hash: 'sha256:eb1069b380a0e8ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CopySparseTextureMappingOperation](../mtl4copysparsetexturemappingoperation.md)

# sourceSlice

<sub>Instance Property</sub>

The index of the array slice in the texture source of the copy operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var sourceSlice: Int
```

## Discussion

Provide `0` in this member if the texture type is not an array.
