---
title: radiusStride
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4accelerationstructuremotioncurvegeometrydescriptor/radiusstride
source_url: 'https://developer.apple.com/documentation/metal/mtl4accelerationstructuremotioncurvegeometrydescriptor/radiusstride'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4accelerationstructuremotioncurvegeometrydescriptor/radiusstride.json'
content_hash: 'sha256:cf8c21d8e34edf98'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4AccelerationStructureMotionCurveGeometryDescriptor](../mtl4accelerationstructuremotioncurvegeometrydescriptor.md)

# radiusStride

<sub>Instance Property</sub>

Sets the stride, in bytes, between radii in the radius buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var radiusStride: Int { get set }
```

## Discussion

You are responsible for ensuring this property is set to a multiple of the size corresponding to the [radiusFormat](radiusformat.md). All keyframes share the same radius stride.

This property defaults to `0` bytes, indicating that the radii are tightly packed.
