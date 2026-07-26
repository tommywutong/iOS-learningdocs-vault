---
title: 'setImageblockSize(width:height:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4computecommandencoder/setimageblocksize(width:height:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4computecommandencoder/setimageblocksize(width:height:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4computecommandencoder/setimageblocksize%28width%3Aheight%3A%29.json'
content_hash: 'sha256:e53fed689af2b89f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4ComputeCommandEncoder](../mtl4computecommandencoder.md)

# setImageblockSize(width:height:)

<sub>Instance Method</sub>

Specifies the size, in pixels, of imageblock data in tile memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setImageblockSize(width: Int, height: Int)
```

## Parameters

- `width` — The width of the imageblock, in pixels.

- `height` — The height of the imageblock, in pixels.

## See Also

### Configuring the pass

- [- setComputePipelineState:](<setcomputepipelinestate(__).md>) — Configures this encoder with a compute pipeline state that applies to your subsequent dispatch commands.
- [- setArgumentTable:](<setargumenttable(__).md>) — Sets an argument table for the compute shader stage of this pipeline.
- [- setThreadgroupMemoryLength:atIndex:](<setthreadgroupmemorylength(__index_).md>) — Configures the size of a threadgroup memory buffer for a threadgroup argument in the compute shader function.
