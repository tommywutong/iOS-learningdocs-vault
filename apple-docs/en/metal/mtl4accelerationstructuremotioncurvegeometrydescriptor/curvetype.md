---
title: curveType
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4accelerationstructuremotioncurvegeometrydescriptor/curvetype
source_url: 'https://developer.apple.com/documentation/metal/mtl4accelerationstructuremotioncurvegeometrydescriptor/curvetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4accelerationstructuremotioncurvegeometrydescriptor/curvetype.json'
content_hash: 'sha256:59bd28ebf397ff53'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4AccelerationStructureMotionCurveGeometryDescriptor](../mtl4accelerationstructuremotioncurvegeometrydescriptor.md)

# curveType

<sub>Instance Property</sub>

Controls the curve type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var curveType: MTLCurveType { get set }
```

## Discussion

Defaults to `MTLCurveTypeRound`. All keyframes share the same curve type.
