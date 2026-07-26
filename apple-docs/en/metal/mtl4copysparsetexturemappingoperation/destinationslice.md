---
title: destinationSlice
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4copysparsetexturemappingoperation/destinationslice
source_url: 'https://developer.apple.com/documentation/metal/mtl4copysparsetexturemappingoperation/destinationslice'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4copysparsetexturemappingoperation/destinationslice.json'
content_hash: 'sha256:c550458098179f9c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CopySparseTextureMappingOperation](../mtl4copysparsetexturemappingoperation.md)

# destinationSlice

<sub>Instance Property</sub>

The index of the array slice in the destination texture to copy into.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var destinationSlice: Int
```

## Discussion

Provide `0` in this member if the texture type is not an array.
