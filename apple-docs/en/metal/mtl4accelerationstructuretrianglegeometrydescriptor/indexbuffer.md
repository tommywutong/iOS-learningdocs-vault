---
title: indexBuffer
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4accelerationstructuretrianglegeometrydescriptor/indexbuffer
source_url: 'https://developer.apple.com/documentation/metal/mtl4accelerationstructuretrianglegeometrydescriptor/indexbuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4accelerationstructuretrianglegeometrydescriptor/indexbuffer.json'
content_hash: 'sha256:abab34411dfeed28'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4AccelerationStructureTriangleGeometryDescriptor](../mtl4accelerationstructuretrianglegeometrydescriptor.md)

# indexBuffer

<sub>Instance Property</sub>

Sets an optional index buffer containing references to vertices in the `vertexBuffer`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var indexBuffer: MTL4BufferRange { get set }
```

## Discussion

You can set this property to `0`, the default, to avoid specifying an index buffer.
