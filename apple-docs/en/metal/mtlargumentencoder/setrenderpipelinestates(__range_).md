---
title: 'setRenderPipelineStates(_:range:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 13.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlargumentencoder/setrenderpipelinestates(_:range:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlargumentencoder/setrenderpipelinestates(_:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargumentencoder/setrenderpipelinestates%28_%3Arange%3A%29.json'
content_hash: 'sha256:bf97eb4152dac23b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgumentEncoder](../mtlargumentencoder.md)

# setRenderPipelineStates(_:range:)

<sub>Instance Method</sub>

Encodes references to an array of render pipeline states into the argument buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setRenderPipelineStates(_ pipelines: [(any MTLRenderPipelineState)?], range: Range<Int>)
```

## Parameters

- `pipelines` — An array of pipeline states the method encodes.

- `range` — A range of indices within the argument buffer for each element in `pipelines`. The values correspond to either the index IDs of declarations in Metal Shading Language (MSL) or the [index](../mtlargumentdescriptor/index.md) property of [MTLArgumentDescriptor](../mtlargumentdescriptor.md) instances.

## See Also

### Encoding pipeline states

- [- setRenderPipelineState:atIndex:](<setrenderpipelinestate(__index_).md>) — Encodes a reference to a render pipeline state into the argument buffer.
- [- setComputePipelineState:atIndex:](<setcomputepipelinestate(__index_).md>) — Encodes a reference to a compute pipeline state into the argument buffer.
- [setComputePipelineStates(_:with:)](<setcomputepipelinestates(__with_).md>) — Encodes references to an array of compute pipeline states into the argument buffer.
- [setComputePipelineState(_:at:)](<setcomputepipelinestate(__at_).md>) — Encodes a reference to a compute pipeline state into the argument buffer.
- [setComputePipelineStates(_:range:)](<setcomputepipelinestates(__range_).md>) — Encodes references to an array of compute pipeline states into the argument buffer.
