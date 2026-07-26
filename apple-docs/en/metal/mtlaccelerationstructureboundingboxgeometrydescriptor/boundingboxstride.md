---
title: boundingBoxStride
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructureboundingboxgeometrydescriptor/boundingboxstride
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructureboundingboxgeometrydescriptor/boundingboxstride'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructureboundingboxgeometrydescriptor/boundingboxstride.json'
content_hash: 'sha256:1b205127e1ed1922'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureBoundingBoxGeometryDescriptor](../mtlaccelerationstructureboundingboxgeometrydescriptor.md)

# boundingBoxStride

<sub>Instance Property</sub>

The stride, in bytes, between bounding boxes in the buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var boundingBoxStride: Int { get set }
```

## Discussion

The stride needs be at least 24 bytes, and be a multiple of 4 bytes. The default value is 24 bytes.

## See Also

### Specifying bounding boxes data

- [boundingBoxBuffer](boundingboxbuffer.md) — A buffer that contains an array of bounding box structures.
- [boundingBoxBufferOffset](boundingboxbufferoffset.md) — The offset, in bytes, to the first bounding box in the buffer.
