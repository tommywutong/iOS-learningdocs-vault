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
doc_path: /documentation/metal/mtl4updatesparsebuffermappingoperation/mode
source_url: 'https://developer.apple.com/documentation/metal/mtl4updatesparsebuffermappingoperation/mode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4updatesparsebuffermappingoperation/mode.json'
content_hash: 'sha256:c61457ac00745b7a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4UpdateSparseBufferMappingOperation](../mtl4updatesparsebuffermappingoperation.md)

# mode

<sub>Instance Property</sub>

The mode of the mapping operation to perform.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var mode: MTLSparseTextureMappingMode
```

## Discussion

When mode is [MTLSparseTextureMappingModeMap](../mtlsparsetexturemappingmode/map.md), Metal walks the tiles in the range in buffer offset order, assigning the next tile from the heap in increasing order, starting at [heapOffset](heapoffset.md).

When mode is [MTLSparseTextureMappingModeUnmap](../mtlsparsetexturemappingmode/unmap.md), Metal unmaps the tiles in the range, and ignores the value of member [heapOffset](heapoffset.md).
