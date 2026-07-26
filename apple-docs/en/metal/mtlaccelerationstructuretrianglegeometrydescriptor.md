---
title: MTLAccelerationStructureTriangleGeometryDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructuretrianglegeometrydescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructuretrianglegeometrydescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructuretrianglegeometrydescriptor.json'
content_hash: 'sha256:30168afa3fdbb616'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLAccelerationStructureTriangleGeometryDescriptor

<sub>Class</sub>

A description of a list of triangle primitives to turn into an acceleration structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLAccelerationStructureTriangleGeometryDescriptor
```

## Relationships

- **Inherits From**: [MTLAccelerationStructureGeometryDescriptor](mtlaccelerationstructuregeometrydescriptor.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Configuring the number of triangles

- [triangleCount](mtlaccelerationstructuretrianglegeometrydescriptor/trianglecount.md) — The number of triangles in the buffers.

### Configuring index data

- [indexType](mtlaccelerationstructuretrianglegeometrydescriptor/indextype.md) — The data type of indices in the index buffer.
- [indexBuffer](mtlaccelerationstructuretrianglegeometrydescriptor/indexbuffer.md) — A buffer that contains indices for the vertices that compose the triangle list.
- [indexBufferOffset](mtlaccelerationstructuretrianglegeometrydescriptor/indexbufferoffset.md) — The offset, in bytes, to the first index in the buffer.

### Configuring vertex data

- [vertexFormat](mtlaccelerationstructuretrianglegeometrydescriptor/vertexformat.md) — The format of each vertex position in the vertex buffer property.
- [vertexBuffer](mtlaccelerationstructuretrianglegeometrydescriptor/vertexbuffer.md) — A buffer that contains vertex data.
- [vertexBufferOffset](mtlaccelerationstructuretrianglegeometrydescriptor/vertexbufferoffset.md) — The offset, in bytes, for the first vertex in the vertex buffer.
- [vertexStride](mtlaccelerationstructuretrianglegeometrydescriptor/vertexstride.md) — The stride, in bytes, between vertices in the vertex buffer.

### Configuring transformation data

- [transformationMatrixLayout](mtlaccelerationstructuretrianglegeometrydescriptor/transformationmatrixlayout.md)
- [transformationMatrixBuffer](mtlaccelerationstructuretrianglegeometrydescriptor/transformationmatrixbuffer.md)
- [transformationMatrixBufferOffset](mtlaccelerationstructuretrianglegeometrydescriptor/transformationmatrixbufferoffset.md)

## See Also

### Geometry descriptors

- [MTL4AccelerationStructureGeometryDescriptor](mtl4accelerationstructuregeometrydescriptor.md) — Base class for all Metal 4 acceleration structure geometry descriptors.
- [MTLAccelerationStructureGeometryDescriptor](mtlaccelerationstructuregeometrydescriptor.md) — A base class for descriptors that contain geometry data to convert into a ray-tracing acceleration structure.
- [MTL4AccelerationStructureTriangleGeometryDescriptor](mtl4accelerationstructuretrianglegeometrydescriptor.md) — Describes triangle geometry suitable for ray tracing.
- [MTL4AccelerationStructureCurveGeometryDescriptor](mtl4accelerationstructurecurvegeometrydescriptor.md) — Describes curve geometry suitable for ray tracing.
- [MTLAccelerationStructureCurveGeometryDescriptor](mtlaccelerationstructurecurvegeometrydescriptor.md) — A descriptor you configure with curve geometry for building acceleration structures.
- [MTLCurveType](mtlcurvetype.md)
- [MTLCurveBasis](mtlcurvebasis.md)
- [MTLCurveEndCaps](mtlcurveendcaps.md)
- [MTL4AccelerationStructureBoundingBoxGeometryDescriptor](mtl4accelerationstructureboundingboxgeometrydescriptor.md) — Describes bounding-box geometry suitable for ray tracing.
- [MTLAccelerationStructureBoundingBoxGeometryDescriptor](mtlaccelerationstructureboundingboxgeometrydescriptor.md) — A description of a list of bounding boxes to turn into an acceleration structure.
