---
title: CISmoothLinearGradient
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cismoothlineargradient
source_url: 'https://developer.apple.com/documentation/coreimage/cismoothlineargradient'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cismoothlineargradient.json'
content_hash: 'sha256:97f1048035f1fed5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CISmoothLinearGradient

<sub>Protocol</sub>

The properties you use to configure a smooth linear gradient filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CISmoothLinearGradient : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [color0](cismoothlineargradient/color0.md) — The first color to use in the gradient.
- [color1](cismoothlineargradient/color1.md) — The second color to use in the gradient.
- [point0](cismoothlineargradient/point0.md) — The starting position of the gradient.
- [point1](cismoothlineargradient/point1.md) — The ending position of the gradient.

## See Also

### Related Documentation

- [+ smoothLinearGradientFilter](<cifilter-swift.class/smoothlineargradient().md>) — Generates a gradient that blends colors along a linear axis between two defined endpoints.

### Protocols

- [CIGaussianGradient](cigaussiangradient.md) — The properties you use to configure a Gaussian gradient filter.
- [CIHueSaturationValueGradient](cihuesaturationvaluegradient.md) — The properties you use to configure a hue-saturation-value gradient filter.
- [CILinearGradient](cilineargradient.md) — The properties you use to configure a linear gradient filter.
- [CIRadialGradient](ciradialgradient.md) — The properties you use to configure a radial gradient filter.
