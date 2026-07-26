---
title: vertexFormat
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4accelerationstructuremotiontrianglegeometrydescriptor/vertexformat
source_url: 'https://developer.apple.com/documentation/metal/mtl4accelerationstructuremotiontrianglegeometrydescriptor/vertexformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4accelerationstructuremotiontrianglegeometrydescriptor/vertexformat.json'
content_hash: 'sha256:9d881356a8ec2275'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4AccelerationStructureMotionTriangleGeometryDescriptor](../mtl4accelerationstructuremotiontrianglegeometrydescriptor.md)

# vertexFormat

<sub>Instance Property</sub>

Defines the format of the vertices in the vertex buffers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var vertexFormat: MTLAttributeFormat { get set }
```

## Discussion

All keyframes share the same vertex format. Defaults to `MTLAttributeFormatFloat3`, corresponding to three packed floating point numbers.
