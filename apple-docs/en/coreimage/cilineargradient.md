---
title: CILinearGradient
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cilineargradient
source_url: 'https://developer.apple.com/documentation/coreimage/cilineargradient'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cilineargradient.json'
content_hash: 'sha256:1697c6b1f1fe2850'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CILinearGradient

<sub>Protocol</sub>

The properties you use to configure a linear gradient filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CILinearGradient : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [color0](cilineargradient/color0.md) — The first color to use in the gradient.
- [color1](cilineargradient/color1.md) — The second color to use in the gradient.
- [point0](cilineargradient/point0.md) — The starting position of the gradient.
- [point1](cilineargradient/point1.md) — The ending position of the gradient.

## See Also

### Related Documentation

- [+ linearGradientFilter](<cifilter-swift.class/lineargradient().md>) — Generates a color gradient that varies along a linear axis between two defined endpoints.

### Protocols

- [CIGaussianGradient](cigaussiangradient.md) — The properties you use to configure a Gaussian gradient filter.
- [CIHueSaturationValueGradient](cihuesaturationvaluegradient.md) — The properties you use to configure a hue-saturation-value gradient filter.
- [CIRadialGradient](ciradialgradient.md) — The properties you use to configure a radial gradient filter.
- [CISmoothLinearGradient](cismoothlineargradient.md) — The properties you use to configure a smooth linear gradient filter.
