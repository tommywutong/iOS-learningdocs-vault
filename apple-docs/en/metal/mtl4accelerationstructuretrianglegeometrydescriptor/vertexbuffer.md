---
title: vertexBuffer
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4accelerationstructuretrianglegeometrydescriptor/vertexbuffer
source_url: 'https://developer.apple.com/documentation/metal/mtl4accelerationstructuretrianglegeometrydescriptor/vertexbuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4accelerationstructuretrianglegeometrydescriptor/vertexbuffer.json'
content_hash: 'sha256:ddf44618f51f2e8d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4AccelerationStructureTriangleGeometryDescriptor](../mtl4accelerationstructuretrianglegeometrydescriptor.md)

# vertexBuffer

<sub>Instance Property</sub>

Associates a vertex buffer containing triangle vertices.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var vertexBuffer: MTL4BufferRange { get set }
```

## Discussion

You are responsible for ensuring that the format of all vertex positions match the [vertexFormat](vertexformat.md) property, and that the buffer address for the buffer range is not zero.
