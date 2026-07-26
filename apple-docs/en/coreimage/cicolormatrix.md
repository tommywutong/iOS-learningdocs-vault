---
title: CIColorMatrix
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicolormatrix
source_url: 'https://developer.apple.com/documentation/coreimage/cicolormatrix'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicolormatrix.json'
content_hash: 'sha256:adc36f505122e2ad'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIColorMatrix

<sub>Protocol</sub>

The properties you use to configure a color matrix filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIColorMatrix : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [AVector](cicolormatrix/avector.md) — The amount of alpha to multiply the source color values by.
- [BVector](cicolormatrix/bvector.md) — The amount of blue to multiply the source color values by.
- [GVector](cicolormatrix/gvector.md) — The amount of green to multiply the source color values by.
- [RVector](cicolormatrix/rvector.md) — The amount of red to multiply the source color values by.
- [biasVector](cicolormatrix/biasvector.md) — A vector that’s added to each color component.
- [inputImage](cicolormatrix/inputimage.md) — The image to use as an input image.

## See Also

### Related Documentation

- [+ colorMatrixFilter](<cifilter-swift.class/colormatrix().md>) — Alters the colors in an image based on vectors provided.

### Protocols

- [CIColorAbsoluteDifference](cicolorabsolutedifference.md)
- [CIColorClamp](cicolorclamp.md) — The properties you use to configure a color clamp filter.
- [CIColorControls](cicolorcontrols.md) — The properties you use to configure a color controls filter.
- [CIColorPolynomial](cicolorpolynomial.md) — The properties you use to configure a color polynomial filter.
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
