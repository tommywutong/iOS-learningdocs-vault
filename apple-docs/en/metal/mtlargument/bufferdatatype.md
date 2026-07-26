---
title: bufferDataType
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（16.0 起废弃）, iPadOS 8.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.11+（13.0 起废弃）, tvOS（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtlargument/bufferdatatype
source_url: 'https://developer.apple.com/documentation/metal/mtlargument/bufferdatatype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargument/bufferdatatype.json'
content_hash: 'sha256:e37abfcb8740fe5f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgument](../mtlargument.md)

# bufferDataType

<sub>Instance Property</sub>

The data type of the buffer data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var bufferDataType: MTLDataType { get }
```

## Discussion

If the argument is not a buffer, querying this property is a fatal error.

## See Also

### Describing a buffer argument

- [bufferAlignment](bufferalignment.md) — The required byte alignment in memory for the buffer data. _(deprecated)_
- [bufferDataSize](bufferdatasize.md) — The size, in bytes, of the buffer data. _(deprecated)_
- [bufferStructType](bufferstructtype.md) — A description of the structure data of a buffer argument. _(deprecated)_
- [bufferPointerType](bufferpointertype.md) — A description of the pointer to a buffer argument. _(deprecated)_
