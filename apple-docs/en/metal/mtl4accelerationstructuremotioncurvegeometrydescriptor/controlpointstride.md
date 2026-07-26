---
title: controlPointStride
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4accelerationstructuremotioncurvegeometrydescriptor/controlpointstride
source_url: 'https://developer.apple.com/documentation/metal/mtl4accelerationstructuremotioncurvegeometrydescriptor/controlpointstride'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4accelerationstructuremotioncurvegeometrydescriptor/controlpointstride.json'
content_hash: 'sha256:433370c293d6e5c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4AccelerationStructureMotionCurveGeometryDescriptor](../mtl4accelerationstructuremotioncurvegeometrydescriptor.md)

# controlPointStride

<sub>Instance Property</sub>

Sets the stride, in bytes, between control points in the control point buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var controlPointStride: Int { get set }
```

## Discussion

All keyframes share the same control point stride.

You are responsible for ensuring this stride is a multiple of the control point format’s element size, and at a minimum exactly the control point format’s size.

This property defaults to `0`, indicating that the control points are tightly-packed.
