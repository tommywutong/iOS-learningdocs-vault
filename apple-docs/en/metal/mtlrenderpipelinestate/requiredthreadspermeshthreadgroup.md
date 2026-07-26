---
title: requiredThreadsPerMeshThreadgroup
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinestate/requiredthreadspermeshthreadgroup
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinestate/requiredthreadspermeshthreadgroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinestate/requiredthreadspermeshthreadgroup.json'
content_hash: 'sha256:3d3c68178df13828'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineState](../mtlrenderpipelinestate.md)

# requiredThreadsPerMeshThreadgroup

<sub>Instance Property</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var requiredThreadsPerMeshThreadgroup: MTLSize { get }
```

## Discussion

The required size of every mesh shader threadgroup.

This value is set in MTLMeshRenderPipelineDescriptor.
