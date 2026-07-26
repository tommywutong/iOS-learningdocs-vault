---
title: 'setStageIn(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（14.0 起废弃）, iPadOS 13.0+（14.0 起废弃）, Mac Catalyst 14.0+（14.0 起废弃）, tvOS 13.0+（14.0 起废弃）, visionOS]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/metal/mtlindirectcomputecommand/setstagein(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlindirectcomputecommand/setstagein(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlindirectcomputecommand/setstagein%28_%3A%29.json'
content_hash: 'sha256:52c5e2691ab61a82'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIndirectComputeCommand](../mtlindirectcomputecommand.md)

# setStageIn(_:)

<sub>Instance Method</sub>

Sets the region of the stage-in attributes to apply to the compute kernel.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setStageIn(_ region: MTLRegion)
```

## Parameters

- `region` — The offset and maximum size of the grid over which compute threads that read per-thread stage-in data are launched.

## See Also

### Setting a command’s arguments

- [- setComputePipelineState:](<setcomputepipelinestate(__).md>) — Sets the command’s compute pipeline state.
- [- setImageblockWidth:height:](<setimageblockwidth(__height_).md>) — Sets the size, in pixels, of the imageblock.
- [- setKernelBuffer:offset:atIndex:](<setkernelbuffer(__offset_at_).md>) — Sets a buffer for the compute function.
- [- setThreadgroupMemoryLength:atIndex:](<setthreadgroupmemorylength(__index_).md>) — Sets the size of a block of threadgroup memory.
- [setThreadgroupMemoryLength(_:at:)](<setthreadgroupmemorylength(__at_).md>) — Sets the size of a block of threadgroup memory.
- [- setStageInRegion:](<setstageinregion(__).md>) — Sets the region of the stage-in attributes to apply to the compute kernel.
