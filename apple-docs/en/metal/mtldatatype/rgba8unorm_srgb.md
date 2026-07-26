---
title: MTLDataType.rgba8Unorm_srgb
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldatatype/rgba8unorm_srgb
source_url: 'https://developer.apple.com/documentation/metal/mtldatatype/rgba8unorm_srgb'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldatatype/rgba8unorm_srgb.json'
content_hash: 'sha256:e3bf7bfc724c6997'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDataType](../mtldatatype.md)

# MTLDataType.rgba8Unorm_srgb

<sub>Case</sub>

An ordinary pixel with four components, each of which is an 8-bit, normalized, unsigned integer value in the sRGB color space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case rgba8Unorm_srgb
```

## Discussion

The color components are in RGBA order, which stands for red, green, blue, and alpha.

## See Also

### 32-bit color integer types

- [MTLDataTypeRGBA8Snorm](rgba8snorm.md) — An ordinary pixel with four components, each of which is an 8-bit, normalized, signed integer value.
- [MTLDataTypeRGBA8Unorm](rgba8unorm.md) — An ordinary pixel with four components, each of which is an 8-bit, normalized, unsigned integer value.
- [MTLDataTypeRG16Snorm](rg16snorm.md) — An ordinary pixel with two components, each of which is a 16-bit, normalized, signed integer value.
- [MTLDataTypeRG16Unorm](rg16unorm.md) — An ordinary pixel with two components, each of which is a 16-bit, normalized, unsigned integer value.
- [MTLDataTypeRGB10A2Unorm](rgb10a2unorm.md) — A packed 32-bit format with three color components, each of which is a 10-bit, normalized, unsigned integer value.
