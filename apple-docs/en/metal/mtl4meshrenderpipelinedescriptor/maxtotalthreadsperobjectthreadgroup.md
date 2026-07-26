---
title: maxTotalThreadsPerObjectThreadgroup
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4meshrenderpipelinedescriptor/maxtotalthreadsperobjectthreadgroup
source_url: 'https://developer.apple.com/documentation/metal/mtl4meshrenderpipelinedescriptor/maxtotalthreadsperobjectthreadgroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4meshrenderpipelinedescriptor/maxtotalthreadsperobjectthreadgroup.json'
content_hash: 'sha256:b3ce27ff416042b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4MeshRenderPipelineDescriptor](../mtl4meshrenderpipelinedescriptor.md)

# maxTotalThreadsPerObjectThreadgroup

<sub>Instance Property</sub>

Controls the largest number of threads the pipeline state can execute in a single object shader threadgroup dispatch.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var maxTotalThreadsPerObjectThreadgroup: Int { get set }
```

## Discussion

This number represents the maximum size of the product of the components of parameter `threadsPerObjectThreadgroup` that Metal can use when drawing with this pipeline in mesh shader dispatch methods, such as [- drawMeshThreadgroups:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:](<../mtl4rendercommandencoder/drawmeshthreadgroups(threadgroupspergrid_threadsperobjectthreadgroup_threadspermeshthreadgroup_).md>).

The compiler’s optimizer can use the value of this property to generate more efficient code, specifically when the value doesn’t exceed the thread execution width of the underlying GPU.

The default value of this property is `0`, which indicates that the number you pass to attribute `[[max_total_threads_per_threadgroup(N)]]` of the pipeline’s object function determines the maximum total threads per threadgroup.

When you specify both the `[[max_total_threads_per_threadgroup(N)]]` attribute and this property, you are responsible for making sure these values match.

Additionally, you are responsible for ensuring this value doesn’t exceed the “maximum threads per threadgroup” device limit documented in the “Metal Feature Set Tables” PDF: [https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf).
