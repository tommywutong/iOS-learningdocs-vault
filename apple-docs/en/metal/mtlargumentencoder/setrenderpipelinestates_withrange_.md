---
title: 'setRenderPipelineStates:withRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 13.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlargumentencoder/setrenderpipelinestates:withrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtlargumentencoder/setrenderpipelinestates:withrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargumentencoder/setrenderpipelinestates%3Awithrange%3A.json'
content_hash: 'sha256:07f2aa5b793df412'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgumentEncoder](../mtlargumentencoder.md)

# setRenderPipelineStates:withRange:

<sub>Instance Method</sub>

Encodes references to an array of render pipeline states into the argument buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setRenderPipelineStates:(id<MTLRenderPipelineState> const[]) pipelines withRange:(NSRange) range;
```

## Parameters

- `pipelines` — An array of pipeline states the method encodes.

- `range` — A range of indices within the argument buffer for each element in `pipelines`. The values correspond to either the index IDs of declarations in Metal Shading Language (MSL) or the [index](../mtlargumentdescriptor/index.md) property of [MTLArgumentDescriptor](../mtlargumentdescriptor.md) instances.

## See Also

### Encoding pipeline states

- [- setRenderPipelineState:atIndex:](<setrenderpipelinestate(__index_).md>) — Encodes a reference to a render pipeline state into the argument buffer.
- [- setComputePipelineState:atIndex:](<setcomputepipelinestate(__index_).md>) — Encodes a reference to a compute pipeline state into the argument buffer.
- [setComputePipelineStates:withRange:](setcomputepipelinestates_withrange_.md) — Encodes references to an array of compute pipeline states into the argument buffer.
