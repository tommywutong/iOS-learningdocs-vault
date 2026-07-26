---
title: 'drawMeshThreadgroups(indirectBuffer:indirectBufferOffset:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/drawmeshthreadgroups(indirectbuffer:indirectbufferoffset:threadsperobjectthreadgroup:threadspermeshthreadgroup:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/drawmeshthreadgroups(indirectbuffer:indirectbufferoffset:threadsperobjectthreadgroup:threadspermeshthreadgroup:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/drawmeshthreadgroups%28indirectbuffer%3Aindirectbufferoffset%3Athreadsperobjectthreadgroup%3Athreadspermeshthreadgroup%3A%29.json'
content_hash: 'sha256:f63233deaa00c193'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# drawMeshThreadgroups(indirectBuffer:indirectBufferOffset:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:)

<sub>Instance Method</sub>

Encodes a draw command that invokes a mesh shader and, optionally, an object shader with indirect arguments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func drawMeshThreadgroups(indirectBuffer: any MTLBuffer, indirectBufferOffset: Int, threadsPerObjectThreadgroup: MTLSize, threadsPerMeshThreadgroup: MTLSize)
```

## Parameters

- `indirectBuffer` — An [MTLBuffer](../mtlbuffer.md) instance with data that matches the layout of the [MTLDispatchThreadgroupsIndirectArguments](../mtldispatchthreadgroupsindirectarguments.md) structure.

- `indirectBufferOffset` — An integer that represents the location, in bytes, from the start of `indirectBuffer` where the indirect arguments structure begins. See the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) to check for offset alignment requirements for buffers in `device` and `constant` address space.

- `threadsPerObjectThreadgroup` — An [MTLSize](../mtlsize.md) instance that represents the number of threads in an object shader threadgroup, if applicable.

- `threadsPerMeshThreadgroup` — An [MTLSize](../mtlsize.md) instance that represents the number of threads in a mesh shader threadgroup.

## See Also

### Drawing with meshes

- [- drawMeshThreads:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:](<drawmeshthreads(__threadsperobjectthreadgroup_threadspermeshthreadgroup_).md>) — Encodes a draw command that invokes a mesh shader and, optionally, an object shader with a grid of threads.
- [- drawMeshThreadgroups:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:](<drawmeshthreadgroups(__threadsperobjectthreadgroup_threadspermeshthreadgroup_).md>) — Encodes a draw command that invokes a mesh shader and, optionally, an object shader with a grid of threadgroups.
