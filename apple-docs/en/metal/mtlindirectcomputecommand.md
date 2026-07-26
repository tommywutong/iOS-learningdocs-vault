---
title: MTLIndirectComputeCommand
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 11.0+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlindirectcomputecommand
source_url: 'https://developer.apple.com/documentation/metal/mtlindirectcomputecommand'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlindirectcomputecommand.json'
content_hash: 'sha256:20bf6a363d2da67f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLIndirectComputeCommand

<sub>Protocol</sub>

A compute command in an indirect command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLIndirectComputeCommand : NSObjectProtocol
```

## Overview

Don’t implement this protocol; you get instances of this type by asking an [MTLIndirectCommandBuffer](mtlindirectcommandbuffer.md) for them.

Use this instance to reset or encode a command. You need to reset a command before encoding a new command.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Setting a command’s arguments

- [- setComputePipelineState:](<mtlindirectcomputecommand/setcomputepipelinestate(__).md>) — Sets the command’s compute pipeline state.
- [- setImageblockWidth:height:](<mtlindirectcomputecommand/setimageblockwidth(__height_).md>) — Sets the size, in pixels, of the imageblock.
- [- setKernelBuffer:offset:atIndex:](<mtlindirectcomputecommand/setkernelbuffer(__offset_at_).md>) — Sets a buffer for the compute function.
- [- setThreadgroupMemoryLength:atIndex:](<mtlindirectcomputecommand/setthreadgroupmemorylength(__index_).md>) — Sets the size of a block of threadgroup memory.
- [setThreadgroupMemoryLength(_:at:)](<mtlindirectcomputecommand/setthreadgroupmemorylength(__at_).md>) — Sets the size of a block of threadgroup memory.
- [- setStageInRegion:](<mtlindirectcomputecommand/setstageinregion(__).md>) — Sets the region of the stage-in attributes to apply to the compute kernel.
- [setStageIn(_:)](<mtlindirectcomputecommand/setstagein(__).md>) — Sets the region of the stage-in attributes to apply to the compute kernel.

### Synchronizing command execution

- [- setBarrier](<mtlindirectcomputecommand/setbarrier().md>) — Adds a barrier to ensure that commands executed prior to this command are complete before this command executes.
- [- clearBarrier](<mtlindirectcomputecommand/clearbarrier().md>) — Removes any barrier set on the command.

### Encoding a compute command

- [- concurrentDispatchThreadgroups:threadsPerThreadgroup:](<mtlindirectcomputecommand/concurrentdispatchthreadgroups(__threadsperthreadgroup_).md>) — Encodes a compute command using a grid aligned to threadgroup boundaries.
- [- concurrentDispatchThreads:threadsPerThreadgroup:](<mtlindirectcomputecommand/concurrentdispatchthreads(__threadsperthreadgroup_).md>) — Encodes a compute command using an arbitrarily sized grid.

### Resetting a command

- [- reset](<mtlindirectcomputecommand/reset().md>) — Resets the command to its default state.

### Instance Methods

- [- setKernelBuffer:offset:attributeStride:atIndex:](<mtlindirectcomputecommand/setkernelbuffer(__offset_attributestride_at_).md>)

## See Also

### Indirect compute commands

- [MTLRegion](mtlregion.md) — The bounds for a subset of an instance’s elements.
- [MTLSize](mtlsize.md) — A type that represents one, two, or three dimensions of a type instance, such as an array or texture.
- [MTLOrigin](mtlorigin.md) — The coordinates for the front upper-left corner of a region.
- [MTLStageInRegionIndirectArguments](mtlstageinregionindirectarguments.md) — The data layout required for the arguments needed to specify the stage-in region.
- [MTLDispatchThreadgroupsIndirectArguments](mtldispatchthreadgroupsindirectarguments.md) — The data layout required for arguments needed to specify the size of threadgroups.
