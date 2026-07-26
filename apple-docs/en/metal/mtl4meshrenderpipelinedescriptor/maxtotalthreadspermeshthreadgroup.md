---
title: maxTotalThreadsPerMeshThreadgroup
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4meshrenderpipelinedescriptor/maxtotalthreadspermeshthreadgroup
source_url: 'https://developer.apple.com/documentation/metal/mtl4meshrenderpipelinedescriptor/maxtotalthreadspermeshthreadgroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4meshrenderpipelinedescriptor/maxtotalthreadspermeshthreadgroup.json'
content_hash: 'sha256:17eee88c0c4134a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4MeshRenderPipelineDescriptor](../mtl4meshrenderpipelinedescriptor.md)

# maxTotalThreadsPerMeshThreadgroup

<sub>Instance Property</sub>

Controls the largest number of threads the pipeline state can execute in a single mesh shader threadgroup dispatch.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var maxTotalThreadsPerMeshThreadgroup: Int { get set }
```

## Discussion

This number represents the maximum size of the product of the components of parameter `threadsPerMeshThreadgroup` that Metal can use when drawing with this pipeline in mesh shader dispatch methods, such as [- drawMeshThreadgroups:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:](<../mtl4rendercommandencoder/drawmeshthreadgroups(threadgroupspergrid_threadsperobjectthreadgroup_threadspermeshthreadgroup_).md>).

The compiler’s optimizer can use the value of this property to generate more efficient code, specifically when the value doesn’t exceed the thread execution width of the underlying GPU.

The default value of this property is `0`, thish indicates that the Metal Shader Language attribute `[[max_total_threads_per_threadgroup]]` you attache to the pipeline’s mesh shader function determines the value of this property.

When you specify both the `[[max_total_threads_per_threadgroup(N)]]` attribute and this property, you are responsible for making sure these values match.

Additionally, you are responsible for ensuring this value doesn’t exceed the “maximum threads per threadgroup” device limit documented in the “Metal Feature Set Tables” PDF: [https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf).
