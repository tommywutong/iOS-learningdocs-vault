---
title: MTLAccelerationStructureGeometryDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructuregeometrydescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructuregeometrydescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructuregeometrydescriptor.json'
content_hash: 'sha256:2c097418f7ee256f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLAccelerationStructureGeometryDescriptor

<sub>Class</sub>

A base class for descriptors that contain geometry data to convert into a ray-tracing acceleration structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLAccelerationStructureGeometryDescriptor
```

## Overview

Don’t use this base class directly. Use one of the derived classes instead, as  [MTLAccelerationStructure](mtlaccelerationstructure.md) describes.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [MTLAccelerationStructureBoundingBoxGeometryDescriptor](mtlaccelerationstructureboundingboxgeometrydescriptor.md), [MTLAccelerationStructureCurveGeometryDescriptor](mtlaccelerationstructurecurvegeometrydescriptor.md), [MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor](mtlaccelerationstructuremotionboundingboxgeometrydescriptor.md), [MTLAccelerationStructureMotionCurveGeometryDescriptor](mtlaccelerationstructuremotioncurvegeometrydescriptor.md), [MTLAccelerationStructureMotionTriangleGeometryDescriptor](mtlaccelerationstructuremotiontrianglegeometrydescriptor.md), [MTLAccelerationStructureTriangleGeometryDescriptor](mtlaccelerationstructuretrianglegeometrydescriptor.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Specifying base geometry properties

- [label](mtlaccelerationstructuregeometrydescriptor/label.md) — A label for the geometry structure, suitable for debugging.
- [intersectionFunctionTableOffset](mtlaccelerationstructuregeometrydescriptor/intersectionfunctiontableoffset.md) — An index into the intersection table for determining which intersection function Metal calls when it intersects a ray with the acceleration structure.
- [opaque](mtlaccelerationstructuregeometrydescriptor/opaque.md) — A Boolean value that determines whether the geometry data in the acceleration structure needs to skip triangle-intersection tests.
- [allowDuplicateIntersectionFunctionInvocation](mtlaccelerationstructuregeometrydescriptor/allowduplicateintersectionfunctioninvocation.md) — A Boolean value that indicates whether Metal calls the ray-intersection test more than once per primitive on the structure.

### Instance Properties

- [primitiveDataBuffer](mtlaccelerationstructuregeometrydescriptor/primitivedatabuffer.md)
- [primitiveDataBufferOffset](mtlaccelerationstructuregeometrydescriptor/primitivedatabufferoffset.md)
- [primitiveDataElementSize](mtlaccelerationstructuregeometrydescriptor/primitivedataelementsize.md)
- [primitiveDataStride](mtlaccelerationstructuregeometrydescriptor/primitivedatastride.md)

## See Also

### Related Documentation

- [MTLAccelerationStructureMotionTriangleGeometryDescriptor](mtlaccelerationstructuremotiontrianglegeometrydescriptor.md) — A description of a list of triangle primitives, as motion keyframe data, to turn into an acceleration structure.
- [MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor](mtlaccelerationstructuremotionboundingboxgeometrydescriptor.md) — A description of a list of bounding boxes, as motion keyframe data, to turn into an acceleration structure.

### Geometry descriptors

- [MTL4AccelerationStructureGeometryDescriptor](mtl4accelerationstructuregeometrydescriptor.md) — Base class for all Metal 4 acceleration structure geometry descriptors.
- [MTL4AccelerationStructureTriangleGeometryDescriptor](mtl4accelerationstructuretrianglegeometrydescriptor.md) — Describes triangle geometry suitable for ray tracing.
- [MTLAccelerationStructureTriangleGeometryDescriptor](mtlaccelerationstructuretrianglegeometrydescriptor.md) — A description of a list of triangle primitives to turn into an acceleration structure.
- [MTL4AccelerationStructureCurveGeometryDescriptor](mtl4accelerationstructurecurvegeometrydescriptor.md) — Describes curve geometry suitable for ray tracing.
- [MTLAccelerationStructureCurveGeometryDescriptor](mtlaccelerationstructurecurvegeometrydescriptor.md) — A descriptor you configure with curve geometry for building acceleration structures.
- [MTLCurveType](mtlcurvetype.md)
- [MTLCurveBasis](mtlcurvebasis.md)
- [MTLCurveEndCaps](mtlcurveendcaps.md)
- [MTL4AccelerationStructureBoundingBoxGeometryDescriptor](mtl4accelerationstructureboundingboxgeometrydescriptor.md) — Describes bounding-box geometry suitable for ray tracing.
- [MTLAccelerationStructureBoundingBoxGeometryDescriptor](mtlaccelerationstructureboundingboxgeometrydescriptor.md) — A description of a list of bounding boxes to turn into an acceleration structure.
