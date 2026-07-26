---
title: tileBuffers
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltilerenderpipelinedescriptor/tilebuffers
source_url: 'https://developer.apple.com/documentation/metal/mtltilerenderpipelinedescriptor/tilebuffers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltilerenderpipelinedescriptor/tilebuffers.json'
content_hash: 'sha256:2ddd74a71d85ba6d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTileRenderPipelineDescriptor](../mtltilerenderpipelinedescriptor.md)

# tileBuffers

<sub>Instance Property</sub>

An array that contains the buffer mutability options for a render pipeline’s tile function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var tileBuffers: MTLPipelineBufferDescriptorArray { get }
```

## Discussion

This property returns an array of [MTLPipelineBufferDescriptor](../mtlpipelinebufferdescriptor.md) objects, with each array index corresponding to the same index in the buffer argument table for the render pipeline’s tile shader.

## See Also

### Specifying graphics functions and associated data

- [tileFunction](tilefunction.md) — The compute kernel or fragment function the pipeline calls.
- [maxCallStackDepth](maxcallstackdepth.md) — The maximum call stack depth for indirect function calls in tile shaders.
