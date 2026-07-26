---
title: arrayLength
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlargumentdescriptor/arraylength
source_url: 'https://developer.apple.com/documentation/metal/mtlargumentdescriptor/arraylength'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargumentdescriptor/arraylength.json'
content_hash: 'sha256:a81fa19ffbdb85c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgumentDescriptor](../mtlargumentdescriptor.md)

# arrayLength

<sub>Instance Property</sub>

The length of an array argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var arrayLength: Int { get set }
```

## Discussion

For a nonarray argument, this value needs to be `0`.

## See Also

### Setting the descriptor’s properties

- [dataType](datatype.md) — The data type of the argument.
- [index](index.md) — The index ID of the argument.
- [access](access.md) — The access permissions of the argument.
- [constantBlockAlignment](constantblockalignment.md) — The alignment of the constant block.
- [textureType](texturetype.md) — The texture type of a texture argument.
