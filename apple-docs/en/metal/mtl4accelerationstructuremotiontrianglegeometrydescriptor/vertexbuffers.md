---
title: vertexBuffers
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4accelerationstructuremotiontrianglegeometrydescriptor/vertexbuffers
source_url: 'https://developer.apple.com/documentation/metal/mtl4accelerationstructuremotiontrianglegeometrydescriptor/vertexbuffers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4accelerationstructuremotiontrianglegeometrydescriptor/vertexbuffers.json'
content_hash: 'sha256:42d2c02ecba8b8ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4AccelerationStructureMotionTriangleGeometryDescriptor](../mtl4accelerationstructuremotiontrianglegeometrydescriptor.md)

# vertexBuffers

<sub>Instance Property</sub>

Assigns a buffer where each entry contains a reference to a vertex buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var vertexBuffers: MTL4BufferRange { get set }
```

## Discussion

This property references a buffer that conceptually represents an array with one entry for each keyframe in the motion animation. Each one of these entries consists of a [MTL4BufferRange](../mtl4bufferrange.md) that, in turn, references a vertex buffer containing the vertex data for the keyframe.

You are responsible for ensuring the buffer address is not zero for the top-level buffer, as well as for all the vertex buffers it references.
