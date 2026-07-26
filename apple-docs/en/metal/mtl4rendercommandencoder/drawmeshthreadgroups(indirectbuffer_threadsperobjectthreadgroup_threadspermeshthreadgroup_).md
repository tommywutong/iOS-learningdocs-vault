---
title: 'drawMeshThreadgroups(indirectBuffer:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4rendercommandencoder/drawmeshthreadgroups(indirectbuffer:threadsperobjectthreadgroup:threadspermeshthreadgroup:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/drawmeshthreadgroups(indirectbuffer:threadsperobjectthreadgroup:threadspermeshthreadgroup:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4rendercommandencoder/drawmeshthreadgroups%28indirectbuffer%3Athreadsperobjectthreadgroup%3Athreadspermeshthreadgroup%3A%29.json'
content_hash: 'sha256:d01a5d8b65955515'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderCommandEncoder](../mtl4rendercommandencoder.md)

# drawMeshThreadgroups(indirectBuffer:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:)

<sub>Instance Method</sub>

Encodes a draw command that invokes a mesh shader and, optionally, an object shader with indirect arguments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func drawMeshThreadgroups(indirectBuffer: MTLGPUAddress, threadsPerObjectThreadgroup: MTLSize, threadsPerMeshThreadgroup: MTLSize)
```

## Parameters

- `indirectBuffer` — GPUAddress of an [MTLBuffer](../mtlbuffer.md) instance with data that matches the layout of the [MTLDispatchThreadgroupsIndirectArguments](../mtldispatchthreadgroupsindirectarguments.md) structure. This address requires 4-byte alignment.

- `threadsPerObjectThreadgroup` — A [MTLSize](../mtlsize.md) instance that represents the number of threads in an object shader threadgroup, if applicable.

- `threadsPerMeshThreadgroup` — A [MTLSize](../mtlsize.md) instance that represents the number of threads in a mesh shader threadgroup.

## Discussion

This method enables you to determine the number of threadgroups per grid indirectly, in the GPU timeline. Metal expects this buffer’s contents to match the layout of structure [MTLDispatchThreadgroupsIndirectArguments](../mtldispatchthreadgroupsindirectarguments.md). You are responsible for ensuring the address of this buffer has 4-byte alignment.

Use an instance of [MTLResidencySet](../mtlresidencyset.md) to mark residency of the indirect buffer that the `indirectBuffer` parameter references.

## See Also

### Drawing with meshes

- [- drawMeshThreads:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:](<drawmeshthreads(threadspergrid_threadsperobjectthreadgroup_threadspermeshthreadgroup_).md>) — Encodes a draw command that invokes a mesh shader and, optionally, an object shader with a grid of threads.
- [- drawMeshThreadgroups:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:](<drawmeshthreadgroups(threadgroupspergrid_threadsperobjectthreadgroup_threadspermeshthreadgroup_).md>) — Encodes a draw command that invokes a mesh shader and, optionally, an object shader with a grid of threadgroups.
