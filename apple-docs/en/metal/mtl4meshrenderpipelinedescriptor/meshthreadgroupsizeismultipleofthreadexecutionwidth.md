---
title: meshThreadgroupSizeIsMultipleOfThreadExecutionWidth
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4meshrenderpipelinedescriptor/meshthreadgroupsizeismultipleofthreadexecutionwidth
source_url: 'https://developer.apple.com/documentation/metal/mtl4meshrenderpipelinedescriptor/meshthreadgroupsizeismultipleofthreadexecutionwidth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4meshrenderpipelinedescriptor/meshthreadgroupsizeismultipleofthreadexecutionwidth.json'
content_hash: 'sha256:da9fd7eb973e4b37'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4MeshRenderPipelineDescriptor](../mtl4meshrenderpipelinedescriptor.md)

# meshThreadgroupSizeIsMultipleOfThreadExecutionWidth

<sub>Instance Property</sub>

Provides a guarantee to Metal regarding the number of threadgroup threads for the mesh stage of a pipeline you create from this descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var meshThreadgroupSizeIsMultipleOfThreadExecutionWidth: Bool { get set }
```

## Discussion

If you set this property to [true](../../swift/true.md), you state to Metal that when you use a mesh render pipeline you create from this descriptor, the number of threadgroup threads you dispatch for the mesh stage is a multiple of its [meshThreadExecutionWidth](../mtlrenderpipelinestate/meshthreadexecutionwidth.md). The compiler’s optimizer can use this guarantee to generate more efficient code.

This property’s default value is [false](../../swift/false.md).
