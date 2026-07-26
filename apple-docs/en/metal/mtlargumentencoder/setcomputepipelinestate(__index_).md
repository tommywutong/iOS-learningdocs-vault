---
title: 'setComputePipelineState(_:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlargumentencoder/setcomputepipelinestate(_:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlargumentencoder/setcomputepipelinestate(_:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargumentencoder/setcomputepipelinestate%28_%3Aindex%3A%29.json'
content_hash: 'sha256:1c2b455da70c65d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgumentEncoder](../mtlargumentencoder.md)

# setComputePipelineState(_:index:)

<sub>Instance Method</sub>

Encodes a reference to a compute pipeline state into the argument buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setComputePipelineState(_ pipeline: (any MTLComputePipelineState)?, index: Int)
```

## Parameters

- `pipeline` — A pipeline state the method encodes.

- `index` — The index of a pipeline state within the argument buffer. The value corresponds to either the index ID of a declaration in Metal Shading Language (MSL) or the [index](../mtlargumentdescriptor/index.md) property of an [MTLArgumentDescriptor](../mtlargumentdescriptor.md) instance.

## See Also

### Encoding pipeline states

- [- setRenderPipelineState:atIndex:](<setrenderpipelinestate(__index_).md>) — Encodes a reference to a render pipeline state into the argument buffer.
- [setRenderPipelineStates(_:range:)](<setrenderpipelinestates(__range_).md>) — Encodes references to an array of render pipeline states into the argument buffer.
- [setComputePipelineStates(_:with:)](<setcomputepipelinestates(__with_).md>) — Encodes references to an array of compute pipeline states into the argument buffer.
- [setComputePipelineState(_:at:)](<setcomputepipelinestate(__at_).md>) — Encodes a reference to a compute pipeline state into the argument buffer.
- [setComputePipelineStates(_:range:)](<setcomputepipelinestates(__range_).md>) — Encodes references to an array of compute pipeline states into the argument buffer.
