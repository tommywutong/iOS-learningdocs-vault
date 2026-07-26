---
title: 'setComputePipelineState(_:at:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（14.0 起废弃）, iPadOS 13.0+（14.0 起废弃）, tvOS 13.0+（14.0 起废弃）, visionOS]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/metal/mtlargumentencoder/setcomputepipelinestate(_:at:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlargumentencoder/setcomputepipelinestate(_:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargumentencoder/setcomputepipelinestate%28_%3Aat%3A%29.json'
content_hash: 'sha256:87f272393b03f54c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgumentEncoder](../mtlargumentencoder.md)

# setComputePipelineState(_:at:)

<sub>Instance Method</sub>

Encodes a reference to a compute pipeline state into the argument buffer.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setComputePipelineState(_ pipeline: (any MTLComputePipelineState)?, at index: Int)
```

## Parameters

- `pipeline` — A pipeline state the method encodes.

- `index` — The index of a pipeline state within the argument buffer. The value corresponds to either the index ID of a declaration in Metal Shading Language (MSL) or the [index](../mtlargumentdescriptor/index.md) property of an [MTLArgumentDescriptor](../mtlargumentdescriptor.md) instance.

## See Also

### Encoding pipeline states

- [- setRenderPipelineState:atIndex:](<setrenderpipelinestate(__index_).md>) — Encodes a reference to a render pipeline state into the argument buffer.
- [setRenderPipelineStates(_:range:)](<setrenderpipelinestates(__range_).md>) — Encodes references to an array of render pipeline states into the argument buffer.
- [- setComputePipelineState:atIndex:](<setcomputepipelinestate(__index_).md>) — Encodes a reference to a compute pipeline state into the argument buffer.
- [setComputePipelineStates(_:with:)](<setcomputepipelinestates(__with_).md>) — Encodes references to an array of compute pipeline states into the argument buffer.
- [setComputePipelineStates(_:range:)](<setcomputepipelinestates(__range_).md>) — Encodes references to an array of compute pipeline states into the argument buffer.
