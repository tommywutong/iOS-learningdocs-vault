---
title: maxTotalThreadgroupsPerMeshGrid
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinestate/maxtotalthreadgroupspermeshgrid
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinestate/maxtotalthreadgroupspermeshgrid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinestate/maxtotalthreadgroupspermeshgrid.json'
content_hash: 'sha256:b3e21df9aac2224c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineState](../mtlrenderpipelinestate.md)

# maxTotalThreadgroupsPerMeshGrid

<sub>Instance Property</sub>

The largest number of threadgroups the pipeline state can have in a single mesh shader grid.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var maxTotalThreadgroupsPerMeshGrid: Int { get }
```

## See Also

### Checking mesh shader memory requirements

- [maxTotalThreadsPerMeshThreadgroup](maxtotalthreadspermeshthreadgroup.md) — The largest number of threads the pipeline state can have in a single mesh shader threadgroup.
- [meshThreadExecutionWidth](meshthreadexecutionwidth.md) — The number of threads the render pass applies to a SIMD group for a mesh shader.
