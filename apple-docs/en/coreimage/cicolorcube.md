---
title: CIColorCube
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicolorcube
source_url: 'https://developer.apple.com/documentation/coreimage/cicolorcube'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicolorcube.json'
content_hash: 'sha256:5c545f59d7e9ec3b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIColorCube

<sub>Protocol</sub>

The properties you use to configure a color cube filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIColorCube : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [cubeData](cicolorcube/cubedata.md) — The cube texture data to use as a color lookup table.
- [cubeDimension](cicolorcube/cubedimension.md) — The length, in texels, of each side of the cube texture.
- [inputImage](cicolorcube/inputimage.md) — The image to use as an input image.
- [extrapolate](cicolorcube/extrapolate.md) — If true, then the filter extrapolates the color cube for any RGB component values outside the range 0.0 to 1.0.

## See Also

### Related Documentation

- [+ colorCubeFilter](<cifilter-swift.class/colorcube().md>) — Adjusts an image’s pixels using a three-dimensional color table.

### Protocols

- [CIColorCrossPolynomial](cicolorcrosspolynomial.md) — The properties you use to configure a color cross-polynomial filter.
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
