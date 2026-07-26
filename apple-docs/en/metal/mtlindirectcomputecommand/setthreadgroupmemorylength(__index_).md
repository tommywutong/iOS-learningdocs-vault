---
title: 'setThreadgroupMemoryLength(_:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 11.0+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlindirectcomputecommand/setthreadgroupmemorylength(_:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlindirectcomputecommand/setthreadgroupmemorylength(_:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlindirectcomputecommand/setthreadgroupmemorylength%28_%3Aindex%3A%29.json'
content_hash: 'sha256:47e8d310e2008c00'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIndirectComputeCommand](../mtlindirectcomputecommand.md)

# setThreadgroupMemoryLength(_:index:)

<sub>Instance Method</sub>

Sets the size of a block of threadgroup memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setThreadgroupMemoryLength(_ length: Int, index: Int)
```

## Parameters

- `length` — The size of the threadgroup memory, in bytes, which needs to be a multiple of 16 bytes.

- `index` — The index in the threadgroup memory argument table.

## See Also

### Setting a command’s arguments

- [- setComputePipelineState:](<setcomputepipelinestate(__).md>) — Sets the command’s compute pipeline state.
- [- setImageblockWidth:height:](<setimageblockwidth(__height_).md>) — Sets the size, in pixels, of the imageblock.
- [- setKernelBuffer:offset:atIndex:](<setkernelbuffer(__offset_at_).md>) — Sets a buffer for the compute function.
- [setThreadgroupMemoryLength(_:at:)](<setthreadgroupmemorylength(__at_).md>) — Sets the size of a block of threadgroup memory.
- [- setStageInRegion:](<setstageinregion(__).md>) — Sets the region of the stage-in attributes to apply to the compute kernel.
- [setStageIn(_:)](<setstagein(__).md>) — Sets the region of the stage-in attributes to apply to the compute kernel.
