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
doc_path: /documentation/metal/mtl4accelerationstructuremotiontrianglegeometrydescriptor/indexbuffer
source_url: 'https://developer.apple.com/documentation/metal/mtl4accelerationstructuremotiontrianglegeometrydescriptor/indexbuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4accelerationstructuremotiontrianglegeometrydescriptor/indexbuffer.json'
content_hash: 'sha256:28815f99f26996f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4AccelerationStructureMotionTriangleGeometryDescriptor](../mtl4accelerationstructuremotiontrianglegeometrydescriptor.md)

# indexBuffer

<sub>Instance Property</sub>

Assigns an optional index buffer containing references to vertices in the vertex buffers you reference through the vertex buffers property.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var indexBuffer: MTL4BufferRange { get set }
```

## Discussion

You can set this property to `0`, the default, to avoid specifying an index buffer. All keyframes share the same index buffer.
