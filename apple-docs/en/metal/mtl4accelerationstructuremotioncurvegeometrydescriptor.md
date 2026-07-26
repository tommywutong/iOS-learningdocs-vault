---
title: MTL4AccelerationStructureMotionCurveGeometryDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4accelerationstructuremotioncurvegeometrydescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtl4accelerationstructuremotioncurvegeometrydescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4accelerationstructuremotioncurvegeometrydescriptor.json'
content_hash: 'sha256:ac0d69cd813cbfca'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTL4AccelerationStructureMotionCurveGeometryDescriptor

<sub>Class</sub>

Describes motion curve geometry, suitable for motion ray tracing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTL4AccelerationStructureMotionCurveGeometryDescriptor
```

## Overview

Use a [MTLResidencySet](mtlresidencyset.md) to mark residency of all buffers this descriptor references when you build this acceleration structure.

## Relationships

- **Inherits From**: [MTL4AccelerationStructureGeometryDescriptor](mtl4accelerationstructuregeometrydescriptor.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Instance Properties

- [controlPointBuffers](mtl4accelerationstructuremotioncurvegeometrydescriptor/controlpointbuffers.md) — Assigns a reference to a buffer where each entry contains a reference to a buffer of control points.
- [controlPointCount](mtl4accelerationstructuremotioncurvegeometrydescriptor/controlpointcount.md) — Specifies the number of control points in the buffers the control point buffers reference.
- [controlPointFormat](mtl4accelerationstructuremotioncurvegeometrydescriptor/controlpointformat.md) — Declares the format of the control points in the buffers that the control point buffers reference.
- [controlPointStride](mtl4accelerationstructuremotioncurvegeometrydescriptor/controlpointstride.md) — Sets the stride, in bytes, between control points in the control point buffer.
- [curveBasis](mtl4accelerationstructuremotioncurvegeometrydescriptor/curvebasis.md) — Sets the curve basis function, determining how Metal interpolates the control points.
- [curveEndCaps](mtl4accelerationstructuremotioncurvegeometrydescriptor/curveendcaps.md) — Configures the type of curve end caps.
- [curveType](mtl4accelerationstructuremotioncurvegeometrydescriptor/curvetype.md) — Controls the curve type.
- [indexBuffer](mtl4accelerationstructuremotioncurvegeometrydescriptor/indexbuffer.md) — Assigns an optional index buffer containing references to control points in the control point buffers.
- [indexType](mtl4accelerationstructuremotioncurvegeometrydescriptor/indextype.md) — Configures the size of the indices the `indexBuffer` contains, which is typically either 16 or 32-bits for each index.
- [radiusBuffers](mtl4accelerationstructuremotioncurvegeometrydescriptor/radiusbuffers.md) — Assigns a reference to a buffer containing, in turn, references to curve radii buffers.
- [radiusFormat](mtl4accelerationstructuremotioncurvegeometrydescriptor/radiusformat.md) — Sets the format of the radii in the radius buffer.
- [radiusStride](mtl4accelerationstructuremotioncurvegeometrydescriptor/radiusstride.md) — Sets the stride, in bytes, between radii in the radius buffer.
- [segmentControlPointCount](mtl4accelerationstructuremotioncurvegeometrydescriptor/segmentcontrolpointcount.md) — Controls the number of control points per curve segment.
- [segmentCount](mtl4accelerationstructuremotioncurvegeometrydescriptor/segmentcount.md) — Declares the number of curve segments.

## See Also

### Motion geometry descriptors

- [MTL4AccelerationStructureMotionTriangleGeometryDescriptor](mtl4accelerationstructuremotiontrianglegeometrydescriptor.md) — Describes motion triangle geometry, suitable for motion ray tracing.
- [MTLAccelerationStructureMotionTriangleGeometryDescriptor](mtlaccelerationstructuremotiontrianglegeometrydescriptor.md) — A description of a list of triangle primitives, as motion keyframe data, to turn into an acceleration structure.
- [MTLAccelerationStructureMotionCurveGeometryDescriptor](mtlaccelerationstructuremotioncurvegeometrydescriptor.md)
- [MTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor](mtl4accelerationstructuremotionboundingboxgeometrydescriptor.md) — Describes motion bounding box geometry, suitable for motion ray tracing.
- [MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor](mtlaccelerationstructuremotionboundingboxgeometrydescriptor.md) — A description of a list of bounding boxes, as motion keyframe data, to turn into an acceleration structure.
- [MTLMotionKeyframeData](mtlmotionkeyframedata.md) — Geometry data for a specific keyframe to use in a moving instance.
