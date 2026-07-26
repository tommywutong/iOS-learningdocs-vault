---
title: 'setKernelBuffer(_:offset:at:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 11.0+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlindirectcomputecommand/setkernelbuffer(_:offset:at:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlindirectcomputecommand/setkernelbuffer(_:offset:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlindirectcomputecommand/setkernelbuffer%28_%3Aoffset%3Aat%3A%29.json'
content_hash: 'sha256:d5942dd9864766dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIndirectComputeCommand](../mtlindirectcomputecommand.md)

# setKernelBuffer(_:offset:at:)

<sub>Instance Method</sub>

Sets a buffer for the compute function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setKernelBuffer(_ buffer: any MTLBuffer, offset: Int, at index: Int)
```

## Parameters

- `buffer` — The buffer to set in the buffer argument table.

- `offset` — Where the data begins, in bytes, from the start of the buffer.

- `index` — An index in the buffer argument table.

## Discussion

If you created the indirect command buffer with [inheritBuffers](../mtlindirectcommandbufferdescriptor/inheritbuffers.md) set to [true](../../swift/true.md), don’t call this method. The command gets the arguments from the parent encoder when you execute the command.

If you need to pass other kinds of parameters to your shader, such as textures and samplers, create an argument buffer and pass it to the shader using this method.

## See Also

### Setting a command’s arguments

- [- setComputePipelineState:](<setcomputepipelinestate(__).md>) — Sets the command’s compute pipeline state.
- [- setImageblockWidth:height:](<setimageblockwidth(__height_).md>) — Sets the size, in pixels, of the imageblock.
- [- setThreadgroupMemoryLength:atIndex:](<setthreadgroupmemorylength(__index_).md>) — Sets the size of a block of threadgroup memory.
- [setThreadgroupMemoryLength(_:at:)](<setthreadgroupmemorylength(__at_).md>) — Sets the size of a block of threadgroup memory.
- [- setStageInRegion:](<setstageinregion(__).md>) — Sets the region of the stage-in attributes to apply to the compute kernel.
- [setStageIn(_:)](<setstagein(__).md>) — Sets the region of the stage-in attributes to apply to the compute kernel.
