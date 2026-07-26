---
title: maxTotalThreadsPerObjectThreadgroup
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinestate/maxtotalthreadsperobjectthreadgroup
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinestate/maxtotalthreadsperobjectthreadgroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinestate/maxtotalthreadsperobjectthreadgroup.json'
content_hash: 'sha256:d61be226e70b2dc1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineState](../mtlrenderpipelinestate.md)

# maxTotalThreadsPerObjectThreadgroup

<sub>Instance Property</sub>

The largest number of threads the pipeline state can have in a single object shader threadgroup.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var maxTotalThreadsPerObjectThreadgroup: Int { get }
```

## See Also

### Checking object shader memory requirements

- [objectThreadExecutionWidth](objectthreadexecutionwidth.md) — The number of threads the render pass applies to a SIMD group for an object shader.
