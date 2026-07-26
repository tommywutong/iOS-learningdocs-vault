---
title: 'setComputePipelineStates(_:with:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（14.0 起废弃）, iPadOS 13.0+（14.0 起废弃）, tvOS 13.0+（14.0 起废弃）, visionOS]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/metal/mtlargumentencoder/setcomputepipelinestates(_:with:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlargumentencoder/setcomputepipelinestates(_:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargumentencoder/setcomputepipelinestates%28_%3Awith%3A%29.json'
content_hash: 'sha256:9d99f436324c92ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgumentEncoder](../mtlargumentencoder.md)

# setComputePipelineStates(_:with:)

<sub>Instance Method</sub>

Encodes references to an array of compute pipeline states into the argument buffer.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setComputePipelineStates(_ pipelines: UnsafePointer<(any MTLComputePipelineState)?>, with range: NSRange)
```

## Parameters

- `pipelines` — An array of pipeline states the method encodes.

- `range` — A range of indices within the argument buffer for each element in `pipelines`. The values correspond to either the index IDs of declarations in Metal Shading Language (MSL) or the [index](../mtlargumentdescriptor/index.md) property of [MTLArgumentDescriptor](../mtlargumentdescriptor.md) instances.

## See Also

### Encoding pipeline states

- [- setRenderPipelineState:atIndex:](<setrenderpipelinestate(__index_).md>) — Encodes a reference to a render pipeline state into the argument buffer.
- [setRenderPipelineStates(_:range:)](<setrenderpipelinestates(__range_).md>) — Encodes references to an array of render pipeline states into the argument buffer.
- [- setComputePipelineState:atIndex:](<setcomputepipelinestate(__index_).md>) — Encodes a reference to a compute pipeline state into the argument buffer.
- [setComputePipelineState(_:at:)](<setcomputepipelinestate(__at_).md>) — Encodes a reference to a compute pipeline state into the argument buffer.
- [setComputePipelineStates(_:range:)](<setcomputepipelinestates(__range_).md>) — Encodes references to an array of compute pipeline states into the argument buffer.
