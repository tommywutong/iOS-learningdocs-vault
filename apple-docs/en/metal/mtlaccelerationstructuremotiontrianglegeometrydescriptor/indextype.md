---
title: indexType
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructuremotiontrianglegeometrydescriptor/indextype
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructuremotiontrianglegeometrydescriptor/indextype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructuremotiontrianglegeometrydescriptor/indextype.json'
content_hash: 'sha256:569a50920a80be4f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureMotionTriangleGeometryDescriptor](../mtlaccelerationstructuremotiontrianglegeometrydescriptor.md)

# indexType

<sub>Instance Property</sub>

The data type of indices in the index buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var indexType: MTLIndexType { get set }
```

## Discussion

The index type needs to be [MTLIndexTypeUInt16](../mtlindextype/uint16.md) or [MTLIndexTypeUInt32](../mtlindextype/uint32.md). The default is [MTLIndexTypeUInt32](../mtlindextype/uint32.md).

## See Also

### Specifying index data

- [indexBuffer](indexbuffer.md) — A buffer that contains indices for the vertices that compose the triangle list.
- [indexBufferOffset](indexbufferoffset.md) — The offset, in bytes, to the first index in the buffer.
