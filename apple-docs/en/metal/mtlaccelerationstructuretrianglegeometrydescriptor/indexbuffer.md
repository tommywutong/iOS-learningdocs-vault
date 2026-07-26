---
title: indexBuffer
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructuretrianglegeometrydescriptor/indexbuffer
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructuretrianglegeometrydescriptor/indexbuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructuretrianglegeometrydescriptor/indexbuffer.json'
content_hash: 'sha256:da58660d65831323'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureTriangleGeometryDescriptor](../mtlaccelerationstructuretrianglegeometrydescriptor.md)

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

### Configuring index data

- [indexType](indextype.md) — The data type of indices in the index buffer.
- [indexBufferOffset](indexbufferoffset.md) — The offset, in bytes, to the first index in the buffer.
