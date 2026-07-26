---
title: vertexBuffer
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructuretrianglegeometrydescriptor/vertexbuffer
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructuretrianglegeometrydescriptor/vertexbuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructuretrianglegeometrydescriptor/vertexbuffer.json'
content_hash: 'sha256:bdc3e6306b3d3a22'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureTriangleGeometryDescriptor](../mtlaccelerationstructuretrianglegeometrydescriptor.md)

# vertexBuffer

<sub>Instance Property</sub>

A buffer that contains vertex data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var vertexBuffer: (any MTLBuffer)? { get set }
```

## Discussion

The [vertexFormat](vertexformat.md) property defines the format of each vertex position in the buffer. You need to set a vertex buffer before creating the acceleration structure.

## See Also

### Configuring vertex data

- [vertexFormat](vertexformat.md) — The format of each vertex position in the vertex buffer property.
- [vertexBufferOffset](vertexbufferoffset.md) — The offset, in bytes, for the first vertex in the vertex buffer.
- [vertexStride](vertexstride.md) — The stride, in bytes, between vertices in the vertex buffer.
