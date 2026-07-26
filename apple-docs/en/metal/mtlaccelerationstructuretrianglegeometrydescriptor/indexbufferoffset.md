---
title: indexBufferOffset
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructuretrianglegeometrydescriptor/indexbufferoffset
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructuretrianglegeometrydescriptor/indexbufferoffset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructuretrianglegeometrydescriptor/indexbufferoffset.json'
content_hash: 'sha256:cb75130fb6cd7c43'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureTriangleGeometryDescriptor](../mtlaccelerationstructuretrianglegeometrydescriptor.md)

# indexBufferOffset

<sub>Instance Property</sub>

The offset, in bytes, to the first index in the buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var indexBufferOffset: Int { get set }
```

## Discussion

The offset needs to be a multiple of the index data type size and aligned to the index data type’s alignment. Check the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) for potential alignment restrictions.

## See Also

### Configuring index data

- [indexType](indextype.md) — The data type of indices in the index buffer.
- [indexBuffer](indexbuffer.md) — A buffer that contains indices for the vertices that compose the triangle list.
