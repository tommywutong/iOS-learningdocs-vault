---
title: MTLDataType.rg11b10Float
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldatatype/rg11b10float
source_url: 'https://developer.apple.com/documentation/metal/mtldatatype/rg11b10float'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldatatype/rg11b10float.json'
content_hash: 'sha256:be57003bbad17248'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDataType](../mtldatatype.md)

# MTLDataType.rg11b10Float

<sub>Case</sub>

A packed 32-bit format with three floating-point color components, two of which are 11-bit values, and one is a 10-bit value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case rg11b10Float
```

## Discussion

The 11-bit components for red and green each store five exponent bits and six mantissa bits. The 10-bit blue component stores five exponent bits and five mantissa bits.

> [!note] Note
> None of the color components have a sign bit.

## See Also

### 32-bit color floating-point types

- [MTLDataTypeRGB9E5Float](rgb9e5float.md) — A packed 32-bit format with three color components, each of which is a 9-bit floating-point value.
