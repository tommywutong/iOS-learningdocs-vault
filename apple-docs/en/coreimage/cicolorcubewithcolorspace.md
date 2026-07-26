---
title: CIColorCubeWithColorSpace
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicolorcubewithcolorspace
source_url: 'https://developer.apple.com/documentation/coreimage/cicolorcubewithcolorspace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicolorcubewithcolorspace.json'
content_hash: 'sha256:3763672c2c004907'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIColorCubeWithColorSpace

<sub>Protocol</sub>

The properties you use to configure a color cube with color space filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIColorCubeWithColorSpace : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [colorSpace](cicolorcubewithcolorspace/colorspace.md) — The working color space.
- [cubeData](cicolorcubewithcolorspace/cubedata.md) — The cube texture data to use as a color lookup table.
- [cubeDimension](cicolorcubewithcolorspace/cubedimension.md) — The length, in texels, of each side of the cube texture.
- [inputImage](cicolorcubewithcolorspace/inputimage.md) — The image to use as an input image.
- [extrapolate](cicolorcubewithcolorspace/extrapolate.md) — If true, then the filter extrapolates the color cube for any RGB component values outside the range 0.0 to 1.0.

## See Also

### Related Documentation

- [+ colorCubeWithColorSpaceFilter](<cifilter-swift.class/colorcubewithcolorspace().md>) — Adjusts an image’s pixels using a three-dimensional color table in specified color space.

### Protocols

- [CIColorCrossPolynomial](cicolorcrosspolynomial.md) — The properties you use to configure a color cross-polynomial filter.
- [CIColorCube](cicolorcube.md) — The properties you use to configure a color cube filter.
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
