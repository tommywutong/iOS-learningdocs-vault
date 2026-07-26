---
title: borderColor
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.12+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlsamplerdescriptor/bordercolor
source_url: 'https://developer.apple.com/documentation/metal/mtlsamplerdescriptor/bordercolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlsamplerdescriptor/bordercolor.json'
content_hash: 'sha256:8c1ca547b72fa28a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLSamplerDescriptor](../mtlsamplerdescriptor.md)

# borderColor

<sub>Instance Property</sub>

The border color for clamped texture values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var borderColor: MTLSamplerBorderColor { get set }
```

## Discussion

This value is only used when the sampler address mode is [MTLSamplerAddressModeClampToBorderColor](../mtlsampleraddressmode/clamptobordercolor.md).

## See Also

### Declaring addressing modes

- [rAddressMode](raddressmode.md) — The address mode for the texture depth (r) coordinate.
- [sAddressMode](saddressmode.md) — The address mode for the texture width (s) coordinate.
- [tAddressMode](taddressmode.md) — The address mode for the texture height (t) coordinate.
- [MTLSamplerAddressMode](../mtlsampleraddressmode.md) — Modes that determine the texture coordinate at each pixel when a fetch falls outside the bounds of a texture.
- [MTLSamplerBorderColor](../mtlsamplerbordercolor.md) — Values that determine the border color for clamped texture values when the sampler address mode is [MTLSamplerAddressModeClampToBorderColor](../mtlsampleraddressmode/clamptobordercolor.md).
