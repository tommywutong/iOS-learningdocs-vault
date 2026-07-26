---
title: controlPointBuffers
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4accelerationstructuremotioncurvegeometrydescriptor/controlpointbuffers
source_url: 'https://developer.apple.com/documentation/metal/mtl4accelerationstructuremotioncurvegeometrydescriptor/controlpointbuffers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4accelerationstructuremotioncurvegeometrydescriptor/controlpointbuffers.json'
content_hash: 'sha256:c41a584085fae351'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4AccelerationStructureMotionCurveGeometryDescriptor](../mtl4accelerationstructuremotioncurvegeometrydescriptor.md)

# controlPointBuffers

<sub>Instance Property</sub>

Assigns a reference to a buffer where each entry contains a reference to a buffer of control points.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var controlPointBuffers: MTL4BufferRange { get set }
```

## Discussion

This property references a buffer that conceptually represents an array with one entry for each keyframe in the motion animation. Each one of these entries consists of a [MTL4BufferRange](../mtl4bufferrange.md) that, in turn, references a buffer containing the control points corresponding to the keyframe.

You are responsible for ensuring the buffer address is not zero for the top-level buffer, as well as for all the vertex buffers it references.
