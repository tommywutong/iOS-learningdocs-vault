---
title: 'writeCompactedSize(accelerationStructure:buffer:offset:sizeDataType:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlaccelerationstructurecommandencoder/writecompactedsize(accelerationstructure:buffer:offset:sizedatatype:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructurecommandencoder/writecompactedsize(accelerationstructure:buffer:offset:sizedatatype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructurecommandencoder/writecompactedsize%28accelerationstructure%3Abuffer%3Aoffset%3Asizedatatype%3A%29.json'
content_hash: 'sha256:f97f46fe1a27a524'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureCommandEncoder](../mtlaccelerationstructurecommandencoder.md)

# writeCompactedSize(accelerationStructure:buffer:offset:sizeDataType:)

<sub>Instance Method</sub>

Encodes a command to calculate the compacted size of an acceleration structure, taking into account the size of the output data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func writeCompactedSize(accelerationStructure: any MTLAccelerationStructure, buffer: any MTLBuffer, offset: Int, sizeDataType: MTLDataType)
```

## Parameters

- `accelerationStructure` — The acceleration structure to measure.

- `buffer` — The buffer to write the size into.

- `offset` — An offset, in bytes, where the GPU should write the result.

- `sizeDataType` — The data type of the resulting data.

## Discussion

The GPU writes the compacted size to the buffer, in bytes, using the `sizeDataType` parameter to determine the size of the output data. The compacted size may be smaller than the source acceleration structure.

To compact an acceleration structure, encode a command to get the minimum size. After the command completes, read the size from the buffer and allocate a new acceleration structure with at least that much storage. Then create another encoder and call the  [- copyAndCompactAccelerationStructure:toAccelerationStructure:](<copyandcompact(sourceaccelerationstructure_destinationaccelerationstructure_).md>) method to copy it into the new structure.

## See Also

### Copying an acceleration structure

- [- copyAccelerationStructure:toAccelerationStructure:](<copy(sourceaccelerationstructure_destinationaccelerationstructure_).md>) — Encodes a command to copy the data from one acceleration structure to another.
- [- writeCompactedAccelerationStructureSize:toBuffer:offset:](<writecompactedsize(accelerationstructure_buffer_offset_).md>) — Encodes a command to calculate the compacted size of an acceleration structure.
- [- copyAndCompactAccelerationStructure:toAccelerationStructure:](<copyandcompact(sourceaccelerationstructure_destinationaccelerationstructure_).md>) — Encodes a command to compact an acceleration structure’s data and copy it into a different acceleration structure.
