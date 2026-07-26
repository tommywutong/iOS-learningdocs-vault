---
title: elementType
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlarraytype/elementtype
source_url: 'https://developer.apple.com/documentation/metal/mtlarraytype/elementtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlarraytype/elementtype.json'
content_hash: 'sha256:4bd160554b946ee4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArrayType](../mtlarraytype.md)

# elementType

<sub>Instance Property</sub>

The data type of the array’s elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var elementType: MTLDataType { get }
```

## Discussion

For information on possible values, see [MTLDataType](../mtldatatype.md).

## See Also

### Describing the array elements

- [arrayLength](arraylength.md) — The number of elements in the array.
- [stride](stride.md) — The stride between array elements, in bytes.
- [argumentIndexStride](argumentindexstride.md) — The stride, in bytes, between argument indices.
