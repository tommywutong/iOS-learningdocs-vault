---
title: MTLAccelerationStructureCommandEncoder
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructurecommandencoder
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructurecommandencoder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructurecommandencoder.json'
content_hash: 'sha256:af726ed71f9c4beb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLAccelerationStructureCommandEncoder

<sub>Protocol</sub>

Encodes commands that build and refit acceleration structures for a single pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLAccelerationStructureCommandEncoder : MTLCommandEncoder
```

## Overview

Create an acceleration structure encoder by calling one of the factory methods on an [MTLCommandBuffer](mtlcommandbuffer.md) instance, such as [- accelerationStructureCommandEncoder](<mtlcommandbuffer/makeaccelerationstructurecommandencoder().md>).

### Command stages

Most commands apply to one stage within a pass. The following table shows which stage applies to each command:

| Function | MTLStages |
|---|---|
| [- buildAccelerationStructure:descriptor:scratchBuffer:scratchBufferOffset:](<mtlaccelerationstructurecommandencoder/build(accelerationstructure_descriptor_scratchbuffer_scratchbufferoffset_).md>) | [MTLStageAccelerationStructure](mtlstages/accelerationstructure.md) |
| [- copyAccelerationStructure:toAccelerationStructure:](<mtlaccelerationstructurecommandencoder/copy(sourceaccelerationstructure_destinationaccelerationstructure_).md>) | [MTLStageAccelerationStructure](mtlstages/accelerationstructure.md) |
| [- writeCompactedAccelerationStructureSize:toBuffer:offset:](<mtlaccelerationstructurecommandencoder/writecompactedsize(accelerationstructure_buffer_offset_).md>) | [MTLStageAccelerationStructure](mtlstages/accelerationstructure.md) |
| [- writeCompactedAccelerationStructureSize:toBuffer:offset:sizeDataType:](<mtlaccelerationstructurecommandencoder/writecompactedsize(accelerationstructure_buffer_offset_sizedatatype_).md>) | [MTLStageAccelerationStructure](mtlstages/accelerationstructure.md) |
| [- copyAndCompactAccelerationStructure:toAccelerationStructure:](<mtlaccelerationstructurecommandencoder/copyandcompact(sourceaccelerationstructure_destinationaccelerationstructure_).md>) | [MTLStageAccelerationStructure](mtlstages/accelerationstructure.md) |
| [- refitAccelerationStructure:descriptor:destination:scratchBuffer:scratchBufferOffset:](<mtlaccelerationstructurecommandencoder/refit(sourceaccelerationstructure_descriptor_destinationaccelerationstructure_scratchbuffer_scratchbufferoffset_).md>) | [MTLStageAccelerationStructure](mtlstages/accelerationstructure.md) |
| [- refitAccelerationStructure:descriptor:destination:scratchBuffer:scratchBufferOffset:options:](<mtlaccelerationstructurecommandencoder/refit(sourceaccelerationstructure_descriptor_destinationaccelerationstructure_scratchbuffer_scratchbufferoffset_options_).md>) | [MTLStageAccelerationStructure](mtlstages/accelerationstructure.md) |
| [- sampleCountersInBuffer:atSampleIndex:withBarrier:](<mtlaccelerationstructurecommandencoder/samplecounters(samplebuffer_sampleindex_barrier_).md>) | None |

For more information about stages and synchronization, see [MTLStages](mtlstages.md) and [Resource synchronization](resource-synchronization.md).

## Relationships

- **Inherits From**: [MTLCommandEncoder](mtlcommandencoder.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Building an acceleration structure

- [- buildAccelerationStructure:descriptor:scratchBuffer:scratchBufferOffset:](<mtlaccelerationstructurecommandencoder/build(accelerationstructure_descriptor_scratchbuffer_scratchbufferoffset_).md>) — Encodes a command to build a new acceleration structure.

### Copying an acceleration structure

- [- copyAccelerationStructure:toAccelerationStructure:](<mtlaccelerationstructurecommandencoder/copy(sourceaccelerationstructure_destinationaccelerationstructure_).md>) — Encodes a command to copy the data from one acceleration structure to another.
- [- writeCompactedAccelerationStructureSize:toBuffer:offset:](<mtlaccelerationstructurecommandencoder/writecompactedsize(accelerationstructure_buffer_offset_).md>) — Encodes a command to calculate the compacted size of an acceleration structure.
- [- writeCompactedAccelerationStructureSize:toBuffer:offset:sizeDataType:](<mtlaccelerationstructurecommandencoder/writecompactedsize(accelerationstructure_buffer_offset_sizedatatype_).md>) — Encodes a command to calculate the compacted size of an acceleration structure, taking into account the size of the output data.
- [- copyAndCompactAccelerationStructure:toAccelerationStructure:](<mtlaccelerationstructurecommandencoder/copyandcompact(sourceaccelerationstructure_destinationaccelerationstructure_).md>) — Encodes a command to compact an acceleration structure’s data and copy it into a different acceleration structure.

### Refitting an acceleration structure

- [- refitAccelerationStructure:descriptor:destination:scratchBuffer:scratchBufferOffset:](<mtlaccelerationstructurecommandencoder/refit(sourceaccelerationstructure_descriptor_destinationaccelerationstructure_scratchbuffer_scratchbufferoffset_).md>) — Updates an acceleration structure with new geometry or instance data.
- [- refitAccelerationStructure:descriptor:destination:scratchBuffer:scratchBufferOffset:options:](<mtlaccelerationstructurecommandencoder/refit(sourceaccelerationstructure_descriptor_destinationaccelerationstructure_scratchbuffer_scratchbufferoffset_options_).md>) — Updates an acceleration structure with new geometry or instance data, with options that control the refitting process.

### Preventing resource access conflicts

- [- updateFence:](<mtlaccelerationstructurecommandencoder/updatefence(__).md>) — Encodes a command that instructs the GPU to update a fence after the acceleration structure pass completes.
- [- waitForFence:](<mtlaccelerationstructurecommandencoder/waitforfence(__).md>) — Encodes a command that instructs the GPU to pause the acceleration structure pass until another pass updates a fence.

### Making indirect resources resident

- [- useHeap:](<mtlaccelerationstructurecommandencoder/useheap(__).md>) — Makes the resources contained in the specified heap available to the acceleration structure pass.
- [useHeaps(_:)](<mtlaccelerationstructurecommandencoder/useheaps(__).md>) — Makes the resources contained in the specified heaps available to the acceleration structure pass.
- [- useResource:usage:](<mtlaccelerationstructurecommandencoder/useresource(__usage_).md>) — Makes a resource available to the acceleration structure pass.
- [useResources(_:usage:)](<mtlaccelerationstructurecommandencoder/useresources(__usage_).md>) — Makes multiple resources available to the acceleration structure pass.
- [MTLResourceUsage](mtlresourceusage.md) — Options that describe how a graphics or compute function uses an argument buffer’s resource.

### Sampling counters

- [- sampleCountersInBuffer:atSampleIndex:withBarrier:](<mtlaccelerationstructurecommandencoder/samplecounters(samplebuffer_sampleindex_barrier_).md>) — Encodes a command to sample hardware counters at this point in the acceleration structure pass and store the samples into a counter sample buffer.

## See Also

### Acceleration structures

- [Improving ray-tracing data access using per-primitive data](improving-ray-tracing-data-access-using-per-primitive-data.md) — Simplify data access and improve GPU utilization by storing custom primitive data directly in the acceleration structure.
- [MTLAccelerationStructure](mtlaccelerationstructure.md) — A collection of model data for GPU-accelerated intersection of rays with the model.
- [MTL4AccelerationStructureDescriptor](mtl4accelerationstructuredescriptor.md) — Base class for Metal 4 acceleration structure descriptors.
- [MTLAccelerationStructureDescriptor](mtlaccelerationstructuredescriptor.md) — A base class for classes that define the configuration for a new acceleration structure.
- [MTL4PrimitiveAccelerationStructureDescriptor](mtl4primitiveaccelerationstructuredescriptor.md) — Descriptor for a primitive acceleration structure that directly references geometric shapes, such as triangles and bounding boxes.
- [MTLPrimitiveAccelerationStructureDescriptor](mtlprimitiveaccelerationstructuredescriptor.md) — A description of an acceleration structure that contains geometry primitives.
- [MTL4InstanceAccelerationStructureDescriptor](mtl4instanceaccelerationstructuredescriptor.md) — Descriptor for an instance acceleration structure.
- [MTLInstanceAccelerationStructureDescriptor](mtlinstanceaccelerationstructuredescriptor.md) — A description of an acceleration structure that derives from instances of primitive acceleration structures.
- [MTLAccelerationStructureUsage](mtlaccelerationstructureusage.md) — Options that affect how Metal builds an acceleration structure and the behavior of that acceleration structure.
- [MTLAccelerationStructureRefitOptions](mtlaccelerationstructurerefitoptions.md)
