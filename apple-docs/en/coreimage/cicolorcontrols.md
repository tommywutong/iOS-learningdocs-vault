---
title: CIColorControls
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicolorcontrols
source_url: 'https://developer.apple.com/documentation/coreimage/cicolorcontrols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicolorcontrols.json'
content_hash: 'sha256:cdd96dc639544432'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIColorControls

<sub>Protocol</sub>

The properties you use to configure a color controls filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIColorControls : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [brightness](cicolorcontrols/brightness.md) — The amount of brightness to apply.
- [contrast](cicolorcontrols/contrast.md) — The amount of contrast to apply.
- [inputImage](cicolorcontrols/inputimage.md) — The image to use as an input image.
- [saturation](cicolorcontrols/saturation.md) — The amount of saturation to apply.

## See Also

### Related Documentation

- [+ colorControlsFilter](<cifilter-swift.class/colorcontrols().md>) — Alters the brightness, contrast, and saturation of an image’s colors.

### Protocols

- [CIColorAbsoluteDifference](cicolorabsolutedifference.md)
- [CIColorClamp](cicolorclamp.md) — The properties you use to configure a color clamp filter.
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
- [CITemperatureAndTint](citemperatureandtint.md) — The properties you use to configure a temperature and tint filter.
