---
title: MTLDataType.rgb10a2Unorm
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldatatype/rgb10a2unorm
source_url: 'https://developer.apple.com/documentation/metal/mtldatatype/rgb10a2unorm'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldatatype/rgb10a2unorm.json'
content_hash: 'sha256:0237508aa8a6465c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDataType](../mtldatatype.md)

# MTLDataType.rgb10a2Unorm

<sub>Case</sub>

A packed 32-bit format with three color components, each of which is a 10-bit, normalized, unsigned integer value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case rgb10a2Unorm
```

## Discussion

The color components are in RGBA order, which stands for red, green, blue, and alpha. The red, green, and blue components each have 10 bits, and the alpha component has 2 bits.

## See Also

### 32-bit color integer types

- [MTLDataTypeRGBA8Snorm](rgba8snorm.md) — An ordinary pixel with four components, each of which is an 8-bit, normalized, signed integer value.
- [MTLDataTypeRGBA8Unorm](rgba8unorm.md) — An ordinary pixel with four components, each of which is an 8-bit, normalized, unsigned integer value.
- [MTLDataTypeRGBA8Unorm_sRGB](rgba8unorm_srgb.md) — An ordinary pixel with four components, each of which is an 8-bit, normalized, unsigned integer value in the sRGB color space.
- [MTLDataTypeRG16Snorm](rg16snorm.md) — An ordinary pixel with two components, each of which is a 16-bit, normalized, signed integer value.
- [MTLDataTypeRG16Unorm](rg16unorm.md) — An ordinary pixel with two components, each of which is a 16-bit, normalized, unsigned integer value.
