---
title: boundingBoxBuffer
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4accelerationstructureboundingboxgeometrydescriptor/boundingboxbuffer
source_url: 'https://developer.apple.com/documentation/metal/mtl4accelerationstructureboundingboxgeometrydescriptor/boundingboxbuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4accelerationstructureboundingboxgeometrydescriptor/boundingboxbuffer.json'
content_hash: 'sha256:cde1275126982898'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4AccelerationStructureBoundingBoxGeometryDescriptor](../mtl4accelerationstructureboundingboxgeometrydescriptor.md)

# boundingBoxBuffer

<sub>Instance Property</sub>

References a buffer containing bounding box data in `MTLAxisAlignedBoundingBoxes` format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var boundingBoxBuffer: MTL4BufferRange { get set }
```

## Discussion

You are responsible for ensuring the buffer address of the range is not zero.
