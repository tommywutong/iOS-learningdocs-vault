---
title: MTLAccelerationStructureBoundingBoxGeometryDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructureboundingboxgeometrydescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructureboundingboxgeometrydescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructureboundingboxgeometrydescriptor.json'
content_hash: 'sha256:7a2b3a596eb71db7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLAccelerationStructureBoundingBoxGeometryDescriptor

<sub>Class</sub>

A description of a list of bounding boxes to turn into an acceleration structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLAccelerationStructureBoundingBoxGeometryDescriptor
```

## Relationships

- **Inherits From**: [MTLAccelerationStructureGeometryDescriptor](mtlaccelerationstructuregeometrydescriptor.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Specifying the number of bounding boxes

- [boundingBoxCount](mtlaccelerationstructureboundingboxgeometrydescriptor/boundingboxcount.md) — The number of bounding boxes in the bounding box buffer.

### Specifying bounding boxes data

- [boundingBoxBuffer](mtlaccelerationstructureboundingboxgeometrydescriptor/boundingboxbuffer.md) — A buffer that contains an array of bounding box structures.
- [boundingBoxBufferOffset](mtlaccelerationstructureboundingboxgeometrydescriptor/boundingboxbufferoffset.md) — The offset, in bytes, to the first bounding box in the buffer.
- [boundingBoxStride](mtlaccelerationstructureboundingboxgeometrydescriptor/boundingboxstride.md) — The stride, in bytes, between bounding boxes in the buffer.

## See Also

### Geometry descriptors

- [MTL4AccelerationStructureGeometryDescriptor](mtl4accelerationstructuregeometrydescriptor.md) — Base class for all Metal 4 acceleration structure geometry descriptors.
- [MTLAccelerationStructureGeometryDescriptor](mtlaccelerationstructuregeometrydescriptor.md) — A base class for descriptors that contain geometry data to convert into a ray-tracing acceleration structure.
- [MTL4AccelerationStructureTriangleGeometryDescriptor](mtl4accelerationstructuretrianglegeometrydescriptor.md) — Describes triangle geometry suitable for ray tracing.
- [MTLAccelerationStructureTriangleGeometryDescriptor](mtlaccelerationstructuretrianglegeometrydescriptor.md) — A description of a list of triangle primitives to turn into an acceleration structure.
- [MTL4AccelerationStructureCurveGeometryDescriptor](mtl4accelerationstructurecurvegeometrydescriptor.md) — Describes curve geometry suitable for ray tracing.
- [MTLAccelerationStructureCurveGeometryDescriptor](mtlaccelerationstructurecurvegeometrydescriptor.md) — A descriptor you configure with curve geometry for building acceleration structures.
- [MTLCurveType](mtlcurvetype.md)
- [MTLCurveBasis](mtlcurvebasis.md)
- [MTLCurveEndCaps](mtlcurveendcaps.md)
- [MTL4AccelerationStructureBoundingBoxGeometryDescriptor](mtl4accelerationstructureboundingboxgeometrydescriptor.md) — Describes bounding-box geometry suitable for ray tracing.
