---
title: CIVignette
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/civignette
source_url: 'https://developer.apple.com/documentation/coreimage/civignette'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/civignette.json'
content_hash: 'sha256:dc7a5624d203c505'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIVignette

<sub>Protocol</sub>

The properties you use to configure a vignette filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIVignette : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [inputImage](civignette/inputimage.md) — The image to use as an input image.
- [intensity](civignette/intensity.md) — The intensity of the effect.
- [radius](civignette/radius.md) — The distance from the center of the effect.

## See Also

### Related Documentation

- [+ vignetteFilter](<cifilter-swift.class/vignette().md>) — Gradually darkens an image’s edges.

### Protocols

- [CIColorCrossPolynomial](cicolorcrosspolynomial.md) — The properties you use to configure a color cross-polynomial filter.
- [CIColorCube](cicolorcube.md) — The properties you use to configure a color cube filter.
- [CIColorCubeWithColorSpace](cicolorcubewithcolorspace.md) — The properties you use to configure a color cube with color space filter.
- [CIColorCubesMixedWithMask](cicolorcubesmixedwithmask.md) — The properties you use to configure a color cube mixed with mask filter.
- [CIColorCurves](cicolorcurves.md) — The properties you use to configure a color curves filter.
- [CIColorInvert](cicolorinvert.md) — The properties you use to configure a color invert filter.
- [CIColorMap](cicolormap.md) — The properties you use to configure a color map filter.
- [CIColorMonochrome](cicolormonochrome.md) — The properties you use to configure a color monochrome filter.
- [CIConvertLab](ciconvertlab.md)
- [CIDither](cidither.md) — The properties you use to configure a dither filter.
- [CIColorPosterize](cicolorposterize.md) — The properties you use to configure a color posterize filter.
- [CIDocumentEnhancer](cidocumentenhancer.md) — The properties you use to configure a document enhancer filter.
- [CIFalseColor](cifalsecolor.md) — The properties you use to configure a false color filter.
- [CILabDeltaE](cilabdeltae.md) — The properties you use to configure a Lab Delta E filter.
- [CIMaskToAlpha](cimasktoalpha.md) — The properties you use to configure a mask-to-alpha filter.
