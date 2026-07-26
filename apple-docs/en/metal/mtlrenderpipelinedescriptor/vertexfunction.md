---
title: vertexFunction
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinedescriptor/vertexfunction
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/vertexfunction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinedescriptor/vertexfunction.json'
content_hash: 'sha256:e06c13c92ba4f0c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineDescriptor](../mtlrenderpipelinedescriptor.md)

# vertexFunction

<sub>Instance Property</sub>

The vertex function the pipeline calls to process vertices.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var vertexFunction: (any MTLFunction)? { get set }
```

## Discussion

The default value is `nil`. The vertex function needs to be specified. The vertex function can be either a regular vertex function or a post-tessellation vertex function.

## See Also

### Specifying graphics functions and associated data

- [fragmentFunction](fragmentfunction.md) — The fragment function the pipeline calls to process fragments.
- [maxVertexCallStackDepth](maxvertexcallstackdepth.md) — The maximum function call depth from the top-most vertex shader function.
- [maxFragmentCallStackDepth](maxfragmentcallstackdepth.md) — The maximum function call depth from the top-most fragment shader function.
