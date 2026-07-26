---
title: constantBlockAlignment
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlargumentdescriptor/constantblockalignment
source_url: 'https://developer.apple.com/documentation/metal/mtlargumentdescriptor/constantblockalignment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargumentdescriptor/constantblockalignment.json'
content_hash: 'sha256:017f6f8997ab6130'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgumentDescriptor](../mtlargumentdescriptor.md)

# constantBlockAlignment

<sub>Instance Property</sub>

The alignment of the constant block.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var constantBlockAlignment: Int { get set }
```

## Discussion

If set, this property forces the constant block to be aligned to the specified value. It should be set on the first constant only, and is valid only if a corresponding explicit `alignas` specifier is applied to the constant in the Metal shader language.

## See Also

### Setting the descriptor’s properties

- [dataType](datatype.md) — The data type of the argument.
- [index](index.md) — The index ID of the argument.
- [access](access.md) — The access permissions of the argument.
- [arrayLength](arraylength.md) — The length of an array argument.
- [textureType](texturetype.md) — The texture type of a texture argument.
