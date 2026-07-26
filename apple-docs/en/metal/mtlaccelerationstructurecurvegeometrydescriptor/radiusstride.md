---
title: radiusStride
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructurecurvegeometrydescriptor/radiusstride
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructurecurvegeometrydescriptor/radiusstride'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructurecurvegeometrydescriptor/radiusstride.json'
content_hash: 'sha256:33726dcd37846b7c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureCurveGeometryDescriptor](../mtlaccelerationstructurecurvegeometrydescriptor.md)

# radiusStride

<sub>Instance Property</sub>

The stride, in bytes, between the radius elements in the radius buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var radiusStride: Int { get set }
```

## Discussion

The stride needs to be a multiple of the radius format size you configure with the [radiusFormat](radiusformat.md) property. The default value is `0`, which indicates that the radius elements in the buffer have zero bytes of padding between them.
