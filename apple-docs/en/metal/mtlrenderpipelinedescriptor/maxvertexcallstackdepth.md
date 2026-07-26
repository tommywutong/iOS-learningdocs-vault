---
title: maxVertexCallStackDepth
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinedescriptor/maxvertexcallstackdepth
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/maxvertexcallstackdepth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinedescriptor/maxvertexcallstackdepth.json'
content_hash: 'sha256:e65b0ae67edaf87f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineDescriptor](../mtlrenderpipelinedescriptor.md)

# maxVertexCallStackDepth

<sub>Instance Property</sub>

The maximum function call depth from the top-most vertex shader function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var maxVertexCallStackDepth: Int { get set }
```

## Discussion

The default value is 1.

## See Also

### Specifying graphics functions and associated data

- [vertexFunction](vertexfunction.md) — The vertex function the pipeline calls to process vertices.
- [fragmentFunction](fragmentfunction.md) — The fragment function the pipeline calls to process fragments.
- [maxFragmentCallStackDepth](maxfragmentcallstackdepth.md) — The maximum function call depth from the top-most fragment shader function.
