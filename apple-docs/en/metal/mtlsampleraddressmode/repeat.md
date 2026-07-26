---
title: MTLSamplerAddressMode.repeat
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlsampleraddressmode/repeat
source_url: 'https://developer.apple.com/documentation/metal/mtlsampleraddressmode/repeat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlsampleraddressmode/repeat.json'
content_hash: 'sha256:dcf33061eb418f34'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLSamplerAddressMode](../mtlsampleraddressmode.md)

# MTLSamplerAddressMode.repeat

<sub>Case</sub>

Texture coordinates wrap to the other side of the texture, effectively keeping only the fractional part of the texture coordinate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case `repeat`
```

## See Also

### Address mode options

- [MTLSamplerAddressModeClampToEdge](clamptoedge.md) — Texture coordinates are clamped between `0.0` and `1.0`, inclusive.
- [MTLSamplerAddressModeMirrorClampToEdge](mirrorclamptoedge.md) — Between `-1.0` and `1.0`, the texture coordinates are mirrored across the axis; outside `-1.0` and `1.0`, texture coordinates are clamped.
- [MTLSamplerAddressModeMirrorRepeat](mirrorrepeat.md) — Between `-1.0` and `1.0`, the texture coordinates are mirrored across the axis; outside `-1.0` and `1.0`, the image is repeated.
- [MTLSamplerAddressModeClampToZero](clamptozero.md) — Out-of-range texture coordinates return transparent zero `(0,0,0,0)` for images with an alpha channel and return opaque zero `(0,0,0,1)` for images without an alpha channel.
- [MTLSamplerAddressModeClampToBorderColor](clamptobordercolor.md) — An address mode that returns the sampler’s border color.
