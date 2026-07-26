---
title: boundingBoxStride
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4accelerationstructuremotionboundingboxgeometrydescriptor/boundingboxstride
source_url: 'https://developer.apple.com/documentation/metal/mtl4accelerationstructuremotionboundingboxgeometrydescriptor/boundingboxstride'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4accelerationstructuremotionboundingboxgeometrydescriptor/boundingboxstride.json'
content_hash: 'sha256:8d98eb8ac1197cf5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor](../mtl4accelerationstructuremotionboundingboxgeometrydescriptor.md)

# boundingBoxStride

<sub>Instance Property</sub>

Declares the stride, in bytes, between bounding boxes in the bounding box buffers each entry in `boundingBoxBuffer` references.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var boundingBoxStride: Int { get set }
```

## Discussion

All keyframes share the same bounding box stride. You are responsible for ensuring this stride is at least 24 bytes and a multiple of 4 bytes.

This property defaults to `24` bytes.
