---
title: radiusBuffer
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4accelerationstructurecurvegeometrydescriptor/radiusbuffer
source_url: 'https://developer.apple.com/documentation/metal/mtl4accelerationstructurecurvegeometrydescriptor/radiusbuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4accelerationstructurecurvegeometrydescriptor/radiusbuffer.json'
content_hash: 'sha256:f8190d7dbdca6376'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4AccelerationStructureCurveGeometryDescriptor](../mtl4accelerationstructurecurvegeometrydescriptor.md)

# radiusBuffer

<sub>Instance Property</sub>

Assigns a reference to a buffer containing the curve radius for each control point.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var radiusBuffer: MTL4BufferRange { get set }
```

## Discussion

Metal interpolates curve radii according to the basis function you specify via [curveBasis](curvebasis.md).

You are responsible for ensuring the type of each radius matches the type property [radiusFormat](radiusformat.md) specifies, that each radius is at least zero, and that the buffer address of the range is not zero.
