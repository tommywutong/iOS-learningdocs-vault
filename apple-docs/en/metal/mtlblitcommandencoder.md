---
title: MTLBlitCommandEncoder
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlblitcommandencoder
source_url: 'https://developer.apple.com/documentation/metal/mtlblitcommandencoder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblitcommandencoder.json'
content_hash: 'sha256:f73a833b567f6364'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLBlitCommandEncoder

<sub>Protocol</sub>

Encodes commands that copy and modify resources for a single blit pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLBlitCommandEncoder : MTLCommandEncoder
```

## Overview

Create a blit encoder by calling one of the factory methods on an [MTLCommandBuffer](mtlcommandbuffer.md) instance, such as [- blitCommandEncoder](<mtlcommandbuffer/makeblitcommandencoder().md>).

A blit command encoder adds commands to a command buffer that modify resources in various ways, including:

- Filling buffers with repeating bytes
- Generating mipmaps for textures
- Copying data between buffers
- Copying data between textures
- Copying data between a texture and a buffer
- Managing the contents of indirect command buffers
- Synchronizing buffers, textures, and other resources between the CPU and GPU
- Improving runtime performance for resources by optimizing their memory layout for the GPU or CPU

You typically use these commands to move data between a resource that uses private storage and another resource that uses CPU-accessible storage. Some apps also use them to apply image-processing and texture effects, such as blurring or reflections, or to render and work with offscreen image data.

When you finish encoding blit commands, finalize the blit pass into the command buffer by calling the encoder’s [- endEncoding](<mtlcommandencoder/endencoding().md>) method.

### Command stages

Most blit commands apply to one stage within a pass. The following table shows which stages apply to each command:

| Function | MTLStages |
|---|---|
| [fill(buffer:range:value:)](<mtlblitcommandencoder/fill(buffer_range_value_).md>) | [MTLStageBlit](mtlstages/blit.md) |
| [- generateMipmapsForTexture:](<mtlblitcommandencoder/generatemipmaps(for_).md>) | [MTLStageBlit](mtlstages/blit.md) |
| [- copyFromBuffer:sourceOffset:toBuffer:destinationOffset:size:](<mtlblitcommandencoder/copy(from_sourceoffset_to_destinationoffset_size_).md>) | [MTLStageBlit](mtlstages/blit.md) |
| [- copyFromTexture:toTexture:](<mtlblitcommandencoder/copy(from_to_).md>) | [MTLStageBlit](mtlstages/blit.md) |
| [- copyFromTexture:sourceSlice:sourceLevel:toTexture:destinationSlice:destinationLevel:sliceCount:levelCount:](<mtlblitcommandencoder/copy(from_sourceslice_sourcelevel_to_destinationslice_destinationlevel_slicecount_levelcount_).md>) | [MTLStageBlit](mtlstages/blit.md) |
| [- copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:](<mtlblitcommandencoder/copy(from_sourceslice_sourcelevel_sourceorigin_sourcesize_to_destinationslice_destinationlevel_destinationorigin_).md>) | [MTLStageBlit](mtlstages/blit.md) |
| [- copyFromTensor:sourceOrigin:sourceDimensions:toTensor:destinationOrigin:destinationDimensions:](<mtlblitcommandencoder/copy(from_sourceorigin_sourcedimensions_to_destinationorigin_destinationdimensions_).md>) | [MTLStageBlit](mtlstages/blit.md) |
| [- copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:](<mtlblitcommandencoder/copy(from_sourceoffset_sourcebytesperrow_sourcebytesperimage_sourcesize_to_destinationslice_destinationlevel_destinationorigin_).md>) | [MTLStageBlit](mtlstages/blit.md) |
| [- copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:](<mtlblitcommandencoder/copy(from_sourceoffset_sourcebytesperrow_sourcebytesperimage_sourcesize_to_destinationslice_destinationlevel_destinationorigin_options_).md>) | [MTLStageBlit](mtlstages/blit.md) |
| [- copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:](<mtlblitcommandencoder/copy(from_sourceslice_sourcelevel_sourceorigin_sourcesize_to_destinationoffset_destinationbytesperrow_destinationbytesperimage_).md>) | [MTLStageBlit](mtlstages/blit.md) |
| [- copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:](<mtlblitcommandencoder/copy(from_sourceslice_sourcelevel_sourceorigin_sourcesize_to_destinationoffset_destinationbytesperrow_destinationbytesperimage_options_).md>) | [MTLStageBlit](mtlstages/blit.md) |
| [- optimizeContentsForGPUAccess:](<mtlblitcommandencoder/optimizecontentsforgpuaccess(texture_).md>) | [MTLStageBlit](mtlstages/blit.md) |
| [- optimizeContentsForGPUAccess:slice:level:](<mtlblitcommandencoder/optimizecontentsforgpuaccess(texture_slice_level_).md>) | [MTLStageBlit](mtlstages/blit.md) |
| [- optimizeContentsForCPUAccess:](<mtlblitcommandencoder/optimizecontentsforcpuaccess(texture_).md>) | [MTLStageBlit](mtlstages/blit.md) |
| [- optimizeContentsForCPUAccess:slice:level:](<mtlblitcommandencoder/optimizecontentsforcpuaccess(texture_slice_level_).md>) | [MTLStageBlit](mtlstages/blit.md) |
| [- synchronizeResource:](<mtlblitcommandencoder/synchronize(resource_).md>) | None |
| [- synchronizeTexture:slice:level:](<mtlblitcommandencoder/synchronize(texture_slice_level_).md>) | None |
| [copyIndirectCommandBuffer(_:sourceRange:destination:destinationIndex:)](<mtlblitcommandencoder/copyindirectcommandbuffer(__sourcerange_destination_destinationindex_).md>) | [MTLStageBlit](mtlstages/blit.md) |
| [resetCommandsInBuffer(_:range:)](<mtlblitcommandencoder/resetcommandsinbuffer(__range_).md>) | [MTLStageBlit](mtlstages/blit.md) |
| [optimizeIndirectCommandBuffer(_:range:)](<mtlblitcommandencoder/optimizeindirectcommandbuffer(__range_).md>) | [MTLStageBlit](mtlstages/blit.md) |
| [- sampleCountersInBuffer:atSampleIndex:withBarrier:](<mtlblitcommandencoder/samplecounters(samplebuffer_sampleindex_barrier_).md>) | None |
| [resolveCounters(_:range:destinationBuffer:destinationOffset:)](<mtlblitcommandencoder/resolvecounters(__range_destinationbuffer_destinationoffset_).md>) | [MTLStageBlit](mtlstages/blit.md) |
| [- getTextureAccessCounters:region:mipLevel:slice:resetCounters:countersBuffer:countersBufferOffset:](<mtlblitcommandencoder/gettextureaccesscounters(__region_miplevel_slice_resetcounters_countersbuffer_countersbufferoffset_).md>) | [MTLStageBlit](mtlstages/blit.md) |
| [- resetTextureAccessCounters:region:mipLevel:slice:](<mtlblitcommandencoder/resettextureaccesscounters(__region_miplevel_slice_).md>) | [MTLStageBlit](mtlstages/blit.md) |

For more information about stages and synchronization, see [MTLStages](mtlstages.md) and [Resource synchronization](resource-synchronization.md).

## Relationships

- **Inherits From**: [MTLCommandEncoder](mtlcommandencoder.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Filling buffers

- [fill(buffer:range:value:)](<mtlblitcommandencoder/fill(buffer_range_value_).md>) — Encodes a command that fills a buffer with a constant value for each byte.

### Generating texture mipmaps

- [- generateMipmapsForTexture:](<mtlblitcommandencoder/generatemipmaps(for_).md>) — Encodes a command that generates mipmaps for a texture from the base mipmap level up to the highest mipmap level.

### Copying buffer data to another buffer

- [- copyFromBuffer:sourceOffset:toBuffer:destinationOffset:size:](<mtlblitcommandencoder/copy(from_sourceoffset_to_destinationoffset_size_).md>) — Encodes a command that copies data from one buffer into another.

### Copying texture data to another texture

- [- copyFromTexture:toTexture:](<mtlblitcommandencoder/copy(from_to_).md>) — Encodes a command that copies data from one texture to another.
- [- copyFromTexture:sourceSlice:sourceLevel:toTexture:destinationSlice:destinationLevel:sliceCount:levelCount:](<mtlblitcommandencoder/copy(from_sourceslice_sourcelevel_to_destinationslice_destinationlevel_slicecount_levelcount_).md>) — Encodes a command that copies slices of a texture to another texture’s slices.
- [- copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:](<mtlblitcommandencoder/copy(from_sourceslice_sourcelevel_sourceorigin_sourcesize_to_destinationslice_destinationlevel_destinationorigin_).md>) — Encodes a command that copies image data from a texture’s slice into another slice.
- [- copyFromTensor:sourceOrigin:sourceDimensions:toTensor:destinationOrigin:destinationDimensions:](<mtlblitcommandencoder/copy(from_sourceorigin_sourcedimensions_to_destinationorigin_destinationdimensions_).md>) — Encodes a command to copy data from a slice of the data plane of a tensor into a slice of the data plane of another tensor.

### Copying buffer data to a texture

- [- copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:](<mtlblitcommandencoder/copy(from_sourceoffset_sourcebytesperrow_sourcebytesperimage_sourcesize_to_destinationslice_destinationlevel_destinationorigin_).md>) — Encodes a command to copy image data from a source buffer into a destination texture.
- [- copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:](<mtlblitcommandencoder/copy(from_sourceoffset_sourcebytesperrow_sourcebytesperimage_sourcesize_to_destinationslice_destinationlevel_destinationorigin_options_).md>) — Encodes a command to copy image data from a source buffer into a destination texture.

### Copying texture data to a buffer

- [- copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:](<mtlblitcommandencoder/copy(from_sourceslice_sourcelevel_sourceorigin_sourcesize_to_destinationoffset_destinationbytesperrow_destinationbytesperimage_).md>) — Encodes a command that copies image data from a texture slice to a buffer.
- [- copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:](<mtlblitcommandencoder/copy(from_sourceslice_sourcelevel_sourceorigin_sourcesize_to_destinationoffset_destinationbytesperrow_destinationbytesperimage_options_).md>) — Encodes a command that copies image data from a texture slice to a buffer, and provides options for special texture formats.

### Optimizing textures for GPU access

- [- optimizeContentsForGPUAccess:](<mtlblitcommandencoder/optimizecontentsforgpuaccess(texture_).md>) — Encodes a command that improves the performance of GPU memory operations with a texture.
- [- optimizeContentsForGPUAccess:slice:level:](<mtlblitcommandencoder/optimizecontentsforgpuaccess(texture_slice_level_).md>) — Encodes a command that improves the performance of GPU memory operations with a specific portion of a texture.

### Optimizing textures for CPU access

- [- optimizeContentsForCPUAccess:](<mtlblitcommandencoder/optimizecontentsforcpuaccess(texture_).md>) — Encodes a command that improves the performance of CPU memory operations with a texture.
- [- optimizeContentsForCPUAccess:slice:level:](<mtlblitcommandencoder/optimizecontentsforcpuaccess(texture_slice_level_).md>) — Encodes a command that improves the performance of CPU memory operations with a specific portion of a texture.

### Synchronizing managed resources

- [- synchronizeResource:](<mtlblitcommandencoder/synchronize(resource_).md>) — Encodes a command that synchronizes the CPU’s copy of a managed resource, such as a buffer or texture, so that it matches the GPU’s copy. _(deprecated)_
- [- synchronizeTexture:slice:level:](<mtlblitcommandencoder/synchronize(texture_slice_level_).md>) — Encodes a command that synchronizes a part of the CPU’s copy of a texture so that it matches the GPU’s copy. _(deprecated)_

### Preventing resource access conflicts

- [- waitForFence:](<mtlblitcommandencoder/waitforfence(__).md>) — Encodes a command that instructs the GPU to pause the blit pass until another pass updates a fence.
- [- updateFence:](<mtlblitcommandencoder/updatefence(__).md>) — Encodes a command that instructs the GPU to update a fence after the blit pass completes.

### Managing indirect command buffers

- [copyIndirectCommandBuffer(_:sourceRange:destination:destinationIndex:)](<mtlblitcommandencoder/copyindirectcommandbuffer(__sourcerange_destination_destinationindex_).md>) — Encodes a command that copies commands from one indirect command buffer into another.
- [resetCommandsInBuffer(_:range:)](<mtlblitcommandencoder/resetcommandsinbuffer(__range_).md>) — Encodes a command that resets a range of commands in an indirect command buffer.
- [optimizeIndirectCommandBuffer(_:range:)](<mtlblitcommandencoder/optimizeindirectcommandbuffer(__range_).md>) — Encodes a command that can improve the performance of a range of commands within an indirect command buffer.

### Sampling counters

- [- sampleCountersInBuffer:atSampleIndex:withBarrier:](<mtlblitcommandencoder/samplecounters(samplebuffer_sampleindex_barrier_).md>) — Encodes a command that samples the GPU’s hardware counters during a blit pass and stores the data in a counter sample buffer.
- [resolveCounters(_:range:destinationBuffer:destinationOffset:)](<mtlblitcommandencoder/resolvecounters(__range_destinationbuffer_destinationoffset_).md>) — Encodes a command that resolves the data from the samples in a sample counter buffer and stores the results into a buffer.

### Managing sparse texture access counters

- [- getTextureAccessCounters:region:mipLevel:slice:resetCounters:countersBuffer:countersBufferOffset:](<mtlblitcommandencoder/gettextureaccesscounters(__region_miplevel_slice_resetcounters_countersbuffer_countersbufferoffset_).md>) — Encodes a command that retrieves a sparse texture’s access data for a specific region, mipmap level, and slice. _(deprecated)_
- [- resetTextureAccessCounters:region:mipLevel:slice:](<mtlblitcommandencoder/resettextureaccesscounters(__region_miplevel_slice_).md>) — Encodes a command that resets a sparse texture’s access data for a specific region, mipmap level, and slice. _(deprecated)_

### Instance Methods

- [- copyFromTensor:sourceOrigin:sourceDimensions:sourcePlane:toTensor:destinationOrigin:destinationDimensions:destinationPlane:](<mtlblitcommandencoder/copy(from_sourceorigin_sourcedimensions_sourceplane_to_destinationorigin_destinationdimensions_destinationplane_).md>) — Encodes a command to copy data from a slice of a plane of a tensor into a slice of a plane of another tensor. _(beta)_

## See Also

### Encoding a blit pass

- [MTLBlitOption](mtlblitoption.md) — The options that enable behavior for some blit operations.
