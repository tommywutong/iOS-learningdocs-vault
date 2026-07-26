---
title: CIGaussianGradient
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cigaussiangradient
source_url: 'https://developer.apple.com/documentation/coreimage/cigaussiangradient'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cigaussiangradient.json'
content_hash: 'sha256:e1ba1713b7ede05d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIGaussianGradient

<sub>Protocol</sub>

The properties you use to configure a Gaussian gradient filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIGaussianGradient : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [center](cigaussiangradient/center.md) — The center of the effect as x and y coordinates.
- [color0](cigaussiangradient/color0.md) — The first color to use in the gradient.
- [color1](cigaussiangradient/color1.md) — The second color to use in the gradient.
- [radius](cigaussiangradient/radius.md) — The radius of the Gaussian distribution.

## See Also

### Related Documentation

- [+ gaussianGradientFilter](<cifilter-swift.class/gaussiangradient().md>) — Generates a gradient that varies from one color to another using a Gaussian distribution.

### Protocols

- [CIHueSaturationValueGradient](cihuesaturationvaluegradient.md) — The properties you use to configure a hue-saturation-value gradient filter.
- [CILinearGradient](cilineargradient.md) — The properties you use to configure a linear gradient filter.
- [CIRadialGradient](ciradialgradient.md) — The properties you use to configure a radial gradient filter.
- [CISmoothLinearGradient](cismoothlineargradient.md) — The properties you use to configure a smooth linear gradient filter.
