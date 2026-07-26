---
title: MTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4accelerationstructuremotionboundingboxgeometrydescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtl4accelerationstructuremotionboundingboxgeometrydescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4accelerationstructuremotionboundingboxgeometrydescriptor.json'
content_hash: 'sha256:9b8e58aa9e1bfd28'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor

<sub>Class</sub>

Describes motion bounding box geometry, suitable for motion ray tracing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor
```

## Overview

You use bounding boxes to implement procedural geometry for ray tracing, such as spheres or any other shape you define by using intersection functions.

Use a [MTLResidencySet](mtlresidencyset.md) to mark residency of all buffers this descriptor references when you build this acceleration structure.

## Relationships

- **Inherits From**: [MTL4AccelerationStructureGeometryDescriptor](mtl4accelerationstructuregeometrydescriptor.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Instance Properties

- [boundingBoxBuffers](mtl4accelerationstructuremotionboundingboxgeometrydescriptor/boundingboxbuffers.md) — Configures a reference to a buffer where each entry contains a reference to a buffer of bounding boxes.
- [boundingBoxCount](mtl4accelerationstructuremotionboundingboxgeometrydescriptor/boundingboxcount.md) — Declares the number of bounding boxes in each buffer that `boundingBoxBuffer` references.
- [boundingBoxStride](mtl4accelerationstructuremotionboundingboxgeometrydescriptor/boundingboxstride.md) — Declares the stride, in bytes, between bounding boxes in the bounding box buffers each entry in `boundingBoxBuffer` references.

## See Also

### Motion geometry descriptors

- [MTL4AccelerationStructureMotionTriangleGeometryDescriptor](mtl4accelerationstructuremotiontrianglegeometrydescriptor.md) — Describes motion triangle geometry, suitable for motion ray tracing.
- [MTLAccelerationStructureMotionTriangleGeometryDescriptor](mtlaccelerationstructuremotiontrianglegeometrydescriptor.md) — A description of a list of triangle primitives, as motion keyframe data, to turn into an acceleration structure.
- [MTL4AccelerationStructureMotionCurveGeometryDescriptor](mtl4accelerationstructuremotioncurvegeometrydescriptor.md) — Describes motion curve geometry, suitable for motion ray tracing.
- [MTLAccelerationStructureMotionCurveGeometryDescriptor](mtlaccelerationstructuremotioncurvegeometrydescriptor.md)
- [MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor](mtlaccelerationstructuremotionboundingboxgeometrydescriptor.md) — A description of a list of bounding boxes, as motion keyframe data, to turn into an acceleration structure.
- [MTLMotionKeyframeData](mtlmotionkeyframedata.md) — Geometry data for a specific keyframe to use in a moving instance.
