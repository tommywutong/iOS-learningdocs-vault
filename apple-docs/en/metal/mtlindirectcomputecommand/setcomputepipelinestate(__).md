---
title: 'setComputePipelineState(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 11.0+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlindirectcomputecommand/setcomputepipelinestate(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlindirectcomputecommand/setcomputepipelinestate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlindirectcomputecommand/setcomputepipelinestate%28_%3A%29.json'
content_hash: 'sha256:ee3512351ca2d025'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIndirectComputeCommand](../mtlindirectcomputecommand.md)

# setComputePipelineState(_:)

<sub>Instance Method</sub>

Sets the command’s compute pipeline state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setComputePipelineState(_ pipelineState: any MTLComputePipelineState)
```

## Parameters

- `pipelineState` — A compute pipeline state instance.

## Discussion

You don’t need to call this method if you create an indirect command buffer with its [inheritPipelineState](../mtlindirectcommandbufferdescriptor/inheritpipelinestate.md) property equal to [true](../../swift/true.md). The command gets the pipeline state from the parent encoder when you run the command.

If you create an indirect command buffer with its [inheritPipelineState](../mtlindirectcommandbufferdescriptor/inheritpipelinestate.md) property equal to [false](../../swift/false.md), you need to set the pipeline state prior to encoding a drawing command.

## See Also

### Setting a command’s arguments

- [- setImageblockWidth:height:](<setimageblockwidth(__height_).md>) — Sets the size, in pixels, of the imageblock.
- [- setKernelBuffer:offset:atIndex:](<setkernelbuffer(__offset_at_).md>) — Sets a buffer for the compute function.
- [- setThreadgroupMemoryLength:atIndex:](<setthreadgroupmemorylength(__index_).md>) — Sets the size of a block of threadgroup memory.
- [setThreadgroupMemoryLength(_:at:)](<setthreadgroupmemorylength(__at_).md>) — Sets the size of a block of threadgroup memory.
- [- setStageInRegion:](<setstageinregion(__).md>) — Sets the region of the stage-in attributes to apply to the compute kernel.
- [setStageIn(_:)](<setstagein(__).md>) — Sets the region of the stage-in attributes to apply to the compute kernel.
