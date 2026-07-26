---
title: indexBufferOffset
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructuremotiontrianglegeometrydescriptor/indexbufferoffset
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructuremotiontrianglegeometrydescriptor/indexbufferoffset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructuremotiontrianglegeometrydescriptor/indexbufferoffset.json'
content_hash: 'sha256:615da6065a4d38f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureMotionTriangleGeometryDescriptor](../mtlaccelerationstructuremotiontrianglegeometrydescriptor.md)

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

### Specifying index data

- [indexBuffer](indexbuffer.md) — A buffer that contains indices for the vertices that compose the triangle list.
- [indexType](indextype.md) — The data type of indices in the index buffer.
