---
title: 'setComputePipelineStates(_:range:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 13.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlargumentencoder/setcomputepipelinestates(_:range:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlargumentencoder/setcomputepipelinestates(_:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargumentencoder/setcomputepipelinestates%28_%3Arange%3A%29.json'
content_hash: 'sha256:44029501023ed21e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgumentEncoder](../mtlargumentencoder.md)

# setComputePipelineStates(_:range:)

<sub>Instance Method</sub>

Encodes references to an array of compute pipeline states into the argument buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setComputePipelineStates(_ pipelines: [(any MTLComputePipelineState)?], range: Range<Int>)
```

## Parameters

- `pipelines` — An array of pipeline states the method encodes.

- `range` — A range of indices within the argument buffer for each element in `pipelines`. The values correspond to either the index IDs of declarations in Metal Shading Language (MSL) or the [index](../mtlargumentdescriptor/index.md) property of [MTLArgumentDescriptor](../mtlargumentdescriptor.md) instances.

## See Also

### Encoding pipeline states

- [- setRenderPipelineState:atIndex:](<setrenderpipelinestate(__index_).md>) — Encodes a reference to a render pipeline state into the argument buffer.
- [setRenderPipelineStates(_:range:)](<setrenderpipelinestates(__range_).md>) — Encodes references to an array of render pipeline states into the argument buffer.
- [- setComputePipelineState:atIndex:](<setcomputepipelinestate(__index_).md>) — Encodes a reference to a compute pipeline state into the argument buffer.
- [setComputePipelineStates(_:with:)](<setcomputepipelinestates(__with_).md>) — Encodes references to an array of compute pipeline states into the argument buffer.
- [setComputePipelineState(_:at:)](<setcomputepipelinestate(__at_).md>) — Encodes a reference to a compute pipeline state into the argument buffer.
