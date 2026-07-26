---
title: bufferStructType
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（16.0 起废弃）, iPadOS 8.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.11+（13.0 起废弃）, tvOS（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtlargument/bufferstructtype
source_url: 'https://developer.apple.com/documentation/metal/mtlargument/bufferstructtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargument/bufferstructtype.json'
content_hash: 'sha256:f4dc680641864060'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgument](../mtlargument.md)

# bufferStructType

<sub>Instance Property</sub>

A description of the structure data of a buffer argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var bufferStructType: MTLStructType? { get }
```

## Discussion

If the buffer data type is [MTLDataTypeStruct](../mtldatatype/struct.md), this property describes the type of the struct; otherwise, this property is `nil`.

## See Also

### Describing a buffer argument

- [bufferAlignment](bufferalignment.md) — The required byte alignment in memory for the buffer data. _(deprecated)_
- [bufferDataSize](bufferdatasize.md) — The size, in bytes, of the buffer data. _(deprecated)_
- [bufferDataType](bufferdatatype.md) — The data type of the buffer data. _(deprecated)_
- [bufferPointerType](bufferpointertype.md) — A description of the pointer to a buffer argument. _(deprecated)_
