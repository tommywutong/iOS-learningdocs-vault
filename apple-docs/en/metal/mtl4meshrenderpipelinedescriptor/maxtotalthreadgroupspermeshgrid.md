---
title: maxTotalThreadgroupsPerMeshGrid
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4meshrenderpipelinedescriptor/maxtotalthreadgroupspermeshgrid
source_url: 'https://developer.apple.com/documentation/metal/mtl4meshrenderpipelinedescriptor/maxtotalthreadgroupspermeshgrid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4meshrenderpipelinedescriptor/maxtotalthreadgroupspermeshgrid.json'
content_hash: 'sha256:4d08be6c103a749a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4MeshRenderPipelineDescriptor](../mtl4meshrenderpipelinedescriptor.md)

# maxTotalThreadgroupsPerMeshGrid

<sub>Instance Property</sub>

Controls the largest number of threads the pipeline state can execute when the object stage of a mesh render pipeline you create from this descriptor dispatches its mesh stage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var maxTotalThreadgroupsPerMeshGrid: Int { get set }
```

## Discussion

This number represents the maximum size of the product of the components of the parameter you pass to Metal Shading Language’s built-in function `mesh_grid_properties::set_threadgroups_per_grid`.

The default value of this property is `0`, which indicates that the Metal Shading Language attribute `[[max_total_threadgroups_per_mesh_grid(N)]]` you attach to the pipeline’s mesh shader function determines the value of this property.

When you specify both the `[[max_total_threadgroups_per_mesh_grid(N)]]` attribute and this property, you are responsible for making sure these values match.

Additionally, you are responsible for ensuring this value doesn’t exceed the “maximum threads per mesh grid” device limit documented in the “Metal Feature Set Tables” PDF: [https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf).
