---
title: dataType
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlstructmember/datatype
source_url: 'https://developer.apple.com/documentation/metal/mtlstructmember/datatype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlstructmember/datatype.json'
content_hash: 'sha256:ee8f654d4cbd14e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLStructMember](../mtlstructmember.md)

# dataType

<sub>Instance Property</sub>

The data type of the struct member.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var dataType: MTLDataType { get }
```

## Discussion

For information on possible values, see [MTLDataType](../mtldatatype.md). If the value is [MTLDataTypeArray](../mtldatatype/array.md), then the [- arrayType](<arraytype().md>) method returns an object that describes the underlying array. If the value is [MTLDataTypeStruct](../mtldatatype/struct.md), then the [- structType](<structtype().md>) method returns an object that describes the underlying struct.

## See Also

### Describing the struct member

- [name](name.md) — The name of the struct member.
- [offset](offset.md) — The location of this member relative to the start of its struct, in bytes.
- [argumentIndex](argumentindex.md) — The index in the argument table that corresponds to the struct member.
