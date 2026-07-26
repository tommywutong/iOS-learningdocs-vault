---
title: CIRadialGradient
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciradialgradient
source_url: 'https://developer.apple.com/documentation/coreimage/ciradialgradient'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciradialgradient.json'
content_hash: 'sha256:200603aa4751388e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIRadialGradient

<sub>Protocol</sub>

The properties you use to configure a radial gradient filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIRadialGradient : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [center](ciradialgradient/center.md) — The center of the effect as x and y coordinates.
- [color0](ciradialgradient/color0.md) — The first color to use in the gradient.
- [color1](ciradialgradient/color1.md) — The second color to use in the gradient.
- [radius0](ciradialgradient/radius0.md) — The radius of the starting circle to use in the gradient.
- [radius1](ciradialgradient/radius1.md) — The radius of the ending circle to use in the gradient.

## See Also

### Related Documentation

- [+ radialGradientFilter](<cifilter-swift.class/radialgradient().md>) — Generates a gradient that varies radially between two circles having the same center.

### Protocols

- [CIGaussianGradient](cigaussiangradient.md) — The properties you use to configure a Gaussian gradient filter.
- [CIHueSaturationValueGradient](cihuesaturationvaluegradient.md) — The properties you use to configure a hue-saturation-value gradient filter.
- [CILinearGradient](cilineargradient.md) — The properties you use to configure a linear gradient filter.
- [CISmoothLinearGradient](cismoothlineargradient.md) — The properties you use to configure a smooth linear gradient filter.
