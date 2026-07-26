---
title: MTLAccelerationStructureCurveGeometryDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructurecurvegeometrydescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructurecurvegeometrydescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructurecurvegeometrydescriptor.json'
content_hash: 'sha256:d74ef40a5aea3e1d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLAccelerationStructureCurveGeometryDescriptor

<sub>Class</sub>

A descriptor you configure with curve geometry for building acceleration structures.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLAccelerationStructureCurveGeometryDescriptor
```

## Relationships

- **Inherits From**: [MTLAccelerationStructureGeometryDescriptor](mtlaccelerationstructuregeometrydescriptor.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Instance Properties

- [controlPointBuffer](mtlaccelerationstructurecurvegeometrydescriptor/controlpointbuffer.md) — A buffer that contains curve control points.
- [controlPointBufferOffset](mtlaccelerationstructurecurvegeometrydescriptor/controlpointbufferoffset.md) — The offset, in bytes, to the control point data in the buffer.
- [controlPointCount](mtlaccelerationstructurecurvegeometrydescriptor/controlpointcount.md) — The number of control points in the control point buffer.
- [controlPointFormat](mtlaccelerationstructurecurvegeometrydescriptor/controlpointformat.md) — The format of the control points in the buffer.
- [controlPointStride](mtlaccelerationstructurecurvegeometrydescriptor/controlpointstride.md) — The stride, in bytes, between control points in the buffer.
- [curveBasis](mtlaccelerationstructurecurvegeometrydescriptor/curvebasis.md) — The basis function for the curve geometry.
- [curveEndCaps](mtlaccelerationstructurecurvegeometrydescriptor/curveendcaps.md) — An end-cap type for the curves in the geometry.
- [curveType](mtlaccelerationstructurecurvegeometrydescriptor/curvetype.md) — A curve type for curves in the geometry.
- [indexBuffer](mtlaccelerationstructurecurvegeometrydescriptor/indexbuffer.md) — A buffer that contains references to control points in the control point buffer.
- [indexBufferOffset](mtlaccelerationstructurecurvegeometrydescriptor/indexbufferoffset.md) — The offset, in bytes, to the index data in the buffer.
- [indexType](mtlaccelerationstructurecurvegeometrydescriptor/indextype.md) — The size of each index in the index buffer.
- [radiusBuffer](mtlaccelerationstructurecurvegeometrydescriptor/radiusbuffer.md) — A buffer that contains the curve radius for each control point.
- [radiusBufferOffset](mtlaccelerationstructurecurvegeometrydescriptor/radiusbufferoffset.md) — The offset, in bytes, to the radius data in the buffer.
- [radiusFormat](mtlaccelerationstructurecurvegeometrydescriptor/radiusformat.md) — The format of each radius in the radius buffer.
- [radiusStride](mtlaccelerationstructurecurvegeometrydescriptor/radiusstride.md) — The stride, in bytes, between the radius elements in the radius buffer.
- [segmentControlPointCount](mtlaccelerationstructurecurvegeometrydescriptor/segmentcontrolpointcount.md) — The number of control points in each curve segment.
- [segmentCount](mtlaccelerationstructurecurvegeometrydescriptor/segmentcount.md) — The number of curve segments in each curve of the geometry.

## See Also

### Geometry descriptors

- [MTL4AccelerationStructureGeometryDescriptor](mtl4accelerationstructuregeometrydescriptor.md) — Base class for all Metal 4 acceleration structure geometry descriptors.
- [MTLAccelerationStructureGeometryDescriptor](mtlaccelerationstructuregeometrydescriptor.md) — A base class for descriptors that contain geometry data to convert into a ray-tracing acceleration structure.
- [MTL4AccelerationStructureTriangleGeometryDescriptor](mtl4accelerationstructuretrianglegeometrydescriptor.md) — Describes triangle geometry suitable for ray tracing.
- [MTLAccelerationStructureTriangleGeometryDescriptor](mtlaccelerationstructuretrianglegeometrydescriptor.md) — A description of a list of triangle primitives to turn into an acceleration structure.
- [MTL4AccelerationStructureCurveGeometryDescriptor](mtl4accelerationstructurecurvegeometrydescriptor.md) — Describes curve geometry suitable for ray tracing.
- [MTLCurveType](mtlcurvetype.md)
- [MTLCurveBasis](mtlcurvebasis.md)
- [MTLCurveEndCaps](mtlcurveendcaps.md)
- [MTL4AccelerationStructureBoundingBoxGeometryDescriptor](mtl4accelerationstructureboundingboxgeometrydescriptor.md) — Describes bounding-box geometry suitable for ray tracing.
- [MTLAccelerationStructureBoundingBoxGeometryDescriptor](mtlaccelerationstructureboundingboxgeometrydescriptor.md) — A description of a list of bounding boxes to turn into an acceleration structure.
