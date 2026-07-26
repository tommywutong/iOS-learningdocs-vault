---
title: 'copyAndCompact(sourceAccelerationStructure:destinationAccelerationStructure:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4computecommandencoder/copyandcompact(sourceaccelerationstructure:destinationaccelerationstructure:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4computecommandencoder/copyandcompact(sourceaccelerationstructure:destinationaccelerationstructure:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4computecommandencoder/copyandcompact%28sourceaccelerationstructure%3Adestinationaccelerationstructure%3A%29.json'
content_hash: 'sha256:cba523294f758e1f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4ComputeCommandEncoder](../mtl4computecommandencoder.md)

# copyAndCompact(sourceAccelerationStructure:destinationAccelerationStructure:)

<sub>Instance Method</sub>

Encodes a command to copy and compact an acceleration structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func copyAndCompact(sourceAccelerationStructure: any MTLAccelerationStructure, destinationAccelerationStructure: any MTLAccelerationStructure)
```

## Parameters

- `sourceAccelerationStructure` — Acceleration structure to copy and compact.

- `destinationAccelerationStructure` — Acceleration structure to copy to.

## Discussion

You are responsible for ensuring that the source and destination acceleration structures don’t overlap in memory. If this is an instance acceleration structure, Metal preserves references to primitive acceleration structures it references.

This operation requires that the destination acceleration structure is at least as large as the compacted size of the source acceleration structure. You can compute this size by calling the [- writeCompactedAccelerationStructureSize:toBuffer:](<writecompactedsize(sourceaccelerationstructure_destinationbuffer_).md>) method.

## See Also

### Encoding acceleration structure copy commands

- [- copyAccelerationStructure:toAccelerationStructure:](<copy(sourceaccelerationstructure_destinationaccelerationstructure_).md>) — Encodes an acceleration structure copy operation into the command buffer.
- [- writeCompactedAccelerationStructureSize:toBuffer:](<writecompactedsize(sourceaccelerationstructure_destinationbuffer_).md>) — Encodes a command to compute the size an acceleration structure can compact into, writing the result into a buffer.
