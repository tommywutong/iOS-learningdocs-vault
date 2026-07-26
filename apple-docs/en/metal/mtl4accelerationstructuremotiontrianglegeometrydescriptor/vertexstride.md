---
title: vertexStride
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4accelerationstructuremotiontrianglegeometrydescriptor/vertexstride
source_url: 'https://developer.apple.com/documentation/metal/mtl4accelerationstructuremotiontrianglegeometrydescriptor/vertexstride'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4accelerationstructuremotiontrianglegeometrydescriptor/vertexstride.json'
content_hash: 'sha256:418df8e0545981fa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4AccelerationStructureMotionTriangleGeometryDescriptor](../mtl4accelerationstructuremotiontrianglegeometrydescriptor.md)

# vertexStride

<sub>Instance Property</sub>

Sets the stride, in bytes, between vertices in all the vertex buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var vertexStride: Int { get set }
```

## Discussion

All keyframes share the same vertex stride. This stride needs to be a multiple of the size of the vertex format you provide in the [vertexFormat](vertexformat.md) property.

Similarly, you are responsible for ensuring this stride matches the vertex format data type’s alignment.

Defaults to `0`, which signals the stride matches the size of the [vertexFormat](vertexformat.md) data.
