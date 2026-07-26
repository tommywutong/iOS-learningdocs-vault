---
title: 'copy(sourceAccelerationStructure:destinationAccelerationStructure:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlaccelerationstructurecommandencoder/copy(sourceaccelerationstructure:destinationaccelerationstructure:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructurecommandencoder/copy(sourceaccelerationstructure:destinationaccelerationstructure:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructurecommandencoder/copy%28sourceaccelerationstructure%3Adestinationaccelerationstructure%3A%29.json'
content_hash: 'sha256:d6d93c415f82df4b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureCommandEncoder](../mtlaccelerationstructurecommandencoder.md)

# copy(sourceAccelerationStructure:destinationAccelerationStructure:)

<sub>Instance Method</sub>

Encodes a command to copy the data from one acceleration structure to another.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func copy(sourceAccelerationStructure: any MTLAccelerationStructure, destinationAccelerationStructure: any MTLAccelerationStructure)
```

## Parameters

- `sourceAccelerationStructure` — The source acceleration structure.

- `destinationAccelerationStructure` — The destination acceleration structure.

## Discussion

The destination acceleration structure needs to be at least as large as the source acceleration structure, unless you’re compacting the source acceleration structure. In that case, the destination acceleration structure needs be at least as large as the compact size of the source acceleration structure.

If the source acceleration structure contains references to other acceleration structures, the copy of the acceleration structure also refers to the same child structures.

## See Also

### Copying an acceleration structure

- [- writeCompactedAccelerationStructureSize:toBuffer:offset:](<writecompactedsize(accelerationstructure_buffer_offset_).md>) — Encodes a command to calculate the compacted size of an acceleration structure.
- [- writeCompactedAccelerationStructureSize:toBuffer:offset:sizeDataType:](<writecompactedsize(accelerationstructure_buffer_offset_sizedatatype_).md>) — Encodes a command to calculate the compacted size of an acceleration structure, taking into account the size of the output data.
- [- copyAndCompactAccelerationStructure:toAccelerationStructure:](<copyandcompact(sourceaccelerationstructure_destinationaccelerationstructure_).md>) — Encodes a command to compact an acceleration structure’s data and copy it into a different acceleration structure.
