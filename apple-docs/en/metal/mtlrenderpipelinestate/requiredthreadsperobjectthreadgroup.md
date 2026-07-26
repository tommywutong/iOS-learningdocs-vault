---
title: requiredThreadsPerObjectThreadgroup
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinestate/requiredthreadsperobjectthreadgroup
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinestate/requiredthreadsperobjectthreadgroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinestate/requiredthreadsperobjectthreadgroup.json'
content_hash: 'sha256:1cd033328c3e1450'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineState](../mtlrenderpipelinestate.md)

# requiredThreadsPerObjectThreadgroup

<sub>Instance Property</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var requiredThreadsPerObjectThreadgroup: MTLSize { get }
```

## Discussion

The required size of every object shader threadgroup.

This value is set in MTLMeshRenderPipelineDescriptor.
