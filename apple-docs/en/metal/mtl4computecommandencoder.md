---
title: MTL4ComputeCommandEncoder
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4computecommandencoder
source_url: 'https://developer.apple.com/documentation/metal/mtl4computecommandencoder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4computecommandencoder.json'
content_hash: 'sha256:5569ee7cae7c9c5f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTL4ComputeCommandEncoder

<sub>Protocol</sub>

Encodes computation dispatches, resource copying commands, and acceleration structure building commands for a single pass into a command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTL4ComputeCommandEncoder : MTL4CommandEncoder
```

## Overview

Each Metal 4 compute encoder combines compute dispatch commands, blit commands, and acceleration structure commands into a single pass. The unified nature of this encoder type eliminates the overhead from creating separate encoders like [MTLComputeCommandEncoder](mtlcomputecommandencoder.md), [MTLBlitCommandEncoder](mtlblitcommandencoder.md), and [MTLAccelerationStructureCommandEncoder](mtlaccelerationstructurecommandencoder.md), and then encoding separate passes with them.

Create a compute encoder by calling a factory method of an [MTL4CommandBuffer](mtl4commandbuffer.md) instance, such as [- computeCommandEncoder](<mtl4commandbuffer/makecomputecommandencoder().md>).

### Command stages

Most compute commands apply to one stage within a pass. The following table shows which stage applies to each command:

| Function | MTLStages |
|---|---|
| [- dispatchThreads:threadsPerThreadgroup:](<mtl4computecommandencoder/dispatchthreads(threadspergrid_threadsperthreadgroup_).md>) | [MTLStageDispatch](mtlstages/dispatch.md) |
| [- dispatchThreadsWithIndirectBuffer:](<mtl4computecommandencoder/dispatchthreads(indirectbuffer_).md>) | [MTLStageDispatch](mtlstages/dispatch.md) |
| [- dispatchThreadgroups:threadsPerThreadgroup:](<mtl4computecommandencoder/dispatchthreadgroups(threadgroupspergrid_threadsperthreadgroup_).md>) | [MTLStageDispatch](mtlstages/dispatch.md) |
| [- dispatchThreadgroupsWithIndirectBuffer:threadsPerThreadgroup:](<mtl4computecommandencoder/dispatchthreadgroups(indirectbuffer_threadsperthreadgroup_).md>) | [MTLStageDispatch](mtlstages/dispatch.md) |
| [- copyFromBuffer:sourceOffset:toBuffer:destinationOffset:size:](<mtl4computecommandencoder/copy(sourcebuffer_sourceoffset_destinationbuffer_destinationoffset_size_).md>) | [MTLStageBlit](mtlstages/blit.md) |
| [copy(sourceBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:destinationTexture:destinationSlice:destinationLevel:destinationOrigin:options:)](<mtl4computecommandencoder/copy(sourcebuffer_sourceoffset_sourcebytesperrow_sourcebytesperimage_sourcesize_destinationtexture_destinationslice_destinationlevel_destinationorigin_options_).md>) | [MTLStageBlit](mtlstages/blit.md) |
| [- copyFromTensor:sourceOrigin:sourceDimensions:toTensor:destinationOrigin:destinationDimensions:](<mtl4computecommandencoder/copy(sourcetensor_sourceorigin_sourcedimensions_destinationtensor_destinationorigin_destinationdimensions_).md>) | [MTLStageBlit](mtlstages/blit.md) |
| [- copyFromTexture:toTexture:](<mtl4computecommandencoder/copy(sourcetexture_destinationtexture_).md>) | [MTLStageBlit](mtlstages/blit.md) |
| [- copyFromTexture:sourceSlice:sourceLevel:toTexture:destinationSlice:destinationLevel:sliceCount:levelCount:](<mtl4computecommandencoder/copy(sourcetexture_sourceslice_sourcelevel_destinationtexture_destinationslice_destinationlevel_slicecount_levelcount_).md>) | [MTLStageBlit](mtlstages/blit.md) |
| [copy(sourceTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:destinationBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:)](<mtl4computecommandencoder/copy(sourcetexture_sourceslice_sourcelevel_sourceorigin_sourcesize_destinationbuffer_destinationoffset_destinationbytesperrow_destinationbytesperimage_options_).md>) | [MTLStageBlit](mtlstages/blit.md) |
| [- copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:](<mtl4computecommandencoder/copy(sourcetexture_sourceslice_sourcelevel_sourceorigin_sourcesize_destinationtexture_destinationslice_destinationlevel_destinationorigin_).md>) | [MTLStageBlit](mtlstages/blit.md) |
| [copyCommands(sourceBuffer:sourceRange:destinationBuffer:destinationIndex:)](<mtl4computecommandencoder/copycommands(sourcebuffer_sourcerange_destinationbuffer_destinationindex_).md>) | [MTLStageBlit](mtlstages/blit.md) |
| [fill(buffer:range:value:)](<mtl4computecommandencoder/fill(buffer_range_value_).md>) | [MTLStageBlit](mtlstages/blit.md) |
| [- generateMipmapsForTexture:](<mtl4computecommandencoder/generatemipmaps(texture_).md>) | [MTLStageBlit](mtlstages/blit.md) |
| [optimizeCommands(buffer:range:)](<mtl4computecommandencoder/optimizecommands(buffer_range_).md>) | [MTLStageBlit](mtlstages/blit.md) |
| [- optimizeContentsForCPUAccess:](<mtl4computecommandencoder/optimizecontents(forcpuaccess_).md>) | [MTLStageBlit](mtlstages/blit.md) |
| [- optimizeContentsForCPUAccess:slice:level:](<mtl4computecommandencoder/optimizecontents(forcpuaccess_slice_level_).md>) | [MTLStageBlit](mtlstages/blit.md) |
| [- optimizeContentsForGPUAccess:](<mtl4computecommandencoder/optimizecontents(forgpuaccess_).md>) | [MTLStageBlit](mtlstages/blit.md) |
| [- optimizeContentsForGPUAccess:slice:level:](<mtl4computecommandencoder/optimizecontents(forgpuaccess_slice_level_).md>) | [MTLStageBlit](mtlstages/blit.md) |
| [resetCommands(buffer:range:)](<mtl4computecommandencoder/resetcommands(buffer_range_).md>) | [MTLStageBlit](mtlstages/blit.md) |
| [- buildAccelerationStructure:descriptor:scratchBuffer:](<mtl4computecommandencoder/build(destinationaccelerationstructure_descriptor_scratchbuffer_).md>) | [MTLStageAccelerationStructure](mtlstages/accelerationstructure.md) |
| [- copyAccelerationStructure:toAccelerationStructure:](<mtl4computecommandencoder/copy(sourceaccelerationstructure_destinationaccelerationstructure_).md>) | [MTLStageAccelerationStructure](mtlstages/accelerationstructure.md) |
| [- copyAndCompactAccelerationStructure:toAccelerationStructure:](<mtl4computecommandencoder/copyandcompact(sourceaccelerationstructure_destinationaccelerationstructure_).md>) | [MTLStageAccelerationStructure](mtlstages/accelerationstructure.md) |
| [- refitAccelerationStructure:descriptor:destination:scratchBuffer:options:](<mtl4computecommandencoder/refit(sourceaccelerationstructure_descriptor_destinationaccelerationstructure_scratchbuffer_options_).md>) | [MTLStageAccelerationStructure](mtlstages/accelerationstructure.md) |
| [- writeCompactedAccelerationStructureSize:toBuffer:](<mtl4computecommandencoder/writecompactedsize(sourceaccelerationstructure_destinationbuffer_).md>) | [MTLStageAccelerationStructure](mtlstages/accelerationstructure.md) |
| [executeCommands(buffer:range:)](<mtl4computecommandencoder/executecommands(buffer_range_).md>)![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[executeCommandsInBuffer:withRange:](mtl4computecommandencoder/executecommandsinbuffer_withrange_.md) | None |
| [- executeCommandsInBuffer:indirectBuffer:](<mtl4computecommandencoder/executecommands(buffer_indirectbuffer_).md>) | None |
| [- writeTimestampWithGranularity:intoHeap:atIndex:](<mtl4computecommandencoder/writetimestamp(granularity_counterheap_index_).md>) | None |

The [executeCommands(buffer:range:)](<mtl4computecommandencoder/executecommands(buffer_range_).md>) and [- executeCommandsInBuffer:indirectBuffer:](<mtl4computecommandencoder/executecommands(buffer_indirectbuffer_).md>) commands don’t apply to any stage, which means you can’t use a barrier to wait for all commands in an indirect command buffer to complete. However, each command within the [MTLIndirectCommandBuffer](mtlindirectcommandbuffer.md) applies to the same stages as when you encode the equivalent command directly.

For more information about stages and synchronization, see [MTLStages](mtlstages.md) and [Resource synchronization](resource-synchronization.md).

## Relationships

- **Inherits From**: [MTL4CommandEncoder](mtl4commandencoder.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Configuring the pass

- [- setComputePipelineState:](<mtl4computecommandencoder/setcomputepipelinestate(__).md>) — Configures this encoder with a compute pipeline state that applies to your subsequent dispatch commands.
- [- setArgumentTable:](<mtl4computecommandencoder/setargumenttable(__).md>) — Sets an argument table for the compute shader stage of this pipeline.
- [- setThreadgroupMemoryLength:atIndex:](<mtl4computecommandencoder/setthreadgroupmemorylength(__index_).md>) — Configures the size of a threadgroup memory buffer for a threadgroup argument in the compute shader function.
- [- setImageblockWidth:height:](<mtl4computecommandencoder/setimageblocksize(width_height_).md>) — Specifies the size, in pixels, of imageblock data in tile memory.

### Inspecting the pass

- [- stages](<mtl4computecommandencoder/stages().md>) — Queries a bitmask representing the shader stages on which commands currently present in this command encoder operate.

### Running dispatch commands

- [- dispatchThreads:threadsPerThreadgroup:](<mtl4computecommandencoder/dispatchthreads(threadspergrid_threadsperthreadgroup_).md>) — Encodes a compute dispatch command using an arbitrarily-sized grid.
- [- dispatchThreadsWithIndirectBuffer:](<mtl4computecommandencoder/dispatchthreads(indirectbuffer_).md>) — Encodes a compute dispatch command with an arbitrarily sized grid, using an indirect buffer for arguments.
- [- dispatchThreadgroups:threadsPerThreadgroup:](<mtl4computecommandencoder/dispatchthreadgroups(threadgroupspergrid_threadsperthreadgroup_).md>) — Encodes a compute dispatch command with a grid that aligns to threadgroup boundaries.
- [- dispatchThreadgroupsWithIndirectBuffer:threadsPerThreadgroup:](<mtl4computecommandencoder/dispatchthreadgroups(indirectbuffer_threadsperthreadgroup_).md>) — Encodes a compute dispatch command with a grid that aligns to threadgroup boundaries, using an indirect buffer for arguments.

### Encoding buffer copy commands

- [- copyFromBuffer:sourceOffset:toBuffer:destinationOffset:size:](<mtl4computecommandencoder/copy(sourcebuffer_sourceoffset_destinationbuffer_destinationoffset_size_).md>) — Encodes a command that copies data from a buffer instance into another.

### Encoding buffer-to-texture copy commands

- [copy(sourceBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:destinationTexture:destinationSlice:destinationLevel:destinationOrigin:options:)](<mtl4computecommandencoder/copy(sourcebuffer_sourceoffset_sourcebytesperrow_sourcebytesperimage_sourcesize_destinationtexture_destinationslice_destinationlevel_destinationorigin_options_).md>) — Encodes a command to copy image data from a buffer into a texture with options for special texture formats.

### Encoding texture copy commands

- [- copyFromTensor:sourceOrigin:sourceDimensions:toTensor:destinationOrigin:destinationDimensions:](<mtl4computecommandencoder/copy(sourcetensor_sourceorigin_sourcedimensions_destinationtensor_destinationorigin_destinationdimensions_).md>) — Encodes a command to copy data from a slice of the data plane of a tensor into a slice of the data plane of another tensor.
- [- copyFromTexture:toTexture:](<mtl4computecommandencoder/copy(sourcetexture_destinationtexture_).md>) — Encodes a command that copies data from a texture to another.
- [- copyFromTexture:sourceSlice:sourceLevel:toTexture:destinationSlice:destinationLevel:sliceCount:levelCount:](<mtl4computecommandencoder/copy(sourcetexture_sourceslice_sourcelevel_destinationtexture_destinationslice_destinationlevel_slicecount_levelcount_).md>) — Encodes a command that copies slices of a texture to slices of another texture.
- [- copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:](<mtl4computecommandencoder/copy(sourcetexture_sourceslice_sourcelevel_sourceorigin_sourcesize_destinationtexture_destinationslice_destinationlevel_destinationorigin_).md>) — Encodes a command that copies image data from a slice of a texture into a slice of another texture.

### Encoding texture-to-buffer copy commands

- [copy(sourceTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:destinationBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:)](<mtl4computecommandencoder/copy(sourcetexture_sourceslice_sourcelevel_sourceorigin_sourcesize_destinationbuffer_destinationoffset_destinationbytesperrow_destinationbytesperimage_options_).md>) — Encodes a command that copies image data from a slice of a texture instance to a buffer, with options for special texture formats.

### Encoding indirect command buffer copy commands

- [copyCommands(sourceBuffer:sourceRange:destinationBuffer:destinationIndex:)](<mtl4computecommandencoder/copycommands(sourcebuffer_sourcerange_destinationbuffer_destinationindex_).md>) — Encodes a command that copies commands from one indirect command buffer into another.

### Encoding buffer fill commands

- [fill(buffer:range:value:)](<mtl4computecommandencoder/fill(buffer_range_value_).md>) — Encodes a command that fills a buffer with a constant value for each byte.

### Encoding mipmap generation commands

- [- generateMipmapsForTexture:](<mtl4computecommandencoder/generatemipmaps(texture_).md>) — Encodes a command that generates mipmaps for a texture instance from the base mipmap level up to the highest mipmap level.

### Encoding optimization commands

- [optimizeCommands(buffer:range:)](<mtl4computecommandencoder/optimizecommands(buffer_range_).md>) — Encode a command to attempt to improve the performance of a range of commands within an indirect command buffer.
- [- optimizeContentsForCPUAccess:](<mtl4computecommandencoder/optimizecontents(forcpuaccess_).md>) — Encodes a command that modifies the contents of a texture to improve the performance of CPU accesses to its contents.
- [- optimizeContentsForCPUAccess:slice:level:](<mtl4computecommandencoder/optimizecontents(forcpuaccess_slice_level_).md>) — Encodes a command that modifies the contents of a texture to improve the performance of CPU accesses to its contents in a specific region.
- [- optimizeContentsForGPUAccess:](<mtl4computecommandencoder/optimizecontents(forgpuaccess_).md>) — Encodes a command that modifies the contents of a texture to improve the performance of GPU accesses to its contents.
- [- optimizeContentsForGPUAccess:slice:level:](<mtl4computecommandencoder/optimizecontents(forgpuaccess_slice_level_).md>) — Encodes a command that modifies the contents of a texture instance to improve the performance of GPU accesses to its contents in a specific region.

### Encoding reset commands

- [resetCommands(buffer:range:)](<mtl4computecommandencoder/resetcommands(buffer_range_).md>) — Encodes a command that resets a range of commands in an indirect command buffer.

### Encoding acceleration structure build commands

- [- buildAccelerationStructure:descriptor:scratchBuffer:](<mtl4computecommandencoder/build(destinationaccelerationstructure_descriptor_scratchbuffer_).md>) — Encodes an acceleration structure build into the command buffer.

### Encoding acceleration structure copy commands

- [- copyAccelerationStructure:toAccelerationStructure:](<mtl4computecommandencoder/copy(sourceaccelerationstructure_destinationaccelerationstructure_).md>) — Encodes an acceleration structure copy operation into the command buffer.
- [- copyAndCompactAccelerationStructure:toAccelerationStructure:](<mtl4computecommandencoder/copyandcompact(sourceaccelerationstructure_destinationaccelerationstructure_).md>) — Encodes a command to copy and compact an acceleration structure.
- [- writeCompactedAccelerationStructureSize:toBuffer:](<mtl4computecommandencoder/writecompactedsize(sourceaccelerationstructure_destinationbuffer_).md>) — Encodes a command to compute the size an acceleration structure can compact into, writing the result into a buffer.

### Encoding acceleration structure refit commands

- [- refitAccelerationStructure:descriptor:destination:scratchBuffer:options:](<mtl4computecommandencoder/refit(sourceaccelerationstructure_descriptor_destinationaccelerationstructure_scratchbuffer_options_).md>) — Encodes an acceleration structure refit operation into the command buffer, providing additional options.

### Encoding indirect command buffers

- [executeCommands(buffer:range:)](<mtl4computecommandencoder/executecommands(buffer_range_).md>) — Encodes a command to execute commands from an indirect command buffer.
- [- executeCommandsInBuffer:indirectBuffer:](<mtl4computecommandencoder/executecommands(buffer_indirectbuffer_).md>) — Encodes an instruction to execute commands from an indirect command buffer, using an indirect buffer for arguments.

### Encoding performance measurement commands

- [- writeTimestampWithGranularity:intoHeap:atIndex:](<mtl4computecommandencoder/writetimestamp(granularity_counterheap_index_).md>) — Writes a GPU timestamp into a heap.

### Instance Methods

- [- copyFromTensor:sourceOrigin:sourceDimensions:sourcePlane:toTensor:destinationOrigin:destinationDimensions:destinationPlane:](<mtl4computecommandencoder/copy(sourcetensor_sourceorigin_sourcedimensions_sourceplane_destinationtensor_destinationorigin_destinationdimensions_destinationplane_).md>) — Encodes a command to copy data from a slice of a plane of a tensor into a slice of a plane of another tensor. _(beta)_

## See Also

### Encoding a compute pass

- [Creating threads and threadgroups](creating-threads-and-threadgroups.md) — Learn how Metal organizes compute-processing workloads.
- [Calculating threadgroup and grid sizes](calculating-threadgroup-and-grid-sizes.md) — Calculate the optimum sizes for threadgroups and grids when dispatching compute-processing workloads.
- [MTLComputeCommandEncoder](mtlcomputecommandencoder.md) — Encodes computation dispatch commands for a single compute pass into a command buffer.
