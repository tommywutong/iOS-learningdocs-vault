---
title: tAddressMode
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlsamplerdescriptor/taddressmode
source_url: 'https://developer.apple.com/documentation/metal/mtlsamplerdescriptor/taddressmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlsamplerdescriptor/taddressmode.json'
content_hash: 'sha256:fe455cb799df19cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLSamplerDescriptor](../mtlsamplerdescriptor.md)

# tAddressMode

<sub>Instance Property</sub>

The address mode for the texture height (t) coordinate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var tAddressMode: MTLSamplerAddressMode { get set }
```

## Discussion

The default value is [MTLSamplerAddressModeClampToEdge](../mtlsampleraddressmode/clamptoedge.md).

## See Also

### Declaring addressing modes

- [rAddressMode](raddressmode.md) — The address mode for the texture depth (r) coordinate.
- [sAddressMode](saddressmode.md) — The address mode for the texture width (s) coordinate.
- [borderColor](bordercolor.md) — The border color for clamped texture values.
- [MTLSamplerAddressMode](../mtlsampleraddressmode.md) — Modes that determine the texture coordinate at each pixel when a fetch falls outside the bounds of a texture.
- [MTLSamplerBorderColor](../mtlsamplerbordercolor.md) — Values that determine the border color for clamped texture values when the sampler address mode is [MTLSamplerAddressModeClampToBorderColor](../mtlsampleraddressmode/clamptobordercolor.md).
