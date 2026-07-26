---
title: MTLAccelerationStructureMotionCurveGeometryDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructuremotioncurvegeometrydescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructuremotioncurvegeometrydescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructuremotioncurvegeometrydescriptor.json'
content_hash: 'sha256:e2437b8da39cb737'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLAccelerationStructureMotionCurveGeometryDescriptor

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLAccelerationStructureMotionCurveGeometryDescriptor
```

## Relationships

- **Inherits From**: [MTLAccelerationStructureGeometryDescriptor](mtlaccelerationstructuregeometrydescriptor.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Instance Properties

- [controlPointBuffers](mtlaccelerationstructuremotioncurvegeometrydescriptor/controlpointbuffers.md)
- [controlPointCount](mtlaccelerationstructuremotioncurvegeometrydescriptor/controlpointcount.md)
- [controlPointFormat](mtlaccelerationstructuremotioncurvegeometrydescriptor/controlpointformat.md)
- [controlPointStride](mtlaccelerationstructuremotioncurvegeometrydescriptor/controlpointstride.md)
- [curveBasis](mtlaccelerationstructuremotioncurvegeometrydescriptor/curvebasis.md)
- [curveEndCaps](mtlaccelerationstructuremotioncurvegeometrydescriptor/curveendcaps.md)
- [curveType](mtlaccelerationstructuremotioncurvegeometrydescriptor/curvetype.md)
- [indexBuffer](mtlaccelerationstructuremotioncurvegeometrydescriptor/indexbuffer.md)
- [indexBufferOffset](mtlaccelerationstructuremotioncurvegeometrydescriptor/indexbufferoffset.md)
- [indexType](mtlaccelerationstructuremotioncurvegeometrydescriptor/indextype.md)
- [radiusBuffers](mtlaccelerationstructuremotioncurvegeometrydescriptor/radiusbuffers.md)
- [radiusFormat](mtlaccelerationstructuremotioncurvegeometrydescriptor/radiusformat.md)
- [radiusStride](mtlaccelerationstructuremotioncurvegeometrydescriptor/radiusstride.md)
- [segmentControlPointCount](mtlaccelerationstructuremotioncurvegeometrydescriptor/segmentcontrolpointcount.md)
- [segmentCount](mtlaccelerationstructuremotioncurvegeometrydescriptor/segmentcount.md)

## See Also

### Motion geometry descriptors

- [MTL4AccelerationStructureMotionTriangleGeometryDescriptor](mtl4accelerationstructuremotiontrianglegeometrydescriptor.md) — Describes motion triangle geometry, suitable for motion ray tracing.
- [MTLAccelerationStructureMotionTriangleGeometryDescriptor](mtlaccelerationstructuremotiontrianglegeometrydescriptor.md) — A description of a list of triangle primitives, as motion keyframe data, to turn into an acceleration structure.
- [MTL4AccelerationStructureMotionCurveGeometryDescriptor](mtl4accelerationstructuremotioncurvegeometrydescriptor.md) — Describes motion curve geometry, suitable for motion ray tracing.
- [MTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor](mtl4accelerationstructuremotionboundingboxgeometrydescriptor.md) — Describes motion bounding box geometry, suitable for motion ray tracing.
- [MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor](mtlaccelerationstructuremotionboundingboxgeometrydescriptor.md) — A description of a list of bounding boxes, as motion keyframe data, to turn into an acceleration structure.
- [MTLMotionKeyframeData](mtlmotionkeyframedata.md) — Geometry data for a specific keyframe to use in a moving instance.
