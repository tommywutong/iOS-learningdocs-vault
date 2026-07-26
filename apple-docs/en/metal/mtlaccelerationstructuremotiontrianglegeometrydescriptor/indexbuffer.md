---
title: indexBuffer
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructuremotiontrianglegeometrydescriptor/indexbuffer
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructuremotiontrianglegeometrydescriptor/indexbuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructuremotiontrianglegeometrydescriptor/indexbuffer.json'
content_hash: 'sha256:7d6c9da056799ee9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureMotionTriangleGeometryDescriptor](../mtlaccelerationstructuremotiontrianglegeometrydescriptor.md)

# indexBuffer

<sub>Instance Property</sub>

A buffer that contains indices for the vertices that compose the triangle list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var indexBuffer: (any MTLBuffer)? { get set }
```

## Discussion

This property can be `nil`, in which case the vertex data defines the triangle list implicitly. You need to store indices in a packed data format.

## See Also

### Specifying index data

- [indexType](indextype.md) — The data type of indices in the index buffer.
- [indexBufferOffset](indexbufferoffset.md) — The offset, in bytes, to the first index in the buffer.
