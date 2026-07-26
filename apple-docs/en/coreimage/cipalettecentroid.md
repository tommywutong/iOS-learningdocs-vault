---
title: CIPaletteCentroid
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cipalettecentroid
source_url: 'https://developer.apple.com/documentation/coreimage/cipalettecentroid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cipalettecentroid.json'
content_hash: 'sha256:23bfb5bd47825821'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIPaletteCentroid

<sub>Protocol</sub>

The properties you use to configure a palette centroid filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIPaletteCentroid : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [inputImage](cipalettecentroid/inputimage.md) — The image to use as an input image.
- [paletteImage](cipalettecentroid/paletteimage.md) — The input color palette, obtained by using a k-means clustering filter.
- [perceptual](cipalettecentroid/perceptual.md) — A Boolean value that specifies whether the filter applies the color palette in a perceptual color space.

## See Also

### Related Documentation

- [+ paletteCentroidFilter](<cifilter-swift.class/palettecentroid().md>) — Calculates the location of an image’s colors.

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
