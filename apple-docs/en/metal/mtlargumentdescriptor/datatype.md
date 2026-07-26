---
title: dataType
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlargumentdescriptor/datatype
source_url: 'https://developer.apple.com/documentation/metal/mtlargumentdescriptor/datatype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargumentdescriptor/datatype.json'
content_hash: 'sha256:4a4310875d6dc7d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgumentDescriptor](../mtlargumentdescriptor.md)

# dataType

<sub>Instance Property</sub>

The data type of the argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var dataType: MTLDataType { get set }
```

## Discussion

For a constant data argument, this value needs to match the binary format of the data stored in the buffer for that argument. For other parameter types, such as textures or samplers, specify the appropriate constant. See [MTLDataType](../mtldatatype.md) for possible values.

## See Also

### Setting the descriptor’s properties

- [index](index.md) — The index ID of the argument.
- [access](access.md) — The access permissions of the argument.
- [arrayLength](arraylength.md) — The length of an array argument.
- [constantBlockAlignment](constantblockalignment.md) — The alignment of the constant block.
- [textureType](texturetype.md) — The texture type of a texture argument.
