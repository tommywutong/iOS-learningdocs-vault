---
title: maxVertexAmplificationCount
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4renderpipelinedescriptor/maxvertexamplificationcount
source_url: 'https://developer.apple.com/documentation/metal/mtl4renderpipelinedescriptor/maxvertexamplificationcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4renderpipelinedescriptor/maxvertexamplificationcount.json'
content_hash: 'sha256:af59fa8ff7d2622d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderPipelineDescriptor](../mtl4renderpipelinedescriptor.md)

# maxVertexAmplificationCount

<sub>Instance Property</sub>

Determines the maximum value that can you can pass as the pipeline’s amplification count.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var maxVertexAmplificationCount: Int { get set }
```

## Discussion

This property controls the maximum count you pass to [setVertexAmplificationCount:viewMappings:](../mtl4rendercommandencoder/setvertexamplificationcount_viewmappings_.md) when using vertex amplification with this pipeline.
