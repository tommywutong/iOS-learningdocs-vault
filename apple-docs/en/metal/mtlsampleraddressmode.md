---
title: MTLSamplerAddressMode
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlsampleraddressmode
source_url: 'https://developer.apple.com/documentation/metal/mtlsampleraddressmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlsampleraddressmode.json'
content_hash: 'sha256:dbaef3bfd1deef03'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLSamplerAddressMode

<sub>Enumeration</sub>

Modes that determine the texture coordinate at each pixel when a fetch falls outside the bounds of a texture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLSamplerAddressMode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Address mode options

- [MTLSamplerAddressModeClampToEdge](mtlsampleraddressmode/clamptoedge.md) — Texture coordinates are clamped between `0.0` and `1.0`, inclusive.
- [MTLSamplerAddressModeMirrorClampToEdge](mtlsampleraddressmode/mirrorclamptoedge.md) — Between `-1.0` and `1.0`, the texture coordinates are mirrored across the axis; outside `-1.0` and `1.0`, texture coordinates are clamped.
- [MTLSamplerAddressModeRepeat](mtlsampleraddressmode/repeat.md) — Texture coordinates wrap to the other side of the texture, effectively keeping only the fractional part of the texture coordinate.
- [MTLSamplerAddressModeMirrorRepeat](mtlsampleraddressmode/mirrorrepeat.md) — Between `-1.0` and `1.0`, the texture coordinates are mirrored across the axis; outside `-1.0` and `1.0`, the image is repeated.
- [MTLSamplerAddressModeClampToZero](mtlsampleraddressmode/clamptozero.md) — Out-of-range texture coordinates return transparent zero `(0,0,0,0)` for images with an alpha channel and return opaque zero `(0,0,0,1)` for images without an alpha channel.
- [MTLSamplerAddressModeClampToBorderColor](mtlsampleraddressmode/clamptobordercolor.md) — An address mode that returns the sampler’s border color.

### Initializers

- [init(rawValue:)](<mtlsampleraddressmode/init(rawvalue_).md>)

## See Also

### Declaring addressing modes

- [rAddressMode](mtlsamplerdescriptor/raddressmode.md) — The address mode for the texture depth (r) coordinate.
- [sAddressMode](mtlsamplerdescriptor/saddressmode.md) — The address mode for the texture width (s) coordinate.
- [tAddressMode](mtlsamplerdescriptor/taddressmode.md) — The address mode for the texture height (t) coordinate.
- [borderColor](mtlsamplerdescriptor/bordercolor.md) — The border color for clamped texture values.
- [MTLSamplerBorderColor](mtlsamplerbordercolor.md) — Values that determine the border color for clamped texture values when the sampler address mode is [MTLSamplerAddressModeClampToBorderColor](mtlsampleraddressmode/clamptobordercolor.md).
