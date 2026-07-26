---
title: indexBuffer
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructurecurvegeometrydescriptor/indexbuffer
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructurecurvegeometrydescriptor/indexbuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructurecurvegeometrydescriptor/indexbuffer.json'
content_hash: 'sha256:1c257ab20198364d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureCurveGeometryDescriptor](../mtlaccelerationstructurecurvegeometrydescriptor.md)

# indexBuffer

<sub>Instance Property</sub>

A buffer that contains references to control points in the control point buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var indexBuffer: (any MTLBuffer)? { get set }
```

## Discussion

This property needs to have a non-nil value when you build an acceleration structure.
