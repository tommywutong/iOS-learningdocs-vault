---
title: payloadMemoryLength
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4meshrenderpipelinedescriptor/payloadmemorylength
source_url: 'https://developer.apple.com/documentation/metal/mtl4meshrenderpipelinedescriptor/payloadmemorylength'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4meshrenderpipelinedescriptor/payloadmemorylength.json'
content_hash: 'sha256:0c285f663415b686'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4MeshRenderPipelineDescriptor](../mtl4meshrenderpipelinedescriptor.md)

# payloadMemoryLength

<sub>Instance Property</sub>

Reserves storage for the object-to-mesh stage payload.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var payloadMemoryLength: Int { get set }
```

## Discussion

This property determines the size, in bytes, of the buffer you indicate via the Metal Shading Language `[[payload]]` attribute in the object and mesh shader functions of the mesh render pipeline.

If this value is `0`, Metal derives the size from the (dereferenced) type you declare for the payload in the object shader function. If the type is a pointer, Metal reserves space for a single element.

The default value is `0`.
