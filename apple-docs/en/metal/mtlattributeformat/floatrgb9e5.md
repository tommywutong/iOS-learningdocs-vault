---
title: MTLAttributeFormat.floatRGB9E5
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlattributeformat/floatrgb9e5
source_url: 'https://developer.apple.com/documentation/metal/mtlattributeformat/floatrgb9e5'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlattributeformat/floatrgb9e5.json'
content_hash: 'sha256:34df20fd6c506b77'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAttributeFormat](../mtlattributeformat.md)

# MTLAttributeFormat.floatRGB9E5

<sub>Case</sub>

One packed 32-bit value representing pixel data containing 9-bit float red, green, and blue channels, and a 5-bit float shared exponent channel.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case floatRGB9E5
```

## Discussion

This data format is identical to [MTLPixelFormatRGB9E5Float](../mtlpixelformat/rgb9e5float.md), and used in compute functions for manipulating pixels.

## See Also

### 32-bit floating-point formats

- [MTLAttributeFormatFloat](float.md) — A 32-bit floating-point value.
- [MTLAttributeFormatFloat2](float2.md) — A two-component vector with 32-bit floating-point values.
- [MTLAttributeFormatFloat3](float3.md) — A three-component vector with 32-bit floating-point values.
- [MTLAttributeFormatFloat4](float4.md) — A four-component vector with 32-bit floating-point values.
- [MTLAttributeFormatFloatRG11B10](floatrg11b10.md) — One packed 32-bit value representing pixel data containing 11-bit float red and green channels, and a 10-bit float blue channel.
