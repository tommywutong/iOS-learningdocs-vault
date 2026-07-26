---
title: 'drawMeshThreads(_:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/drawmeshthreads(_:threadsperobjectthreadgroup:threadspermeshthreadgroup:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/drawmeshthreads(_:threadsperobjectthreadgroup:threadspermeshthreadgroup:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/drawmeshthreads%28_%3Athreadsperobjectthreadgroup%3Athreadspermeshthreadgroup%3A%29.json'
content_hash: 'sha256:41872de3398b50f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# drawMeshThreads(_:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:)

<sub>Instance Method</sub>

Encodes a draw command that invokes a mesh shader and, optionally, an object shader with a grid of threads.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func drawMeshThreads(_ threadsPerGrid: MTLSize, threadsPerObjectThreadgroup: MTLSize, threadsPerMeshThreadgroup: MTLSize)
```

## Parameters

- `threadsPerGrid` — An [MTLSize](../mtlsize.md) instance that represents the number of threads for each grid dimension. For mesh shaders, the command rounds the value down to the nearest multiple of `threadsPerMeshThreadgroup` for each dimension. For object shaders, the value doesn’t need to be a multiple of `threadsPerObjectThreadgroup`.

- `threadsPerObjectThreadgroup` — An [MTLSize](../mtlsize.md) instance that represents the number of threads in an object shader threadgroup, if applicable.

- `threadsPerMeshThreadgroup` — An [MTLSize](../mtlsize.md) instance that represents the number of threads in a mesh shader threadgroup.

## See Also

### Drawing with meshes

- [- drawMeshThreadgroups:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:](<drawmeshthreadgroups(__threadsperobjectthreadgroup_threadspermeshthreadgroup_).md>) — Encodes a draw command that invokes a mesh shader and, optionally, an object shader with a grid of threadgroups.
- [- drawMeshThreadgroupsWithIndirectBuffer:indirectBufferOffset:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:](<drawmeshthreadgroups(indirectbuffer_indirectbufferoffset_threadsperobjectthreadgroup_threadspermeshthreadgroup_).md>) — Encodes a draw command that invokes a mesh shader and, optionally, an object shader with indirect arguments.
