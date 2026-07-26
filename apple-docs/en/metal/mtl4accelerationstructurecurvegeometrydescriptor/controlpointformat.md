---
title: controlPointFormat
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4accelerationstructurecurvegeometrydescriptor/controlpointformat
source_url: 'https://developer.apple.com/documentation/metal/mtl4accelerationstructurecurvegeometrydescriptor/controlpointformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4accelerationstructurecurvegeometrydescriptor/controlpointformat.json'
content_hash: 'sha256:c865800f2e782c94'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4AccelerationStructureCurveGeometryDescriptor](../mtl4accelerationstructurecurvegeometrydescriptor.md)

# controlPointFormat

<sub>Instance Property</sub>

Declares the format of the control points the control point buffer references.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var controlPointFormat: MTLAttributeFormat { get set }
```

## Discussion

Defaults to `MTLAttributeFormatFloat3`, representing 3 floating point values tightly packed.
