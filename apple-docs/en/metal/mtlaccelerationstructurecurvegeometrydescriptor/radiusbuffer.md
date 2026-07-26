---
title: radiusBuffer
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructurecurvegeometrydescriptor/radiusbuffer
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructurecurvegeometrydescriptor/radiusbuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructurecurvegeometrydescriptor/radiusbuffer.json'
content_hash: 'sha256:52995e888f8ed33e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureCurveGeometryDescriptor](../mtlaccelerationstructurecurvegeometrydescriptor.md)

# radiusBuffer

<sub>Instance Property</sub>

A buffer that contains the curve radius for each control point.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var radiusBuffer: (any MTLBuffer)? { get set }
```

## Discussion

The buffer contains values that are greater than or equal to `0.0` in the format you configure with the [radiusFormat](radiusformat.md) property. This property needs to have a non-nil value when you build an acceleration structure.
