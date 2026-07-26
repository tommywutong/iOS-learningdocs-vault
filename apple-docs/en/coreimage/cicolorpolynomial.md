---
title: CIColorPolynomial
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicolorpolynomial
source_url: 'https://developer.apple.com/documentation/coreimage/cicolorpolynomial'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicolorpolynomial.json'
content_hash: 'sha256:0783fb0e4a41a074'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIColorPolynomial

<sub>Protocol</sub>

The properties you use to configure a color polynomial filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIColorPolynomial : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [alphaCoefficients](cicolorpolynomial/alphacoefficients.md) — Polynomial coefficients for the alpha channel.
- [blueCoefficients](cicolorpolynomial/bluecoefficients.md) — Polynomial coefficients for the blue channel.
- [greenCoefficients](cicolorpolynomial/greencoefficients.md) — Polynomial coefficients for the green channel.
- [inputImage](cicolorpolynomial/inputimage.md) — The image to use as an input image.
- [redCoefficients](cicolorpolynomial/redcoefficients.md) — Polynomial coefficients for the red channel.

## See Also

### Related Documentation

- [+ colorPolynomialFilter](<cifilter-swift.class/colorpolynomial().md>) — Alters an image’s colors.

### Protocols

- [CIColorAbsoluteDifference](cicolorabsolutedifference.md)
- [CIColorClamp](cicolorclamp.md) — The properties you use to configure a color clamp filter.
- [CIColorControls](cicolorcontrols.md) — The properties you use to configure a color controls filter.
- [CIColorMatrix](cicolormatrix.md) — The properties you use to configure a color matrix filter.
- [CIColorThreshold](cicolorthreshold.md)
- [CIColorThresholdOtsu](cicolorthresholdotsu.md)
- [CIDepthToDisparity](cidepthtodisparity.md) — The properties you use to configure a depth-to-disparity filter.
- [CIDisparityToDepth](cidisparitytodepth.md) — The properties you use to configure a disparity-to-depth filter.
- [CIExposureAdjust](ciexposureadjust.md) — The properties you use to configure an exposure adjust filter.
- [CIGammaAdjust](cigammaadjust.md) — The properties you use to configure a gamma adjust filter.
- [CIHueAdjust](cihueadjust.md) — The properties you use to configure a hue adjust filter.
- [CILinearToSRGBToneCurve](cilineartosrgbtonecurve.md) — The properties you use to configure a linear-to-sRGB filter.
- [CISRGBToneCurveToLinear](cisrgbtonecurvetolinear.md) — The properties you use to configure an sRGB-to-linear filter.
- [CISystemToneMap](cisystemtonemap.md) — The protocol for the System Tone Map filter.
- [CITemperatureAndTint](citemperatureandtint.md) — The properties you use to configure a temperature and tint filter.
