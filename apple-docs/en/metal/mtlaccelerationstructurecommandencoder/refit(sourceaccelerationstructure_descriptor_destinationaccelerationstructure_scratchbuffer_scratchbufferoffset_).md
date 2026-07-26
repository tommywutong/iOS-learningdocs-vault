---
title: 'refit(sourceAccelerationStructure:descriptor:destinationAccelerationStructure:scratchBuffer:scratchBufferOffset:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlaccelerationstructurecommandencoder/refit(sourceaccelerationstructure:descriptor:destinationaccelerationstructure:scratchbuffer:scratchbufferoffset:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructurecommandencoder/refit(sourceaccelerationstructure:descriptor:destinationaccelerationstructure:scratchbuffer:scratchbufferoffset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructurecommandencoder/refit%28sourceaccelerationstructure%3Adescriptor%3Adestinationaccelerationstructure%3Ascratchbuffer%3Ascratchbufferoffset%3A%29.json'
content_hash: 'sha256:65bb7709df8acf48'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureCommandEncoder](../mtlaccelerationstructurecommandencoder.md)

# refit(sourceAccelerationStructure:descriptor:destinationAccelerationStructure:scratchBuffer:scratchBufferOffset:)

<sub>Instance Method</sub>

Updates an acceleration structure with new geometry or instance data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func refit(sourceAccelerationStructure: any MTLAccelerationStructure, descriptor: MTLAccelerationStructureDescriptor, destinationAccelerationStructure: (any MTLAccelerationStructure)?, scratchBuffer: (any MTLBuffer)?, scratchBufferOffset: Int)
```

## Parameters

- `sourceAccelerationStructure` — The source acceleration structure.

- `descriptor` — A description of the updated acceleration structure.

- `destinationAccelerationStructure` — The destination to write the new acceleration structure to. Pass the same acceleration structure or `nil` to refit the structure in place.

- `scratchBuffer` — A buffer used to hold data while building the acceleration structure. Pass `nil` if [refitScratchBufferSize](../mtlaccelerationstructuresizes/refitscratchbuffersize.md) returns zero.

- `scratchBufferOffset` — An offset, in bytes, in the scratch buffer where the scratch memory starts.

## Discussion

Use refitting to update an acceleration structure when you make small changes to the underlying geometry. Refitting performs much faster than rebuilding an acceleration structure from scratch. However, ray-tracing performance may degrade, based on how many changes you make to the geometry data.

You can’t use refitting to add or remove geometry in the acceleration structure.

If the source and destination acceleration structures aren’t the same, they can’t overlap in memory. The destination acceleration structure and the scratch buffer need to have enough space in memory to hold the acceleration structure data. Get the minimum amount of space it needs by calling the [- accelerationStructureSizesWithDescriptor:](<../mtldevice/accelerationstructuresizes(descriptor_).md>) method of the Metal device instance. If you’re compacting the source structure, the destination needs to be at least as large as the compact size of the source acceleration structure.

## See Also

### Refitting an acceleration structure

- [- refitAccelerationStructure:descriptor:destination:scratchBuffer:scratchBufferOffset:options:](<refit(sourceaccelerationstructure_descriptor_destinationaccelerationstructure_scratchbuffer_scratchbufferoffset_options_).md>) — Updates an acceleration structure with new geometry or instance data, with options that control the refitting process.
