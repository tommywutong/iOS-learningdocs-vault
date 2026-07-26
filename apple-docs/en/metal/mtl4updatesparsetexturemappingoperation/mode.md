---
title: mode
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4updatesparsetexturemappingoperation/mode
source_url: 'https://developer.apple.com/documentation/metal/mtl4updatesparsetexturemappingoperation/mode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4updatesparsetexturemappingoperation/mode.json'
content_hash: 'sha256:1d9f245863516100'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4UpdateSparseTextureMappingOperation](../mtl4updatesparsetexturemappingoperation.md)

# mode

<sub>Instance Property</sub>

The mode of the mapping operation to perform.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var mode: MTLSparseTextureMappingMode
```

## Discussion

When mode is [MTLSparseTextureMappingModeMap](../mtlsparsetexturemappingmode/map.md), Metal walks the tiles in the region in X, Y, then Z order, assigning the next tile from the heap in increasing order, starting at [heapOffset](heapoffset.md).

When mode is [MTLSparseTextureMappingModeUnmap](../mtlsparsetexturemappingmode/unmap.md), Metal unmaps the tiles in the region, ignoring the contents of member [heapOffset](heapoffset.md).
