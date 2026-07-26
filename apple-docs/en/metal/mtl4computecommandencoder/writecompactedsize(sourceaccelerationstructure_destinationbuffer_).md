---
title: 'writeCompactedSize(sourceAccelerationStructure:destinationBuffer:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4computecommandencoder/writecompactedsize(sourceaccelerationstructure:destinationbuffer:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4computecommandencoder/writecompactedsize(sourceaccelerationstructure:destinationbuffer:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4computecommandencoder/writecompactedsize%28sourceaccelerationstructure%3Adestinationbuffer%3A%29.json'
content_hash: 'sha256:c451b6a5734ea0a0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4ComputeCommandEncoder](../mtl4computecommandencoder.md)

# writeCompactedSize(sourceAccelerationStructure:destinationBuffer:)

<sub>Instance Method</sub>

Encodes a command to compute the size an acceleration structure can compact into, writing the result into a buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func writeCompactedSize(sourceAccelerationStructure accelerationStructure: any MTLAccelerationStructure, destinationBuffer buffer: MTL4BufferRange)
```

## Parameters

- `accelerationStructure` — Source acceleration structure.

- `buffer` — Destination size buffer. Metal writes the compacted size as a 64-bit unsigned integer value, representing the compacted size in bytes.

## Discussion

This size is potentially smaller than the acceleration structure. To perform compaction, you typically read this size from the buffer once the command buffer completes. You then use it to allocate a new, potentially smaller acceleration structure. Finally, you call the [- copyAndCompactAccelerationStructure:toAccelerationStructure:](<copyandcompact(sourceaccelerationstructure_destinationaccelerationstructure_).md>) method to perform the copy.

## See Also

### Encoding acceleration structure copy commands

- [- copyAccelerationStructure:toAccelerationStructure:](<copy(sourceaccelerationstructure_destinationaccelerationstructure_).md>) — Encodes an acceleration structure copy operation into the command buffer.
- [- copyAndCompactAccelerationStructure:toAccelerationStructure:](<copyandcompact(sourceaccelerationstructure_destinationaccelerationstructure_).md>) — Encodes a command to copy and compact an acceleration structure.
