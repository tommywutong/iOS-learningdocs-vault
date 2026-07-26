---
title: controlPointBuffer
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4accelerationstructurecurvegeometrydescriptor/controlpointbuffer
source_url: 'https://developer.apple.com/documentation/metal/mtl4accelerationstructurecurvegeometrydescriptor/controlpointbuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4accelerationstructurecurvegeometrydescriptor/controlpointbuffer.json'
content_hash: 'sha256:c2a170bf48af86fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4AccelerationStructureCurveGeometryDescriptor](../mtl4accelerationstructurecurvegeometrydescriptor.md)

# controlPointBuffer

<sub>Instance Property</sub>

References a buffer containing curve control points.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var controlPointBuffer: MTL4BufferRange { get set }
```

## Discussion

Control points are interpolated according to the basis function you specify in [curveBasis](curvebasis.md).

You are responsible for ensuring each control is in a format matching the control point format [controlPointFormat](controlpointformat.md) specifies, as well as ensuring that the buffer address of the range is not zero.
