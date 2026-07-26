---
title: 'copyAndCompact(sourceAccelerationStructure:destinationAccelerationStructure:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlaccelerationstructurecommandencoder/copyandcompact(sourceaccelerationstructure:destinationaccelerationstructure:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructurecommandencoder/copyandcompact(sourceaccelerationstructure:destinationaccelerationstructure:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructurecommandencoder/copyandcompact%28sourceaccelerationstructure%3Adestinationaccelerationstructure%3A%29.json'
content_hash: 'sha256:278ede8be83e147c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureCommandEncoder](../mtlaccelerationstructurecommandencoder.md)

# copyAndCompact(sourceAccelerationStructure:destinationAccelerationStructure:)

<sub>Instance Method</sub>

Encodes a command to compact an acceleration structure’s data and copy it into a different acceleration structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func copyAndCompact(sourceAccelerationStructure: any MTLAccelerationStructure, destinationAccelerationStructure: any MTLAccelerationStructure)
```

## Parameters

- `sourceAccelerationStructure` — The source acceleration structure.

- `destinationAccelerationStructure` — The destination acceleration structure.

## Discussion

The source and destination acceleration structures can’t overlap in memory. The destination acceleration structure needs to be at least as large as the compact size of the source acceleration structure, which you obtain by using the [- writeCompactedAccelerationStructureSize:toBuffer:offset:](<writecompactedsize(accelerationstructure_buffer_offset_).md>) method.

If the source acceleration structure contains references to other acceleration structures, the copy of the acceleration structure refers to the same child structures.

## See Also

### Copying an acceleration structure

- [- copyAccelerationStructure:toAccelerationStructure:](<copy(sourceaccelerationstructure_destinationaccelerationstructure_).md>) — Encodes a command to copy the data from one acceleration structure to another.
- [- writeCompactedAccelerationStructureSize:toBuffer:offset:](<writecompactedsize(accelerationstructure_buffer_offset_).md>) — Encodes a command to calculate the compacted size of an acceleration structure.
- [- writeCompactedAccelerationStructureSize:toBuffer:offset:sizeDataType:](<writecompactedsize(accelerationstructure_buffer_offset_sizedatatype_).md>) — Encodes a command to calculate the compacted size of an acceleration structure, taking into account the size of the output data.
