---
title: 'setComputePipelineState(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4computecommandencoder/setcomputepipelinestate(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4computecommandencoder/setcomputepipelinestate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4computecommandencoder/setcomputepipelinestate%28_%3A%29.json'
content_hash: 'sha256:4a9044b231164616'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4ComputeCommandEncoder](../mtl4computecommandencoder.md)

# setComputePipelineState(_:)

<sub>Instance Method</sub>

Configures this encoder with a compute pipeline state that applies to your subsequent dispatch commands.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setComputePipelineState(_ state: any MTLComputePipelineState)
```

## Parameters

- `state` — A non-`nil` [MTLComputePipelineState](../mtlcomputepipelinestate.md).

## See Also

### Configuring the pass

- [- setArgumentTable:](<setargumenttable(__).md>) — Sets an argument table for the compute shader stage of this pipeline.
- [- setThreadgroupMemoryLength:atIndex:](<setthreadgroupmemorylength(__index_).md>) — Configures the size of a threadgroup memory buffer for a threadgroup argument in the compute shader function.
- [- setImageblockWidth:height:](<setimageblocksize(width_height_).md>) — Specifies the size, in pixels, of imageblock data in tile memory.
