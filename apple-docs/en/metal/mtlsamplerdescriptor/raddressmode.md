---
title: rAddressMode
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlsamplerdescriptor/raddressmode
source_url: 'https://developer.apple.com/documentation/metal/mtlsamplerdescriptor/raddressmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlsamplerdescriptor/raddressmode.json'
content_hash: 'sha256:97fadaf998be4e3b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLSamplerDescriptor](../mtlsamplerdescriptor.md)

# rAddressMode

<sub>Instance Property</sub>

The address mode for the texture depth (r) coordinate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var rAddressMode: MTLSamplerAddressMode { get set }
```

## Discussion

The default value is [MTLSamplerAddressModeClampToEdge](../mtlsampleraddressmode/clamptoedge.md).

## See Also

### Related Documentation

- [Metal Shading Language Guide](https://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)

### Declaring addressing modes

- [sAddressMode](saddressmode.md) — The address mode for the texture width (s) coordinate.
- [tAddressMode](taddressmode.md) — The address mode for the texture height (t) coordinate.
- [borderColor](bordercolor.md) — The border color for clamped texture values.
- [MTLSamplerAddressMode](../mtlsampleraddressmode.md) — Modes that determine the texture coordinate at each pixel when a fetch falls outside the bounds of a texture.
- [MTLSamplerBorderColor](../mtlsamplerbordercolor.md) — Values that determine the border color for clamped texture values when the sampler address mode is [MTLSamplerAddressModeClampToBorderColor](../mtlsampleraddressmode/clamptobordercolor.md).
