---
title: vertexBufferOffset
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructuretrianglegeometrydescriptor/vertexbufferoffset
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructuretrianglegeometrydescriptor/vertexbufferoffset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructuretrianglegeometrydescriptor/vertexbufferoffset.json'
content_hash: 'sha256:0d99be7d41c645ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureTriangleGeometryDescriptor](../mtlaccelerationstructuretrianglegeometrydescriptor.md)

# vertexBufferOffset

<sub>Instance Property</sub>

The offset, in bytes, for the first vertex in the vertex buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var vertexBufferOffset: Int { get set }
```

## Discussion

The offset needs to be a multiple of the vertex stride. Check the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) for potential alignment restrictions. The default value is `0`.

## See Also

### Configuring vertex data

- [vertexFormat](vertexformat.md) — The format of each vertex position in the vertex buffer property.
- [vertexBuffer](vertexbuffer.md) — A buffer that contains vertex data.
- [vertexStride](vertexstride.md) — The stride, in bytes, between vertices in the vertex buffer.
