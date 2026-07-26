---
title: bufferPointerType
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+（16.0 起废弃）, iPadOS 11.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.13+（13.0 起废弃）, tvOS 11.0+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtlargument/bufferpointertype
source_url: 'https://developer.apple.com/documentation/metal/mtlargument/bufferpointertype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargument/bufferpointertype.json'
content_hash: 'sha256:fdaf74cfda73ad97'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgument](../mtlargument.md)

# bufferPointerType

<sub>Instance Property</sub>

A description of the pointer to a buffer argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var bufferPointerType: MTLPointerType? { get }
```

## Discussion

This property describes the type of the pointer to the buffer.

## See Also

### Describing a buffer argument

- [bufferAlignment](bufferalignment.md) — The required byte alignment in memory for the buffer data. _(deprecated)_
- [bufferDataSize](bufferdatasize.md) — The size, in bytes, of the buffer data. _(deprecated)_
- [bufferDataType](bufferdatatype.md) — The data type of the buffer data. _(deprecated)_
- [bufferStructType](bufferstructtype.md) — A description of the structure data of a buffer argument. _(deprecated)_
