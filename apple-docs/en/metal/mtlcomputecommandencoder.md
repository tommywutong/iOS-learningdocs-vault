---
title: MTLComputeCommandEncoder
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcomputecommandencoder
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputecommandencoder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputecommandencoder.json'
content_hash: 'sha256:c26d59cb9687ab39'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLComputeCommandEncoder

<sub>Protocol</sub>

Encodes computation dispatch commands for a single compute pass into a command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLComputeCommandEncoder : MTLCommandEncoder
```

## Overview

Create a compute encoder by calling one of the factory methods on an [MTLCommandBuffer](mtlcommandbuffer.md) instance, such as [- computeCommandEncoderWithDispatchType:](<mtlcommandbuffer/makecomputecommandencoder(dispatchtype_).md>). You can encode multiple commands that each run a compute kernel as part of a single pass of the encoder with the following steps:

1. Configure an [MTLComputePipelineState](mtlcomputepipelinestate.md) instance with a kernel, using a method such as [- newComputePipelineStateWithFunction:error:](<mtldevice/makecomputepipelinestate(function_).md>). See the [Creating compute pipeline states](pipeline-state-creation.md#Creating-compute-pipeline-states) section of [Pipeline state creation](pipeline-state-creation.md) for all [MTLDevice](mtldevice.md) methods that create a new pipeline state for your command encoder.
2. Set the pipeline state with the [- setComputePipelineState:](<mtlcomputecommandencoder/setcomputepipelinestate(__).md>) method on your command encoder.
3. Set kernel arguments by binding buffers, textures, and other resources with methods such as [- setBuffer:offset:atIndex:](<mtlcomputecommandencoder/setbuffer(__offset_index_).md>) and [- setTexture:atIndex:](<mtlcomputecommandencoder/settexture(__index_).md>).
4. Encode compute commands that call your kernel by either [Dispatching kernel calls directly](mtlcomputecommandencoder.md#Dispatching-kernel-calls-directly) or [Dispatching from indirect command buffers](mtlcomputecommandencoder.md#Dispatching-from-indirect-command-buffers).
5. Call [- endEncoding](<mtlcommandencoder/endencoding().md>) to finish encoding the kernel call of the compute pass.

### Command stages

Most compute commands apply to one stage within a pass. The following table shows which stage applies to each command:

| Function | MTLStages |
|---|---|
| [- dispatchThreads:threadsPerThreadgroup:](<mtlcomputecommandencoder/dispatchthreads(__threadsperthreadgroup_).md>) | [MTLStageDispatch](mtlstages/dispatch.md) |
| [- dispatchThreadgroups:threadsPerThreadgroup:](<mtlcomputecommandencoder/dispatchthreadgroups(__threadsperthreadgroup_).md>) | [MTLStageDispatch](mtlstages/dispatch.md) |
| [- dispatchThreadgroupsWithIndirectBuffer:indirectBufferOffset:threadsPerThreadgroup:](<mtlcomputecommandencoder/dispatchthreadgroups(indirectbuffer_indirectbufferoffset_threadsperthreadgroup_).md>) | [MTLStageDispatch](mtlstages/dispatch.md) |
| [executeCommandsInBuffer(_:range:)](<mtlcomputecommandencoder/executecommandsinbuffer(__range_).md>)![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[executeCommandsInBuffer:withRange:](mtlcomputecommandencoder/executecommandsinbuffer_withrange_.md) | None |
| [executeCommandsInBuffer(_:indirectBuffer:offset:)](<mtlcomputecommandencoder/executecommandsinbuffer(__indirectbuffer_offset_).md>)![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[executeCommandsInBuffer:indirectBuffer:indirectBufferOffset:](mtlcomputecommandencoder/executecommandsinbuffer_indirectbuffer_indirectbufferoffset_.md) | None |
| [- sampleCountersInBuffer:atSampleIndex:withBarrier:](<mtlcomputecommandencoder/samplecounters(samplebuffer_sampleindex_barrier_).md>) | None |

The [executeCommandsInBuffer(_:range:)](<mtlcomputecommandencoder/executecommandsinbuffer(__range_).md>) and [executeCommandsInBuffer(_:indirectBuffer:offset:)](<mtlcomputecommandencoder/executecommandsinbuffer(__indirectbuffer_offset_).md>) commands don’t apply to any stage, which means you can’t use a barrier to wait for all commands in an indirect command buffer to complete. However, each command within the [MTLIndirectCommandBuffer](mtlindirectcommandbuffer.md) applies to the same stages as when you encode the equivalent command directly.

For more information about stages and synchronization, see [MTLStages](mtlstages.md) and [Resource synchronization](resource-synchronization.md).

## Relationships

- **Inherits From**: [MTLCommandEncoder](mtlcommandencoder.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Configuring the pipeline state

- [- setComputePipelineState:](<mtlcomputecommandencoder/setcomputepipelinestate(__).md>) — Configures the compute encoder with a pipeline state for subsequent kernel calls.
- [dispatchType](mtlcomputecommandencoder/dispatchtype.md) — The dispatch type to use when submitting compute work to the GPU.

### Binding buffers

- [- setBuffer:offset:atIndex:](<mtlcomputecommandencoder/setbuffer(__offset_index_).md>) — Binds a buffer to the buffer argument table, allowing compute kernels to access its data on the GPU.
- [- setBuffer:offset:attributeStride:atIndex:](<mtlcomputecommandencoder/setbuffer(__offset_attributestride_index_).md>) — Binds a buffer with a stride to the buffer argument table, allowing compute kernels to access its data on the GPU.
- [setBuffers(_:offsets:range:)](<mtlcomputecommandencoder/setbuffers(__offsets_range_).md>) — Binds multiple buffers to the buffer argument table at once, allowing compute kernels to access their data on the GPU.
- [setBuffers(_:offsets:attributeStrides:range:)](<mtlcomputecommandencoder/setbuffers(__offsets_attributestrides_range_).md>) — Binds multiple buffers with data in stride to the buffer argument table at once, allowing compute kernels to access their data on the GPU.
- [- setBufferOffset:atIndex:](<mtlcomputecommandencoder/setbufferoffset(__index_).md>) — Changes where the data begins in a buffer already bound to the buffer argument table.
- [- setBufferOffset:attributeStride:atIndex:](<mtlcomputecommandencoder/setbufferoffset(offset_attributestride_index_).md>) — Changes where the data begins and the distance between adjacent elements in a buffer already bound to the buffer argument table.

### Binding raw bytes

- [- setBytes:length:atIndex:](<mtlcomputecommandencoder/setbytes(__length_index_).md>) — Copies data directly to the GPU to populate an entry in the buffer argument table.
- [- setBytes:length:attributeStride:atIndex:](<mtlcomputecommandencoder/setbytes(__length_attributestride_index_).md>) — Copies data with a given stride directly to the GPU to populate an entry in the buffer argument table.

### Binding textures

- [- setTexture:atIndex:](<mtlcomputecommandencoder/settexture(__index_).md>) — Binds a texture to the texture argument table, allowing compute kernels to access its data on the GPU.
- [setTextures(_:range:)](<mtlcomputecommandencoder/settextures(__range_).md>) — Binds multiple textures to the texture argument table, allowing compute functions to access their data on the GPU.

### Binding texture samplers

- [- setSamplerState:atIndex:](<mtlcomputecommandencoder/setsamplerstate(__index_).md>) — Encodes a texture sampler, allowing compute kernels to use it for sampling textures on the GPU.
- [- setSamplerState:lodMinClamp:lodMaxClamp:atIndex:](<mtlcomputecommandencoder/setsamplerstate(__lodminclamp_lodmaxclamp_index_).md>) — Encodes a texture sampler with a custom level of detail clamping, allowing compute kernels to use it for sampling textures on the GPU.
- [setSamplerStates(_:range:)](<mtlcomputecommandencoder/setsamplerstates(__range_).md>) — Encodes multiple texture samplers to the sampler argument table, allowing compute kernels to use them for sampling textures on the GPU.
- [setSamplerStates(_:lodMinClamps:lodMaxClamps:range:)](<mtlcomputecommandencoder/setsamplerstates(__lodminclamps_lodmaxclamps_range_).md>) — Encodes multiple texture samplers for the compute function, specifying clamp values for the level of detail of each sampler.

### Binding function tables

- [- setVisibleFunctionTable:atBufferIndex:](<mtlcomputecommandencoder/setvisiblefunctiontable(__bufferindex_).md>) — Binds a visible function table to the buffer argument table, allowing you to call its functions on the GPU.
- [setVisibleFunctionTables(_:bufferRange:)](<mtlcomputecommandencoder/setvisiblefunctiontables(__bufferrange_).md>) — Binds multiple visible function tables to the buffer argument table, allowing you to call their functions on the GPU.
- [setIntersectionFunctionTables(_:bufferRange:)](<mtlcomputecommandencoder/setintersectionfunctiontables(__bufferrange_).md>) — Binds multiple intersection function tables to the buffer argument table, allowing you to call their functions on the GPU.

### Binding arguments for acceleration structures

- [- setAccelerationStructure:atBufferIndex:](<mtlcomputecommandencoder/setaccelerationstructure(__bufferindex_).md>) — Binds an acceleration structure to the buffer argument table, allowing functions to access it on the GPU.
- [- setIntersectionFunctionTable:atBufferIndex:](<mtlcomputecommandencoder/setintersectionfunctiontable(__bufferindex_).md>) — Binds an intersection function table to the buffer argument table, making it callable in your Metal shaders.

### Making indirect resources resident

- [- useResource:usage:](<mtlcomputecommandencoder/useresource(__usage_).md>) — Ensures kernel calls that the system encodes in subsequent commands have access to a resource.
- [useResources(_:usage:)](<mtlcomputecommandencoder/useresources(__usage_).md>) — Ensures kernel calls that the system encodes in subsequent commands have access to multiple resources.
- [- useHeap:](<mtlcomputecommandencoder/useheap(__).md>) — Ensures the shaders in the render pass’s subsequent draw commands have access to all of the resources you allocate from a heap.
- [useHeaps(_:)](<mtlcomputecommandencoder/useheaps(__).md>) — Ensures the shaders in the render pass’s subsequent draw commands have access to all of the resources you allocate from multiple heaps.

### Configuring tile memory

- [- setThreadgroupMemoryLength:atIndex:](<mtlcomputecommandencoder/setthreadgroupmemorylength(__index_).md>) — Configures the size of a block of threadgroup memory.
- [- setImageblockWidth:height:](<mtlcomputecommandencoder/setimageblockwidth(__height_).md>) — Sets the size, in pixels, of imageblock data in tile memory.

### Configuring stage-in data

- [- setStageInRegion:](<mtlcomputecommandencoder/setstageinregion(__).md>) — Sets the dimensions over the thread grid of how your compute kernel receives stage-in arguments.
- [- setStageInRegionWithIndirectBuffer:indirectBufferOffset:](<mtlcomputecommandencoder/setstageinregionwithindirectbuffer(__indirectbufferoffset_).md>) — Sets the region of the stage-in attributes to apply to a compute kernel using an indirect buffer.

### Dispatching kernel calls directly

- [- dispatchThreads:threadsPerThreadgroup:](<mtlcomputecommandencoder/dispatchthreads(__threadsperthreadgroup_).md>) — Encodes a compute command using an arbitrarily sized grid.
- [- dispatchThreadgroups:threadsPerThreadgroup:](<mtlcomputecommandencoder/dispatchthreadgroups(__threadsperthreadgroup_).md>) — Encodes a compute dispatch command using a grid aligned to threadgroup boundaries.

### Dispatching from indirect command buffers

- [- dispatchThreadgroupsWithIndirectBuffer:indirectBufferOffset:threadsPerThreadgroup:](<mtlcomputecommandencoder/dispatchthreadgroups(indirectbuffer_indirectbufferoffset_threadsperthreadgroup_).md>) — Encodes a dispatch call for a compute pass, using an indirect buffer that defines the size of a grid that aligns to threadgroup boundaries.
- [executeCommandsInBuffer(_:range:)](<mtlcomputecommandencoder/executecommandsinbuffer(__range_).md>) — Encodes an instruction to run commands from an indirect buffer.
- [executeCommandsInBuffer(_:indirectBuffer:offset:)](<mtlcomputecommandencoder/executecommandsinbuffer(__indirectbuffer_offset_).md>) — Encodes an instruction to run commands from an indirect buffer, using another buffer to provide the command range.
- [executeCommands(in:indirectBuffer:indirectBufferOffset:)](<mtlcomputecommandencoder/executecommands(in_indirectbuffer_indirectbufferoffset_).md>) — Encodes an instruction to run commands from an indirect buffer, using another buffer to provide the command range.
- [executeCommands(in:with:)](<mtlcomputecommandencoder/executecommands(in_with_).md>) — Encodes an instruction to run commands from an indirect buffer.

### Preventing resource access conflicts

- [- waitForFence:](<mtlcomputecommandencoder/waitforfence(__).md>) — Encodes a command that instructs the GPU to pause the compute pass until another pass updates a fence.
- [- updateFence:](<mtlcomputecommandencoder/updatefence(__).md>) — Encodes a command that instructs the GPU to update a fence after the compute pass completes.
- [- memoryBarrierWithScope:](<mtlcomputecommandencoder/memorybarrier(scope_).md>) — Creates a memory barrier that enforces the order of write and read operations for specific resource types.
- [memoryBarrier(resources:)](<mtlcomputecommandencoder/memorybarrier(resources_).md>) — Creates a memory barrier that enforces the order of write and read operations for specific resources.

### Sampling counters

- [- sampleCountersInBuffer:atSampleIndex:withBarrier:](<mtlcomputecommandencoder/samplecounters(samplebuffer_sampleindex_barrier_).md>) — Encodes a command to sample hardware counters, providing performance information.

## See Also

### Encoding a compute pass

- [Creating threads and threadgroups](creating-threads-and-threadgroups.md) — Learn how Metal organizes compute-processing workloads.
- [Calculating threadgroup and grid sizes](calculating-threadgroup-and-grid-sizes.md) — Calculate the optimum sizes for threadgroups and grids when dispatching compute-processing workloads.
- [MTL4ComputeCommandEncoder](mtl4computecommandencoder.md) — Encodes computation dispatches, resource copying commands, and acceleration structure building commands for a single pass into a command buffer.
