---
title: MTLVertexFormat.floatRG11B10
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlvertexformat/floatrg11b10
source_url: 'https://developer.apple.com/documentation/metal/mtlvertexformat/floatrg11b10'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlvertexformat/floatrg11b10.json'
content_hash: 'sha256:89f096458c54e578'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLVertexFormat](../mtlvertexformat.md)

# MTLVertexFormat.floatRG11B10

<sub>Case</sub>

A three-component vector with 11-bit floating-point values for red and green, and a 10-bit value for blue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case floatRG11B10
```

## Discussion

The 11-bit components for red and green each store five exponent bits and six mantissa bits. The 10-bit blue component stores five exponent bits and five mantissa bits.

## See Also

### 32-bit floating-point formats

- [MTLVertexFormatFloat](float.md) — A 32-bit floating-point value.
- [MTLVertexFormatFloat2](float2.md) — A two-component vector with 32-bit floating-point values.
- [MTLVertexFormatFloat3](float3.md) — A three-component vector with 32-bit floating-point values.
- [MTLVertexFormatFloat4](float4.md) — A four-component vector with 32-bit floating-point values.
- [MTLVertexFormatFloatRGB9E5](floatrgb9e5.md) — A three-component vector with 9-bit floating-point values for red, green, and blue, and a 5-bit shared exponent.
