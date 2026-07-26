---
title: MTL4AccelerationStructureGeometryDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4accelerationstructuregeometrydescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtl4accelerationstructuregeometrydescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4accelerationstructuregeometrydescriptor.json'
content_hash: 'sha256:580fc82d30a38e42'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTL4AccelerationStructureGeometryDescriptor

<sub>Class</sub>

Base class for all Metal 4 acceleration structure geometry descriptors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTL4AccelerationStructureGeometryDescriptor
```

## Overview

Don’t use this class directly. Use one of the derived classes instead.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [MTL4AccelerationStructureBoundingBoxGeometryDescriptor](mtl4accelerationstructureboundingboxgeometrydescriptor.md), [MTL4AccelerationStructureCurveGeometryDescriptor](mtl4accelerationstructurecurvegeometrydescriptor.md), [MTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor](mtl4accelerationstructuremotionboundingboxgeometrydescriptor.md), [MTL4AccelerationStructureMotionCurveGeometryDescriptor](mtl4accelerationstructuremotioncurvegeometrydescriptor.md), [MTL4AccelerationStructureMotionTriangleGeometryDescriptor](mtl4accelerationstructuremotiontrianglegeometrydescriptor.md), [MTL4AccelerationStructureTriangleGeometryDescriptor](mtl4accelerationstructuretrianglegeometrydescriptor.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Instance Properties

- [allowDuplicateIntersectionFunctionInvocation](mtl4accelerationstructuregeometrydescriptor/allowduplicateintersectionfunctioninvocation.md) — A boolean value that indicates whether the ray-tracing system in Metal allows the invocation of intersection functions more than once per ray-primitive intersection.
- [intersectionFunctionTableOffset](mtl4accelerationstructuregeometrydescriptor/intersectionfunctiontableoffset.md) — Sets the offset that this geometry contributes to determining the intersection function to invoke when a ray intersects it.
- [label](mtl4accelerationstructuregeometrydescriptor/label.md) — Assigns an optional label you can assign to this geometry for debugging purposes.
- [opaque](mtl4accelerationstructuregeometrydescriptor/opaque.md) — Provides a hint to Metal that this geometry is opaque, potentially accelerating the ray/primitive intersection process.
- [primitiveDataBuffer](mtl4accelerationstructuregeometrydescriptor/primitivedatabuffer.md) — Assigns optional buffer containing data to associate with each primitive in this geometry.
- [primitiveDataElementSize](mtl4accelerationstructuregeometrydescriptor/primitivedataelementsize.md) — Sets the size, in bytes, of the data for each primitive in the primitive data buffer [primitiveDataBuffer](mtl4accelerationstructuregeometrydescriptor/primitivedatabuffer.md) references.
- [primitiveDataStride](mtl4accelerationstructuregeometrydescriptor/primitivedatastride.md) — Defines the stride, in bytes, between each primitive’s data in the primitive data buffer [primitiveDataBuffer](mtl4accelerationstructuregeometrydescriptor/primitivedatabuffer.md) references.

## See Also

### Geometry descriptors

- [MTLAccelerationStructureGeometryDescriptor](mtlaccelerationstructuregeometrydescriptor.md) — A base class for descriptors that contain geometry data to convert into a ray-tracing acceleration structure.
- [MTL4AccelerationStructureTriangleGeometryDescriptor](mtl4accelerationstructuretrianglegeometrydescriptor.md) — Describes triangle geometry suitable for ray tracing.
- [MTLAccelerationStructureTriangleGeometryDescriptor](mtlaccelerationstructuretrianglegeometrydescriptor.md) — A description of a list of triangle primitives to turn into an acceleration structure.
- [MTL4AccelerationStructureCurveGeometryDescriptor](mtl4accelerationstructurecurvegeometrydescriptor.md) — Describes curve geometry suitable for ray tracing.
- [MTLAccelerationStructureCurveGeometryDescriptor](mtlaccelerationstructurecurvegeometrydescriptor.md) — A descriptor you configure with curve geometry for building acceleration structures.
- [MTLCurveType](mtlcurvetype.md)
- [MTLCurveBasis](mtlcurvebasis.md)
- [MTLCurveEndCaps](mtlcurveendcaps.md)
- [MTL4AccelerationStructureBoundingBoxGeometryDescriptor](mtl4accelerationstructureboundingboxgeometrydescriptor.md) — Describes bounding-box geometry suitable for ray tracing.
- [MTLAccelerationStructureBoundingBoxGeometryDescriptor](mtlaccelerationstructureboundingboxgeometrydescriptor.md) — A description of a list of bounding boxes to turn into an acceleration structure.
