---
title: MTL4AccelerationStructureTriangleGeometryDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4accelerationstructuretrianglegeometrydescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtl4accelerationstructuretrianglegeometrydescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4accelerationstructuretrianglegeometrydescriptor.json'
content_hash: 'sha256:9981458d64b7ffc8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTL4AccelerationStructureTriangleGeometryDescriptor

<sub>Class</sub>

Describes triangle geometry suitable for ray tracing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTL4AccelerationStructureTriangleGeometryDescriptor
```

## Overview

Use a [MTLResidencySet](mtlresidencyset.md) to mark residency of all buffers this descriptor references when you build this acceleration structure.

## Relationships

- **Inherits From**: [MTL4AccelerationStructureGeometryDescriptor](mtl4accelerationstructuregeometrydescriptor.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Instance Properties

- [indexBuffer](mtl4accelerationstructuretrianglegeometrydescriptor/indexbuffer.md) — Sets an optional index buffer containing references to vertices in the `vertexBuffer`.
- [indexType](mtl4accelerationstructuretrianglegeometrydescriptor/indextype.md) — Configures the size of the indices the `indexBuffer` contains, which is typically either 16 or 32-bits for each index.
- [transformationMatrixBuffer](mtl4accelerationstructuretrianglegeometrydescriptor/transformationmatrixbuffer.md) — Assigns an optional reference to a buffer containing a `float4x3` transformation matrix.
- [transformationMatrixLayout](mtl4accelerationstructuretrianglegeometrydescriptor/transformationmatrixlayout.md) — Configures the layout for the transformation matrix in the transformation matrix buffer.
- [triangleCount](mtl4accelerationstructuretrianglegeometrydescriptor/trianglecount.md) — Declares the number of triangles in this geometry descriptor.
- [vertexBuffer](mtl4accelerationstructuretrianglegeometrydescriptor/vertexbuffer.md) — Associates a vertex buffer containing triangle vertices.
- [vertexFormat](mtl4accelerationstructuretrianglegeometrydescriptor/vertexformat.md) — Describes the format of the vertices in the vertex buffer.
- [vertexStride](mtl4accelerationstructuretrianglegeometrydescriptor/vertexstride.md) — Sets the stride, in bytes, between vertices in the vertex buffer.

## See Also

### Geometry descriptors

- [MTL4AccelerationStructureGeometryDescriptor](mtl4accelerationstructuregeometrydescriptor.md) — Base class for all Metal 4 acceleration structure geometry descriptors.
- [MTLAccelerationStructureGeometryDescriptor](mtlaccelerationstructuregeometrydescriptor.md) — A base class for descriptors that contain geometry data to convert into a ray-tracing acceleration structure.
- [MTLAccelerationStructureTriangleGeometryDescriptor](mtlaccelerationstructuretrianglegeometrydescriptor.md) — A description of a list of triangle primitives to turn into an acceleration structure.
- [MTL4AccelerationStructureCurveGeometryDescriptor](mtl4accelerationstructurecurvegeometrydescriptor.md) — Describes curve geometry suitable for ray tracing.
- [MTLAccelerationStructureCurveGeometryDescriptor](mtlaccelerationstructurecurvegeometrydescriptor.md) — A descriptor you configure with curve geometry for building acceleration structures.
- [MTLCurveType](mtlcurvetype.md)
- [MTLCurveBasis](mtlcurvebasis.md)
- [MTLCurveEndCaps](mtlcurveendcaps.md)
- [MTL4AccelerationStructureBoundingBoxGeometryDescriptor](mtl4accelerationstructureboundingboxgeometrydescriptor.md) — Describes bounding-box geometry suitable for ray tracing.
- [MTLAccelerationStructureBoundingBoxGeometryDescriptor](mtlaccelerationstructureboundingboxgeometrydescriptor.md) — A description of a list of bounding boxes to turn into an acceleration structure.
