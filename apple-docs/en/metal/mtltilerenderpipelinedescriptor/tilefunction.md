---
title: tileFunction
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltilerenderpipelinedescriptor/tilefunction
source_url: 'https://developer.apple.com/documentation/metal/mtltilerenderpipelinedescriptor/tilefunction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltilerenderpipelinedescriptor/tilefunction.json'
content_hash: 'sha256:076d8147ed6fa7a0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTileRenderPipelineDescriptor](../mtltilerenderpipelinedescriptor.md)

# tileFunction

<sub>Instance Property</sub>

The compute kernel or fragment function the pipeline calls.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var tileFunction: any MTLFunction { get set }
```

## Discussion

Kernel-based and fragment-based tile pipeline dispatches act as a barrier against previous draw commands and other dispatches. Kernel-based pipelines wait until all prior access to the tile completes. Fragment-based pipelines wait only until all prior access to the fragment’s location completes.

## See Also

### Specifying graphics functions and associated data

- [tileBuffers](tilebuffers.md) — An array that contains the buffer mutability options for a render pipeline’s tile function.
- [maxCallStackDepth](maxcallstackdepth.md) — The maximum call stack depth for indirect function calls in tile shaders.
