---
title: 'copy(sourceAccelerationStructure:destinationAccelerationStructure:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4computecommandencoder/copy(sourceaccelerationstructure:destinationaccelerationstructure:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4computecommandencoder/copy(sourceaccelerationstructure:destinationaccelerationstructure:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4computecommandencoder/copy%28sourceaccelerationstructure%3Adestinationaccelerationstructure%3A%29.json'
content_hash: 'sha256:772f753a501c7a17'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4ComputeCommandEncoder](../mtl4computecommandencoder.md)

# copy(sourceAccelerationStructure:destinationAccelerationStructure:)

<sub>Instance Method</sub>

Encodes an acceleration structure copy operation into the command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func copy(sourceAccelerationStructure: any MTLAccelerationStructure, destinationAccelerationStructure: any MTLAccelerationStructure)
```

## Parameters

- `sourceAccelerationStructure` — Acceleration structure to copy from.

- `destinationAccelerationStructure` — Acceleration structure to copy to.

## Discussion

You are responsible for ensuring the source and destination acceleration structures don’t overlap in memory. If this is an instance acceleration structure, Metal preserves references to the primitive acceleration structures it references.

Typically, the destination acceleration structure is at least as large as the source acceleration structure, except in cases where you compact the source acceleration structure. In this case, you need to allocate the destination acceleration to be at least as large as the compacted size of the source acceleration structure.

## See Also

### Encoding acceleration structure copy commands

- [- copyAndCompactAccelerationStructure:toAccelerationStructure:](<copyandcompact(sourceaccelerationstructure_destinationaccelerationstructure_).md>) — Encodes a command to copy and compact an acceleration structure.
- [- writeCompactedAccelerationStructureSize:toBuffer:](<writecompactedsize(sourceaccelerationstructure_destinationbuffer_).md>) — Encodes a command to compute the size an acceleration structure can compact into, writing the result into a buffer.
