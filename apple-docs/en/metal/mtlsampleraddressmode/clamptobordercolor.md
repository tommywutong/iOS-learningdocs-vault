---
title: MTLSamplerAddressMode.clampToBorderColor
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.12+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlsampleraddressmode/clamptobordercolor
source_url: 'https://developer.apple.com/documentation/metal/mtlsampleraddressmode/clamptobordercolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlsampleraddressmode/clamptobordercolor.json'
content_hash: 'sha256:b99e0400119f389e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLSamplerAddressMode](../mtlsampleraddressmode.md)

# MTLSamplerAddressMode.clampToBorderColor

<sub>Case</sub>

An address mode that returns the sampler’s border color.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case clampToBorderColor
```

## Discussion

You can configure the sampler’s border color by setting the [borderColor](../mtlsamplerdescriptor/bordercolor.md) property in the [MTLSamplerDescriptor](../mtlsamplerdescriptor.md) instance that creates the sampler.

## See Also

### Address mode options

- [MTLSamplerAddressModeClampToEdge](clamptoedge.md) — Texture coordinates are clamped between `0.0` and `1.0`, inclusive.
- [MTLSamplerAddressModeMirrorClampToEdge](mirrorclamptoedge.md) — Between `-1.0` and `1.0`, the texture coordinates are mirrored across the axis; outside `-1.0` and `1.0`, texture coordinates are clamped.
- [MTLSamplerAddressModeRepeat](repeat.md) — Texture coordinates wrap to the other side of the texture, effectively keeping only the fractional part of the texture coordinate.
- [MTLSamplerAddressModeMirrorRepeat](mirrorrepeat.md) — Between `-1.0` and `1.0`, the texture coordinates are mirrored across the axis; outside `-1.0` and `1.0`, the image is repeated.
- [MTLSamplerAddressModeClampToZero](clamptozero.md) — Out-of-range texture coordinates return transparent zero `(0,0,0,0)` for images with an alpha channel and return opaque zero `(0,0,0,1)` for images without an alpha channel.
