---
title: CIVibrance
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/civibrance
source_url: 'https://developer.apple.com/documentation/coreimage/civibrance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/civibrance.json'
content_hash: 'sha256:801add1336e785a9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIVibrance

<sub>Protocol</sub>

The properties you use to configure a vibrance filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIVibrance : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [amount](civibrance/amount.md) — The amount to adjust the saturation by.
- [inputImage](civibrance/inputimage.md) — The image to use as an input image.

## See Also

### Related Documentation

- [+ vibranceFilter](<cifilter-swift.class/vibrance().md>) — Adjusts an image’s vibrancy.

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
- [CIGammaAdjust](cigammaadjust.md) — The properties you use to configure a gamma adjust filter.
- [CIHueAdjust](cihueadjust.md) — The properties you use to configure a hue adjust filter.
- [CILinearToSRGBToneCurve](cilineartosrgbtonecurve.md) — The properties you use to configure a linear-to-sRGB filter.
- [CISRGBToneCurveToLinear](cisrgbtonecurvetolinear.md) — The properties you use to configure an sRGB-to-linear filter.
- [CISystemToneMap](cisystemtonemap.md) — The protocol for the System Tone Map filter.
