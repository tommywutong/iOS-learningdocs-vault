---
title: curveBasis
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4accelerationstructuremotioncurvegeometrydescriptor/curvebasis
source_url: 'https://developer.apple.com/documentation/metal/mtl4accelerationstructuremotioncurvegeometrydescriptor/curvebasis'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4accelerationstructuremotioncurvegeometrydescriptor/curvebasis.json'
content_hash: 'sha256:33f8ca6de3952593'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4AccelerationStructureMotionCurveGeometryDescriptor](../mtl4accelerationstructuremotioncurvegeometrydescriptor.md)

# curveBasis

<sub>Instance Property</sub>

Sets the curve basis function, determining how Metal interpolates the control points.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var curveBasis: MTLCurveBasis { get set }
```

## Discussion

Defaults to `MTLCurveBasisBSpline`. All keyframes share the same curve basis function.
