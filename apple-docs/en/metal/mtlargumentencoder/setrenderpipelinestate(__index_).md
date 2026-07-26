---
title: 'setRenderPipelineState(_:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlargumentencoder/setrenderpipelinestate(_:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlargumentencoder/setrenderpipelinestate(_:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargumentencoder/setrenderpipelinestate%28_%3Aindex%3A%29.json'
content_hash: 'sha256:c7ffa23b6666d436'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgumentEncoder](../mtlargumentencoder.md)

# setRenderPipelineState(_:index:)

<sub>Instance Method</sub>

Encodes a reference to a render pipeline state into the argument buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setRenderPipelineState(_ pipeline: (any MTLRenderPipelineState)?, index: Int)
```

## Parameters

- `pipeline` — A pipeline state the method encodes.

- `index` — The index of a pipeline state within the argument buffer. The value corresponds to either the index ID of a declaration in Metal Shading Language (MSL) or the [index](../mtlargumentdescriptor/index.md) property of an [MTLArgumentDescriptor](../mtlargumentdescriptor.md) instance.

## See Also

### Encoding pipeline states

- [setRenderPipelineStates(_:range:)](<setrenderpipelinestates(__range_).md>) — Encodes references to an array of render pipeline states into the argument buffer.
- [- setComputePipelineState:atIndex:](<setcomputepipelinestate(__index_).md>) — Encodes a reference to a compute pipeline state into the argument buffer.
- [setComputePipelineStates(_:with:)](<setcomputepipelinestates(__with_).md>) — Encodes references to an array of compute pipeline states into the argument buffer.
- [setComputePipelineState(_:at:)](<setcomputepipelinestate(__at_).md>) — Encodes a reference to a compute pipeline state into the argument buffer.
- [setComputePipelineStates(_:range:)](<setcomputepipelinestates(__range_).md>) — Encodes references to an array of compute pipeline states into the argument buffer.
