---
title: boundingBoxCount
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4accelerationstructuremotionboundingboxgeometrydescriptor/boundingboxcount
source_url: 'https://developer.apple.com/documentation/metal/mtl4accelerationstructuremotionboundingboxgeometrydescriptor/boundingboxcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4accelerationstructuremotionboundingboxgeometrydescriptor/boundingboxcount.json'
content_hash: 'sha256:5595ed78d19bac4e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor](../mtl4accelerationstructuremotionboundingboxgeometrydescriptor.md)

# boundingBoxCount

<sub>Instance Property</sub>

Declares the number of bounding boxes in each buffer that `boundingBoxBuffer` references.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var boundingBoxCount: Int { get set }
```

## Discussion

All keyframes share the same bounding box count.
