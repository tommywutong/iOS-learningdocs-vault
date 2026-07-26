---
title: vertexStride
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructuretrianglegeometrydescriptor/vertexstride
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructuretrianglegeometrydescriptor/vertexstride'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructuretrianglegeometrydescriptor/vertexstride.json'
content_hash: 'sha256:ba9e13df79008205'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureTriangleGeometryDescriptor](../mtlaccelerationstructuretrianglegeometrydescriptor.md)

# vertexStride

<sub>Instance Property</sub>

The stride, in bytes, between vertices in the vertex buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var vertexStride: Int { get set }
```

## Discussion

The stride needs to be at least 12 bytes and needs to be a multiple of 4 bytes. The default value is 12 bytes.

## See Also

### Configuring vertex data

- [vertexFormat](vertexformat.md) — The format of each vertex position in the vertex buffer property.
- [vertexBuffer](vertexbuffer.md) — A buffer that contains vertex data.
- [vertexBufferOffset](vertexbufferoffset.md) — The offset, in bytes, for the first vertex in the vertex buffer.
