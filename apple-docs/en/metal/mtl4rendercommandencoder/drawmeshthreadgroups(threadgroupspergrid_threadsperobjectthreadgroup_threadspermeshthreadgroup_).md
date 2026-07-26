---
title: 'drawMeshThreadgroups(threadgroupsPerGrid:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4rendercommandencoder/drawmeshthreadgroups(threadgroupspergrid:threadsperobjectthreadgroup:threadspermeshthreadgroup:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/drawmeshthreadgroups(threadgroupspergrid:threadsperobjectthreadgroup:threadspermeshthreadgroup:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4rendercommandencoder/drawmeshthreadgroups%28threadgroupspergrid%3Athreadsperobjectthreadgroup%3Athreadspermeshthreadgroup%3A%29.json'
content_hash: 'sha256:0723f5b74337dcfd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderCommandEncoder](../mtl4rendercommandencoder.md)

# drawMeshThreadgroups(threadgroupsPerGrid:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:)

<sub>Instance Method</sub>

Encodes a draw command that invokes a mesh shader and, optionally, an object shader with a grid of threadgroups.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func drawMeshThreadgroups(threadgroupsPerGrid: MTLSize, threadsPerObjectThreadgroup: MTLSize, threadsPerMeshThreadgroup: MTLSize)
```

## Parameters

- `threadgroupsPerGrid` — A [MTLSize](../mtlsize.md) instance that represents the number of threadgroups for each grid dimension.

- `threadsPerObjectThreadgroup` — A [MTLSize](../mtlsize.md) instance that represents the number of threads in an object shader threadgroup, if applicable.

- `threadsPerMeshThreadgroup` — A [MTLSize](../mtlsize.md) instance that represents the number of threads in a mesh shader threadgroup.

## See Also

### Drawing with meshes

- [- drawMeshThreads:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:](<drawmeshthreads(threadspergrid_threadsperobjectthreadgroup_threadspermeshthreadgroup_).md>) — Encodes a draw command that invokes a mesh shader and, optionally, an object shader with a grid of threads.
- [- drawMeshThreadgroupsWithIndirectBuffer:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:](<drawmeshthreadgroups(indirectbuffer_threadsperobjectthreadgroup_threadspermeshthreadgroup_).md>) — Encodes a draw command that invokes a mesh shader and, optionally, an object shader with indirect arguments.
