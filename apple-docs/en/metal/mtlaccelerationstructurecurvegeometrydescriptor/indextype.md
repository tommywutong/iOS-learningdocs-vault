---
title: indexType
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructurecurvegeometrydescriptor/indextype
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructurecurvegeometrydescriptor/indextype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructurecurvegeometrydescriptor/indextype.json'
content_hash: 'sha256:96e83b70852a7256'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureCurveGeometryDescriptor](../mtlaccelerationstructurecurvegeometrydescriptor.md)

# indexType

<sub>Instance Property</sub>

The size of each index in the index buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var indexType: MTLIndexType { get set }
```

## Discussion

Set this property to a value that reflects the size of the indices in the [indexBuffer](indexbuffer.md) property, such as [MTLIndexTypeUInt16](../mtlindextype/uint16.md) or [MTLIndexTypeUInt32](../mtlindextype/uint32.md).
