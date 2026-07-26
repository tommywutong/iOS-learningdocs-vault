---
title: 'setArgumentTable(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4computecommandencoder/setargumenttable(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4computecommandencoder/setargumenttable(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4computecommandencoder/setargumenttable%28_%3A%29.json'
content_hash: 'sha256:e31fa72576ad7ea7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4ComputeCommandEncoder](../mtl4computecommandencoder.md)

# setArgumentTable(_:)

<sub>Instance Method</sub>

Sets an argument table for the compute shader stage of this pipeline.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setArgumentTable(_ argumentTable: (any MTL4ArgumentTable)?)
```

## Parameters

- `argumentTable` — A [MTL4ArgumentTable](../mtl4argumenttable.md) to set on the command encoder.

## Discussion

Metal takes a snapshot of the resources in the argument table when you make dispatch or execute calls on this encoder instance. Metal makes the snapshot contents available to the compute shader function of the current pipeline state.

## See Also

### Configuring the pass

- [- setComputePipelineState:](<setcomputepipelinestate(__).md>) — Configures this encoder with a compute pipeline state that applies to your subsequent dispatch commands.
- [- setThreadgroupMemoryLength:atIndex:](<setthreadgroupmemorylength(__index_).md>) — Configures the size of a threadgroup memory buffer for a threadgroup argument in the compute shader function.
- [- setImageblockWidth:height:](<setimageblocksize(width_height_).md>) — Specifies the size, in pixels, of imageblock data in tile memory.
