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
doc_path: /documentation/metal/mtl4accelerationstructuretrianglegeometrydescriptor/vertexformat
source_url: 'https://developer.apple.com/documentation/metal/mtl4accelerationstructuretrianglegeometrydescriptor/vertexformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4accelerationstructuretrianglegeometrydescriptor/vertexformat.json'
content_hash: 'sha256:6d8dcc4a0f21ccac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4AccelerationStructureTriangleGeometryDescriptor](../mtl4accelerationstructuretrianglegeometrydescriptor.md)

# vertexFormat

<sub>Instance Property</sub>

Describes the format of the vertices in the vertex buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var vertexFormat: MTLAttributeFormat { get set }
```

## Discussion

This property controls the format of the position attribute of the vertices the [vertexBuffer](vertexbuffer.md) references.

The format defaults to `MTLAttributeFormatFloat3`, corresponding to three packed floating point numbers.
