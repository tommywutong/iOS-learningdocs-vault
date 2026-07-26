---
title: transformationMatrixBuffer
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4accelerationstructuretrianglegeometrydescriptor/transformationmatrixbuffer
source_url: 'https://developer.apple.com/documentation/metal/mtl4accelerationstructuretrianglegeometrydescriptor/transformationmatrixbuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4accelerationstructuretrianglegeometrydescriptor/transformationmatrixbuffer.json'
content_hash: 'sha256:17fbd2f980904e0b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4AccelerationStructureTriangleGeometryDescriptor](../mtl4accelerationstructuretrianglegeometrydescriptor.md)

# transformationMatrixBuffer

<sub>Instance Property</sub>

Assigns an optional reference to a buffer containing a `float4x3` transformation matrix.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var transformationMatrixBuffer: MTL4BufferRange { get set }
```

## Discussion

When the buffer address is non-zero, Metal applies this transform to the vertex data positions when building the acceleration structure.

Building an acceleration structure with a descriptor that specifies this property doesn’t modify the contents of the input `vertexBuffer`.
