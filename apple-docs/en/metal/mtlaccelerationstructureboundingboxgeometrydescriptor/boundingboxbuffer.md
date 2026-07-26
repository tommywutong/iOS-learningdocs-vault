---
title: boundingBoxBuffer
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructureboundingboxgeometrydescriptor/boundingboxbuffer
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructureboundingboxgeometrydescriptor/boundingboxbuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructureboundingboxgeometrydescriptor/boundingboxbuffer.json'
content_hash: 'sha256:4a87a61a9c3bd6eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureBoundingBoxGeometryDescriptor](../mtlaccelerationstructureboundingboxgeometrydescriptor.md)

# boundingBoxBuffer

<sub>Instance Property</sub>

A buffer that contains an array of bounding box structures.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var boundingBoxBuffer: (any MTLBuffer)? { get set }
```

## Discussion

The buffer contains an array of [MTLAxisAlignedBoundingBox](../mtlaxisalignedboundingbox-c.struct.md) structures, one for each bounding box in the geometry.

## See Also

### Specifying bounding boxes data

- [boundingBoxBufferOffset](boundingboxbufferoffset.md) — The offset, in bytes, to the first bounding box in the buffer.
- [boundingBoxStride](boundingboxstride.md) — The stride, in bytes, between bounding boxes in the buffer.
