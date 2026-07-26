---
title: 'setThreadgroupMemoryLength(_:at:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（14.0 起废弃）, iPadOS 13.0+（14.0 起废弃）, Mac Catalyst 14.0+（14.0 起废弃）, tvOS 13.0+（14.0 起废弃）, visionOS]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/metal/mtlindirectcomputecommand/setthreadgroupmemorylength(_:at:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlindirectcomputecommand/setthreadgroupmemorylength(_:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlindirectcomputecommand/setthreadgroupmemorylength%28_%3Aat%3A%29.json'
content_hash: 'sha256:0b594af49ece609a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIndirectComputeCommand](../mtlindirectcomputecommand.md)

# setThreadgroupMemoryLength(_:at:)

<sub>Instance Method</sub>

Sets the size of a block of threadgroup memory.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setThreadgroupMemoryLength(_ length: Int, at index: Int)
```

## Parameters

- `length` — The size of the threadgroup memory, in bytes, which needs to be a multiple of 16 bytes.

- `index` — The index in the threadgroup memory argument table.

## See Also

### Setting a command’s arguments

- [- setComputePipelineState:](<setcomputepipelinestate(__).md>) — Sets the command’s compute pipeline state.
- [- setImageblockWidth:height:](<setimageblockwidth(__height_).md>) — Sets the size, in pixels, of the imageblock.
- [- setKernelBuffer:offset:atIndex:](<setkernelbuffer(__offset_at_).md>) — Sets a buffer for the compute function.
- [- setThreadgroupMemoryLength:atIndex:](<setthreadgroupmemorylength(__index_).md>) — Sets the size of a block of threadgroup memory.
- [- setStageInRegion:](<setstageinregion(__).md>) — Sets the region of the stage-in attributes to apply to the compute kernel.
- [setStageIn(_:)](<setstagein(__).md>) — Sets the region of the stage-in attributes to apply to the compute kernel.
