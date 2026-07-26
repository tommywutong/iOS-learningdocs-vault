---
title: fragmentFunction
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinedescriptor/fragmentfunction
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/fragmentfunction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinedescriptor/fragmentfunction.json'
content_hash: 'sha256:cc0009f8f25c9a50'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineDescriptor](../mtlrenderpipelinedescriptor.md)

# fragmentFunction

<sub>Instance Property</sub>

The fragment function the pipeline calls to process fragments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var fragmentFunction: (any MTLFunction)? { get set }
```

## Discussion

The default value is `nil`. If this value is `nil`, then there is no fragment function and therefore no writes to the color render target occur. Depth and stencil writes and visibility result counting can still proceed.

## See Also

### Specifying graphics functions and associated data

- [vertexFunction](vertexfunction.md) — The vertex function the pipeline calls to process vertices.
- [maxVertexCallStackDepth](maxvertexcallstackdepth.md) — The maximum function call depth from the top-most vertex shader function.
- [maxFragmentCallStackDepth](maxfragmentcallstackdepth.md) — The maximum function call depth from the top-most fragment shader function.
