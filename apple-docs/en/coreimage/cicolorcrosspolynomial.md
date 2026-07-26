---
title: CIColorCrossPolynomial
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicolorcrosspolynomial
source_url: 'https://developer.apple.com/documentation/coreimage/cicolorcrosspolynomial'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicolorcrosspolynomial.json'
content_hash: 'sha256:eebfab4be0809b51'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIColorCrossPolynomial

<sub>Protocol</sub>

The properties you use to configure a color cross-polynomial filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIColorCrossPolynomial : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [blueCoefficients](cicolorcrosspolynomial/bluecoefficients.md) — Polynomial coefficients for the blue channel.
- [greenCoefficients](cicolorcrosspolynomial/greencoefficients.md) — Polynomial coefficients for the green channel.
- [inputImage](cicolorcrosspolynomial/inputimage.md) — The image to use as an input image.
- [redCoefficients](cicolorcrosspolynomial/redcoefficients.md) — Polynomial coefficients for the red channel.

## See Also

### Related Documentation

- [+ colorCrossPolynomialFilter](<cifilter-swift.class/colorcrosspolynomial().md>) — Adjusts an image’s color by applying polynomial cross-products.

### Protocols

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
- [CIMaximumComponent](cimaximumcomponent.md) — The properties you use to configure a maximum component filter.
