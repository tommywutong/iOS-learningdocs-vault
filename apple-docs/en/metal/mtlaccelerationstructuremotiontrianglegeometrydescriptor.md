---
title: MTLAccelerationStructureMotionTriangleGeometryDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructuremotiontrianglegeometrydescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructuremotiontrianglegeometrydescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructuremotiontrianglegeometrydescriptor.json'
content_hash: 'sha256:a0e96ac991c89a07'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLAccelerationStructureMotionTriangleGeometryDescriptor

<sub>Class</sub>

A description of a list of triangle primitives, as motion keyframe data, to turn into an acceleration structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLAccelerationStructureMotionTriangleGeometryDescriptor
```

## Relationships

- **Inherits From**: [MTLAccelerationStructureGeometryDescriptor](mtlaccelerationstructuregeometrydescriptor.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Specifying the number of triangles

- [triangleCount](mtlaccelerationstructuremotiontrianglegeometrydescriptor/trianglecount.md) — The number of triangles in the buffers.

### Specifying index data

- [indexBuffer](mtlaccelerationstructuremotiontrianglegeometrydescriptor/indexbuffer.md) — A buffer that contains indices for the vertices that compose the triangle list.
- [indexType](mtlaccelerationstructuremotiontrianglegeometrydescriptor/indextype.md) — The data type of indices in the index buffer.
- [indexBufferOffset](mtlaccelerationstructuremotiontrianglegeometrydescriptor/indexbufferoffset.md) — The offset, in bytes, to the first index in the buffer.

### Specifying vertex data

- [vertexBuffers](mtlaccelerationstructuremotiontrianglegeometrydescriptor/vertexbuffers.md) — An array of motion keyframes, each containing triangle data.
- [vertexStride](mtlaccelerationstructuremotiontrianglegeometrydescriptor/vertexstride.md) — The stride, in bytes, between vertices in each vertex buffer.

### Instance Properties

- [transformationMatrixBuffer](mtlaccelerationstructuremotiontrianglegeometrydescriptor/transformationmatrixbuffer.md)
- [transformationMatrixBufferOffset](mtlaccelerationstructuremotiontrianglegeometrydescriptor/transformationmatrixbufferoffset.md)
- [transformationMatrixLayout](mtlaccelerationstructuremotiontrianglegeometrydescriptor/transformationmatrixlayout.md)
- [vertexFormat](mtlaccelerationstructuremotiontrianglegeometrydescriptor/vertexformat.md)

## See Also

### Motion geometry descriptors

- [MTL4AccelerationStructureMotionTriangleGeometryDescriptor](mtl4accelerationstructuremotiontrianglegeometrydescriptor.md) — Describes motion triangle geometry, suitable for motion ray tracing.
- [MTL4AccelerationStructureMotionCurveGeometryDescriptor](mtl4accelerationstructuremotioncurvegeometrydescriptor.md) — Describes motion curve geometry, suitable for motion ray tracing.
- [MTLAccelerationStructureMotionCurveGeometryDescriptor](mtlaccelerationstructuremotioncurvegeometrydescriptor.md)
- [MTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor](mtl4accelerationstructuremotionboundingboxgeometrydescriptor.md) — Describes motion bounding box geometry, suitable for motion ray tracing.
- [MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor](mtlaccelerationstructuremotionboundingboxgeometrydescriptor.md) — A description of a list of bounding boxes, as motion keyframe data, to turn into an acceleration structure.
- [MTLMotionKeyframeData](mtlmotionkeyframedata.md) — Geometry data for a specific keyframe to use in a moving instance.
