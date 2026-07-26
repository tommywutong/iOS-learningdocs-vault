---
title: 'setThreadgroupMemoryLength(_:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4computecommandencoder/setthreadgroupmemorylength(_:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4computecommandencoder/setthreadgroupmemorylength(_:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4computecommandencoder/setthreadgroupmemorylength%28_%3Aindex%3A%29.json'
content_hash: 'sha256:b61e1eae7ab4157a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4ComputeCommandEncoder](../mtl4computecommandencoder.md)

# setThreadgroupMemoryLength(_:index:)

<sub>Instance Method</sub>

Configures the size of a threadgroup memory buffer for a threadgroup argument in the compute shader function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setThreadgroupMemoryLength(_ length: Int, index: Int)
```

## Parameters

- `length` — The size of the threadgroup memory, in bytes. Use a multiple of `16` bytes.

- `index` — An integer that corresponds to the index of the argument you annotate with attribute `[[threadgroup(index)]]` in the shader function.

## See Also

### Configuring the pass

- [- setComputePipelineState:](<setcomputepipelinestate(__).md>) — Configures this encoder with a compute pipeline state that applies to your subsequent dispatch commands.
- [- setArgumentTable:](<setargumenttable(__).md>) — Sets an argument table for the compute shader stage of this pipeline.
- [- setImageblockWidth:height:](<setimageblocksize(width_height_).md>) — Specifies the size, in pixels, of imageblock data in tile memory.
