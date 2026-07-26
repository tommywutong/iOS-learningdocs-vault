---
title: segmentControlPointCount
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4accelerationstructurecurvegeometrydescriptor/segmentcontrolpointcount
source_url: 'https://developer.apple.com/documentation/metal/mtl4accelerationstructurecurvegeometrydescriptor/segmentcontrolpointcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4accelerationstructurecurvegeometrydescriptor/segmentcontrolpointcount.json'
content_hash: 'sha256:0ac1041436b42f29'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4AccelerationStructureCurveGeometryDescriptor](../mtl4accelerationstructurecurvegeometrydescriptor.md)

# segmentControlPointCount

<sub>Instance Property</sub>

Declares the number of control points per curve segment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var segmentControlPointCount: Int { get set }
```

## Discussion

Valid values for this property are `2`, `3`, or `4`.
