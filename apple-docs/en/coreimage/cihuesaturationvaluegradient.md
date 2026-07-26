---
title: CIHueSaturationValueGradient
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cihuesaturationvaluegradient
source_url: 'https://developer.apple.com/documentation/coreimage/cihuesaturationvaluegradient'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cihuesaturationvaluegradient.json'
content_hash: 'sha256:e3c97815ecfb90bd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIHueSaturationValueGradient

<sub>Protocol</sub>

The properties you use to configure a hue-saturation-value gradient filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIHueSaturationValueGradient : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [colorSpace](cihuesaturationvaluegradient/colorspace.md) — The color space for the generated color wheel.
- [dither](cihuesaturationvaluegradient/dither.md) — A Boolean value specifying whether the dither the generated output.
- [radius](cihuesaturationvaluegradient/radius.md) — The distance from the center of the effect.
- [softness](cihuesaturationvaluegradient/softness.md) — The softness of the generated color wheel.
- [value](cihuesaturationvaluegradient/value.md) — The lightness of the hue-saturation gradient.

## See Also

### Related Documentation

- [+ hueSaturationValueGradientFilter](<cifilter-swift.class/huesaturationvaluegradient().md>) — Generates a gradient representing a specified color space.

### Protocols

- [CIGaussianGradient](cigaussiangradient.md) — The properties you use to configure a Gaussian gradient filter.
- [CILinearGradient](cilineargradient.md) — The properties you use to configure a linear gradient filter.
- [CIRadialGradient](ciradialgradient.md) — The properties you use to configure a radial gradient filter.
- [CISmoothLinearGradient](cismoothlineargradient.md) — The properties you use to configure a smooth linear gradient filter.
