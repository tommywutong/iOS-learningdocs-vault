---
title: MTLDataType.rgb9e5Float
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldatatype/rgb9e5float
source_url: 'https://developer.apple.com/documentation/metal/mtldatatype/rgb9e5float'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldatatype/rgb9e5float.json'
content_hash: 'sha256:3395d7fc31f82e22'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDataType](../mtldatatype.md)

# MTLDataType.rgb9e5Float

<sub>Case</sub>

A packed 32-bit format with three color components, each of which is a 9-bit floating-point value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case rgb9e5Float
```

## Discussion

The color components are in RGBA order, which stands for red, green, blue, and alpha. The red, green, and blue components each have 9 bits, and the alpha component has 5 bits.

## See Also

### 32-bit color floating-point types

- [MTLDataTypeRG11B10Float](rg11b10float.md) — A packed 32-bit format with three floating-point color components, two of which are 11-bit values, and one is a 10-bit value.
