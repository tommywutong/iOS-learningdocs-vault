---
title: CIGammaAdjust
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cigammaadjust
source_url: 'https://developer.apple.com/documentation/coreimage/cigammaadjust'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cigammaadjust.json'
content_hash: 'sha256:efe70afafca39cab'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIGammaAdjust

<sub>Protocol</sub>

The properties you use to configure a gamma adjust filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIGammaAdjust : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [inputImage](cigammaadjust/inputimage.md) — The image to use as an input image.
- [power](cigammaadjust/power.md) — A gamma value to use to correct image brightness.

## See Also

### Related Documentation

- [+ gammaAdjustFilter](<cifilter-swift.class/gammaadjust().md>) — Alters an image’s transition between black and white.

### Protocols

- [CIColorAbsoluteDifference](cicolorabsolutedifference.md)
- [CIColorClamp](cicolorclamp.md) — The properties you use to configure a color clamp filter.
- [CIColorControls](cicolorcontrols.md) — The properties you use to configure a color controls filter.
- [CIColorMatrix](cicolormatrix.md) — The properties you use to configure a color matrix filter.
- [CIColorPolynomial](cicolorpolynomial.md) — The properties you use to configure a color polynomial filter.
- [CIColorThreshold](cicolorthreshold.md)
- [CIColorThresholdOtsu](cicolorthresholdotsu.md)
- [CIDepthToDisparity](cidepthtodisparity.md) — The properties you use to configure a depth-to-disparity filter.
- [CIDisparityToDepth](cidisparitytodepth.md) — The properties you use to configure a disparity-to-depth filter.
- [CIExposureAdjust](ciexposureadjust.md) — The properties you use to configure an exposure adjust filter.
- [CIHueAdjust](cihueadjust.md) — The properties you use to configure a hue adjust filter.
- [CILinearToSRGBToneCurve](cilineartosrgbtonecurve.md) — The properties you use to configure a linear-to-sRGB filter.
- [CISRGBToneCurveToLinear](cisrgbtonecurvetolinear.md) — The properties you use to configure an sRGB-to-linear filter.
- [CISystemToneMap](cisystemtonemap.md) — The protocol for the System Tone Map filter.
- [CITemperatureAndTint](citemperatureandtint.md) — The properties you use to configure a temperature and tint filter.
