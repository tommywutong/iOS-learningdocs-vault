---
title: MTLSamplerBorderColor
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.12+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlsamplerbordercolor
source_url: 'https://developer.apple.com/documentation/metal/mtlsamplerbordercolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlsamplerbordercolor.json'
content_hash: 'sha256:0c81b5e70fbd00d0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLSamplerBorderColor

<sub>Enumeration</sub>

Values that determine the border color for clamped texture values when the sampler address mode is [MTLSamplerAddressModeClampToBorderColor](mtlsampleraddressmode/clamptobordercolor.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLSamplerBorderColor
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Specifying border color options

- [MTLSamplerBorderColorTransparentBlack](mtlsamplerbordercolor/transparentblack.md) — A transparent black color `(0,0,0,0)` for texture values outside the border.
- [MTLSamplerBorderColorOpaqueBlack](mtlsamplerbordercolor/opaqueblack.md) — An opaque black color `(0,0,0,1)` for texture values outside the border
- [MTLSamplerBorderColorOpaqueWhite](mtlsamplerbordercolor/opaquewhite.md) — An opaque white color `(1,1,1,1)` for texture values outside the border.

### Initializers

- [init(rawValue:)](<mtlsamplerbordercolor/init(rawvalue_).md>)

## See Also

### Declaring addressing modes

- [rAddressMode](mtlsamplerdescriptor/raddressmode.md) — The address mode for the texture depth (r) coordinate.
- [sAddressMode](mtlsamplerdescriptor/saddressmode.md) — The address mode for the texture width (s) coordinate.
- [tAddressMode](mtlsamplerdescriptor/taddressmode.md) — The address mode for the texture height (t) coordinate.
- [borderColor](mtlsamplerdescriptor/bordercolor.md) — The border color for clamped texture values.
- [MTLSamplerAddressMode](mtlsampleraddressmode.md) — Modes that determine the texture coordinate at each pixel when a fetch falls outside the bounds of a texture.
