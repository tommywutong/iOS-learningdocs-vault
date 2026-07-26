---
title: controlPointStride
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructurecurvegeometrydescriptor/controlpointstride
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructurecurvegeometrydescriptor/controlpointstride'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructurecurvegeometrydescriptor/controlpointstride.json'
content_hash: 'sha256:d2241587bce4c739'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureCurveGeometryDescriptor](../mtlaccelerationstructurecurvegeometrydescriptor.md)

# controlPointStride

<sub>Instance Property</sub>

The stride, in bytes, between control points in the buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var controlPointStride: Int { get set }
```

## Discussion

The stride needs to be a multiple of the format element size you configure with the [controlPointFormat](controlpointformat.md) property, and at least the format’s size. The default value is `0`, which indicates that the control point elements in the buffer have zero bytes of padding between them.
