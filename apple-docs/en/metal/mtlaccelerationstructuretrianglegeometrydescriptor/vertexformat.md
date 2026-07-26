---
title: vertexFormat
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructuretrianglegeometrydescriptor/vertexformat
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructuretrianglegeometrydescriptor/vertexformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructuretrianglegeometrydescriptor/vertexformat.json'
content_hash: 'sha256:97d5db6ca7525246'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureTriangleGeometryDescriptor](../mtlaccelerationstructuretrianglegeometrydescriptor.md)

# vertexFormat

<sub>Instance Property</sub>

The format of each vertex position in the vertex buffer property.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var vertexFormat: MTLAttributeFormat { get set }
```

## Discussion

Set this property to a value that represents the pixel format of the data you assign to the [vertexBuffer](vertexbuffer.md) property. The property’s default is [MTLAttributeFormatFloat3](../mtlattributeformat/float3.md).

## See Also

### Configuring vertex data

- [vertexBuffer](vertexbuffer.md) — A buffer that contains vertex data.
- [vertexBufferOffset](vertexbufferoffset.md) — The offset, in bytes, for the first vertex in the vertex buffer.
- [vertexStride](vertexstride.md) — The stride, in bytes, between vertices in the vertex buffer.
