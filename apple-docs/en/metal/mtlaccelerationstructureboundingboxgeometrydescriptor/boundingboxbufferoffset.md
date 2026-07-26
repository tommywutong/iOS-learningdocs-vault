---
title: boundingBoxBufferOffset
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructureboundingboxgeometrydescriptor/boundingboxbufferoffset
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructureboundingboxgeometrydescriptor/boundingboxbufferoffset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructureboundingboxgeometrydescriptor/boundingboxbufferoffset.json'
content_hash: 'sha256:9b46a74e47276eb7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureBoundingBoxGeometryDescriptor](../mtlaccelerationstructureboundingboxgeometrydescriptor.md)

# boundingBoxBufferOffset

<sub>Instance Property</sub>

The offset, in bytes, to the first bounding box in the buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var boundingBoxBufferOffset: Int { get set }
```

## Discussion

The offset needs to be a multiple of [boundingBoxStride](boundingboxstride.md). Check the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) for potential alignment restrictions.

## See Also

### Specifying bounding boxes data

- [boundingBoxBuffer](boundingboxbuffer.md) — A buffer that contains an array of bounding box structures.
- [boundingBoxStride](boundingboxstride.md) — The stride, in bytes, between bounding boxes in the buffer.
