---
title: MTL4AccelerationStructureMotionTriangleGeometryDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4accelerationstructuremotiontrianglegeometrydescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtl4accelerationstructuremotiontrianglegeometrydescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4accelerationstructuremotiontrianglegeometrydescriptor.json'
content_hash: 'sha256:6ad66931fa264e66'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTL4AccelerationStructureMotionTriangleGeometryDescriptor

<sub>Class</sub>

Describes motion triangle geometry, suitable for motion ray tracing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTL4AccelerationStructureMotionTriangleGeometryDescriptor
```

## Overview

Use a [MTLResidencySet](mtlresidencyset.md) to mark residency of all buffers this descriptor references when you build this acceleration structure.

## Relationships

- **Inherits From**: [MTL4AccelerationStructureGeometryDescriptor](mtl4accelerationstructuregeometrydescriptor.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Instance Properties

- [indexBuffer](mtl4accelerationstructuremotiontrianglegeometrydescriptor/indexbuffer.md) — Assigns an optional index buffer containing references to vertices in the vertex buffers you reference through the vertex buffers property.
- [indexType](mtl4accelerationstructuremotiontrianglegeometrydescriptor/indextype.md) — Specifies the size of the indices the `indexBuffer` contains, which is typically either 16 or 32-bits for each index.
- [transformationMatrixBuffer](mtl4accelerationstructuremotiontrianglegeometrydescriptor/transformationmatrixbuffer.md) — Assings an optional reference to a buffer containing a `float4x3` transformation matrix.
- [transformationMatrixLayout](mtl4accelerationstructuremotiontrianglegeometrydescriptor/transformationmatrixlayout.md) — Configures the layout for the transformation matrix in the transformation matrix buffer.
- [triangleCount](mtl4accelerationstructuremotiontrianglegeometrydescriptor/trianglecount.md) — Declares the number of triangles in the vertex buffers that the buffer in the vertex buffers property references.
- [vertexBuffers](mtl4accelerationstructuremotiontrianglegeometrydescriptor/vertexbuffers.md) — Assigns a buffer where each entry contains a reference to a vertex buffer.
- [vertexFormat](mtl4accelerationstructuremotiontrianglegeometrydescriptor/vertexformat.md) — Defines the format of the vertices in the vertex buffers.
- [vertexStride](mtl4accelerationstructuremotiontrianglegeometrydescriptor/vertexstride.md) — Sets the stride, in bytes, between vertices in all the vertex buffer.

## See Also

### Motion geometry descriptors

- [MTLAccelerationStructureMotionTriangleGeometryDescriptor](mtlaccelerationstructuremotiontrianglegeometrydescriptor.md) — A description of a list of triangle primitives, as motion keyframe data, to turn into an acceleration structure.
- [MTL4AccelerationStructureMotionCurveGeometryDescriptor](mtl4accelerationstructuremotioncurvegeometrydescriptor.md) — Describes motion curve geometry, suitable for motion ray tracing.
- [MTLAccelerationStructureMotionCurveGeometryDescriptor](mtlaccelerationstructuremotioncurvegeometrydescriptor.md)
- [MTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor](mtl4accelerationstructuremotionboundingboxgeometrydescriptor.md) — Describes motion bounding box geometry, suitable for motion ray tracing.
- [MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor](mtlaccelerationstructuremotionboundingboxgeometrydescriptor.md) — A description of a list of bounding boxes, as motion keyframe data, to turn into an acceleration structure.
- [MTLMotionKeyframeData](mtlmotionkeyframedata.md) — Geometry data for a specific keyframe to use in a moving instance.
