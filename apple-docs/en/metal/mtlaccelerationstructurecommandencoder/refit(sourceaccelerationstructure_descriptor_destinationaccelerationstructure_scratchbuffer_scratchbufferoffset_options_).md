---
title: 'refit(sourceAccelerationStructure:descriptor:destinationAccelerationStructure:scratchBuffer:scratchBufferOffset:options:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlaccelerationstructurecommandencoder/refit(sourceaccelerationstructure:descriptor:destinationaccelerationstructure:scratchbuffer:scratchbufferoffset:options:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructurecommandencoder/refit(sourceaccelerationstructure:descriptor:destinationaccelerationstructure:scratchbuffer:scratchbufferoffset:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructurecommandencoder/refit%28sourceaccelerationstructure%3Adescriptor%3Adestinationaccelerationstructure%3Ascratchbuffer%3Ascratchbufferoffset%3Aoptions%3A%29.json'
content_hash: 'sha256:4f628a7683fd2e15'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureCommandEncoder](../mtlaccelerationstructurecommandencoder.md)

# refit(sourceAccelerationStructure:descriptor:destinationAccelerationStructure:scratchBuffer:scratchBufferOffset:options:)

<sub>Instance Method</sub>

Updates an acceleration structure with new geometry or instance data, with options that control the refitting process.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func refit(sourceAccelerationStructure: any MTLAccelerationStructure, descriptor: MTLAccelerationStructureDescriptor, destinationAccelerationStructure: (any MTLAccelerationStructure)?, scratchBuffer: (any MTLBuffer)?, scratchBufferOffset: Int, options: MTLAccelerationStructureRefitOptions = [])
```

## Parameters

- `sourceAccelerationStructure` — The source acceleration structure.

- `descriptor` — A description of the updated acceleration structure.

- `destinationAccelerationStructure` — The destination to write the new acceleration structure to. Pass the same acceleration structure or `nil` to refit the structure in place.

- `scratchBuffer` — A buffer used to hold data while building the acceleration structure. Pass `nil` if [refitScratchBufferSize](../mtlaccelerationstructuresizes/refitscratchbuffersize.md) returns zero.

- `scratchBufferOffset` — An offset, in bytes, in the scratch buffer where the scratch memory starts.

- `options` — Options that control the refitting process.

## Discussion

Use refitting to update an acceleration structure when you make small changes to the underlying geometry. Refitting performs much faster than rebuilding an acceleration structure from scratch. However, ray-tracing performance may degrade, based on how many changes you make to the geometry data.

You can’t use refitting to add or remove geometry in the acceleration structure.

If the source and destination acceleration structures are not the same, they need to avoid overlapping in memory. The destination acceleration structure and the scratch buffer need to have enough space in memory to hold the acceleration structure data. Call the [- accelerationStructureSizesWithDescriptor:](<../mtldevice/accelerationstructuresizes(descriptor_).md>) method on the Metal device object to get the required space. If you compact the source structure, the destination needs to be at least as large as the compacted size of the source acceleration structure.

## See Also

### Refitting an acceleration structure

- [- refitAccelerationStructure:descriptor:destination:scratchBuffer:scratchBufferOffset:](<refit(sourceaccelerationstructure_descriptor_destinationaccelerationstructure_scratchbuffer_scratchbufferoffset_).md>) — Updates an acceleration structure with new geometry or instance data.
