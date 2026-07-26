---
title: boundingBoxBuffers
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructuremotionboundingboxgeometrydescriptor/boundingboxbuffers
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructuremotionboundingboxgeometrydescriptor/boundingboxbuffers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructuremotionboundingboxgeometrydescriptor/boundingboxbuffers.json'
content_hash: 'sha256:ab0fcd753599937d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor](../mtlaccelerationstructuremotionboundingboxgeometrydescriptor.md)

# boundingBoxBuffers

<sub>Instance Property</sub>

A array of motion keyframes, each containing bounding box data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var boundingBoxBuffers: [MTLMotionKeyframeData] { get set }
```

## See Also

### Specifying bounding boxes data

- [boundingBoxStride](boundingboxstride.md) — The stride, in bytes, between bounding boxes in each buffer.
