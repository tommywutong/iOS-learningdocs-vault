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
doc_path: /documentation/metal/mtl4meshrenderpipelinedescriptor/requiredthreadsperobjectthreadgroup
source_url: 'https://developer.apple.com/documentation/metal/mtl4meshrenderpipelinedescriptor/requiredthreadsperobjectthreadgroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4meshrenderpipelinedescriptor/requiredthreadsperobjectthreadgroup.json'
content_hash: 'sha256:7cf24f421f4e6150'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4MeshRenderPipelineDescriptor](../mtl4meshrenderpipelinedescriptor.md)

# requiredThreadsPerObjectThreadgroup

<sub>Instance Property</sub>

Controls the required number of object threads-per-threadgroup when drawing with a mesh shader pipeline you create from this descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var requiredThreadsPerObjectThreadgroup: MTLSize { get set }
```

## Discussion

This argument is optional, unless this pipeline uses `CooperativeTensors`, in which case you are responsible for providing it.

When this value is set to non-zero, you are responsible for ensuring the parameter `threadsPerObjectThreadgroup` in any mesh dispatch draw calls that use this mesh render pipeline, such as [- drawMeshThreadgroups:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:](<../mtl4rendercommandencoder/drawmeshthreadgroups(threadgroupspergrid_threadsperobjectthreadgroup_threadspermeshthreadgroup_).md>), match it.

Setting this value to a size of 0 in every dimension disables this property.
