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
doc_path: /documentation/metal/mtlmeshrenderpipelinedescriptor/requiredthreadsperobjectthreadgroup
source_url: 'https://developer.apple.com/documentation/metal/mtlmeshrenderpipelinedescriptor/requiredthreadsperobjectthreadgroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlmeshrenderpipelinedescriptor/requiredthreadsperobjectthreadgroup.json'
content_hash: 'sha256:628e4a50b04fd49a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLMeshRenderPipelineDescriptor](../mtlmeshrenderpipelinedescriptor.md)

# requiredThreadsPerObjectThreadgroup

<sub>Instance Property</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var requiredThreadsPerObjectThreadgroup: MTLSize { get set }
```

## Discussion

Sets the required object threads-per-threadgroup during mesh draws. The `threadsPerObjectThreadgroup` argument of any draw must match to this value if it is set. Setting this to a size of 0 in every dimension disables this property
