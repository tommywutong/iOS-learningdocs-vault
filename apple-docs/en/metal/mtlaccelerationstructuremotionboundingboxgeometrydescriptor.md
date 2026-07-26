---
title: MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructuremotionboundingboxgeometrydescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructuremotionboundingboxgeometrydescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructuremotionboundingboxgeometrydescriptor.json'
content_hash: 'sha256:17ff269eb55a13f3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor

<sub>Class</sub>

A description of a list of bounding boxes, as motion keyframe data, to turn into an acceleration structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor
```

## Relationships

- **Inherits From**: [MTLAccelerationStructureGeometryDescriptor](mtlaccelerationstructuregeometrydescriptor.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Specifying the number of bounding boxes

- [boundingBoxCount](mtlaccelerationstructuremotionboundingboxgeometrydescriptor/boundingboxcount.md) — The number of bounding boxes in each bounding box buffer.

### Specifying bounding boxes data

- [boundingBoxBuffers](mtlaccelerationstructuremotionboundingboxgeometrydescriptor/boundingboxbuffers.md) — A array of motion keyframes, each containing bounding box data.
- [boundingBoxStride](mtlaccelerationstructuremotionboundingboxgeometrydescriptor/boundingboxstride.md) — The stride, in bytes, between bounding boxes in each buffer.

## See Also

### Motion geometry descriptors

- [MTL4AccelerationStructureMotionTriangleGeometryDescriptor](mtl4accelerationstructuremotiontrianglegeometrydescriptor.md) — Describes motion triangle geometry, suitable for motion ray tracing.
- [MTLAccelerationStructureMotionTriangleGeometryDescriptor](mtlaccelerationstructuremotiontrianglegeometrydescriptor.md) — A description of a list of triangle primitives, as motion keyframe data, to turn into an acceleration structure.
- [MTL4AccelerationStructureMotionCurveGeometryDescriptor](mtl4accelerationstructuremotioncurvegeometrydescriptor.md) — Describes motion curve geometry, suitable for motion ray tracing.
- [MTLAccelerationStructureMotionCurveGeometryDescriptor](mtlaccelerationstructuremotioncurvegeometrydescriptor.md)
- [MTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor](mtl4accelerationstructuremotionboundingboxgeometrydescriptor.md) — Describes motion bounding box geometry, suitable for motion ray tracing.
- [MTLMotionKeyframeData](mtlmotionkeyframedata.md) — Geometry data for a specific keyframe to use in a moving instance.
