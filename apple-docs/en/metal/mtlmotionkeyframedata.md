---
title: MTLMotionKeyframeData
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlmotionkeyframedata
source_url: 'https://developer.apple.com/documentation/metal/mtlmotionkeyframedata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlmotionkeyframedata.json'
content_hash: 'sha256:712d2b1e9ad3d994'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLMotionKeyframeData

<sub>Class</sub>

Geometry data for a specific keyframe to use in a moving instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLMotionKeyframeData
```

## Overview

An [MTLMotionKeyframeData](mtlmotionkeyframedata.md) instance describes the location of geometry data for a keyframe. The exact type of data can vary, depending on which kind of motion descriptor you create. For an [MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor](mtlaccelerationstructuremotionboundingboxgeometrydescriptor.md) instance, the buffer data is a list of bounding boxes. For an [MTLAccelerationStructureMotionTriangleGeometryDescriptor](mtlaccelerationstructuremotiontrianglegeometrydescriptor.md), the buffer data is a list of vertices.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Specifying the keyframe data

- [buffer](mtlmotionkeyframedata/buffer.md) — The buffer that holds the geometry data.
- [offset](mtlmotionkeyframedata/offset.md) — The offset, in bytes, to the keyframe data.

## See Also

### Motion geometry descriptors

- [MTL4AccelerationStructureMotionTriangleGeometryDescriptor](mtl4accelerationstructuremotiontrianglegeometrydescriptor.md) — Describes motion triangle geometry, suitable for motion ray tracing.
- [MTLAccelerationStructureMotionTriangleGeometryDescriptor](mtlaccelerationstructuremotiontrianglegeometrydescriptor.md) — A description of a list of triangle primitives, as motion keyframe data, to turn into an acceleration structure.
- [MTL4AccelerationStructureMotionCurveGeometryDescriptor](mtl4accelerationstructuremotioncurvegeometrydescriptor.md) — Describes motion curve geometry, suitable for motion ray tracing.
- [MTLAccelerationStructureMotionCurveGeometryDescriptor](mtlaccelerationstructuremotioncurvegeometrydescriptor.md)
- [MTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor](mtl4accelerationstructuremotionboundingboxgeometrydescriptor.md) — Describes motion bounding box geometry, suitable for motion ray tracing.
- [MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor](mtlaccelerationstructuremotionboundingboxgeometrydescriptor.md) — A description of a list of bounding boxes, as motion keyframe data, to turn into an acceleration structure.
