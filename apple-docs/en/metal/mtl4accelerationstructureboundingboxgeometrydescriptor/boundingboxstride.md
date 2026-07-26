---
title: boundingBoxStride
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4accelerationstructureboundingboxgeometrydescriptor/boundingboxstride
source_url: 'https://developer.apple.com/documentation/metal/mtl4accelerationstructureboundingboxgeometrydescriptor/boundingboxstride'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4accelerationstructureboundingboxgeometrydescriptor/boundingboxstride.json'
content_hash: 'sha256:fd65e40c7429e4fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4AccelerationStructureBoundingBoxGeometryDescriptor](../mtl4accelerationstructureboundingboxgeometrydescriptor.md)

# boundingBoxStride

<sub>Instance Property</sub>

Assigns the stride, in bytes, between bounding boxes in the bounding box buffer `boundingBoxBuffer` references.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var boundingBoxStride: Int { get set }
```

## Discussion

You are responsible for ensuring this stride is at least 24 bytes and a multiple of 4 bytes.

This property defaults to `24` bytes.
