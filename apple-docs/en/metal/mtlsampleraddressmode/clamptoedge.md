---
title: MTLSamplerAddressMode.clampToEdge
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlsampleraddressmode/clamptoedge
source_url: 'https://developer.apple.com/documentation/metal/mtlsampleraddressmode/clamptoedge'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlsampleraddressmode/clamptoedge.json'
content_hash: 'sha256:4d20b5a09667cc55'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLSamplerAddressMode](../mtlsampleraddressmode.md)

# MTLSamplerAddressMode.clampToEdge

<sub>Case</sub>

Texture coordinates are clamped between `0.0` and `1.0`, inclusive.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case clampToEdge
```

## See Also

### Address mode options

- [MTLSamplerAddressModeMirrorClampToEdge](mirrorclamptoedge.md) — Between `-1.0` and `1.0`, the texture coordinates are mirrored across the axis; outside `-1.0` and `1.0`, texture coordinates are clamped.
- [MTLSamplerAddressModeRepeat](repeat.md) — Texture coordinates wrap to the other side of the texture, effectively keeping only the fractional part of the texture coordinate.
- [MTLSamplerAddressModeMirrorRepeat](mirrorrepeat.md) — Between `-1.0` and `1.0`, the texture coordinates are mirrored across the axis; outside `-1.0` and `1.0`, the image is repeated.
- [MTLSamplerAddressModeClampToZero](clamptozero.md) — Out-of-range texture coordinates return transparent zero `(0,0,0,0)` for images with an alpha channel and return opaque zero `(0,0,0,1)` for images without an alpha channel.
- [MTLSamplerAddressModeClampToBorderColor](clamptobordercolor.md) — An address mode that returns the sampler’s border color.
