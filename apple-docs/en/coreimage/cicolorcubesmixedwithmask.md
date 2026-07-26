---
title: CIColorCubesMixedWithMask
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicolorcubesmixedwithmask
source_url: 'https://developer.apple.com/documentation/coreimage/cicolorcubesmixedwithmask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicolorcubesmixedwithmask.json'
content_hash: 'sha256:d85c72d297e3efee'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIColorCubesMixedWithMask

<sub>Protocol</sub>

The properties you use to configure a color cube mixed with mask filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIColorCubesMixedWithMask : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [colorSpace](cicolorcubesmixedwithmask/colorspace.md) — The working color space.
- [cube0Data](cicolorcubesmixedwithmask/cube0data.md) — The cube texture data to use as a color lookup table.
- [cube1Data](cicolorcubesmixedwithmask/cube1data.md) — The cube texture data to use as a color lookup table.
- [cubeDimension](cicolorcubesmixedwithmask/cubedimension.md) — The length, in texels, of each side of the cube texture.
- [inputImage](cicolorcubesmixedwithmask/inputimage.md) — The image to use as an input image.
- [maskImage](cicolorcubesmixedwithmask/maskimage.md) — A masking image.
- [extrapolate](cicolorcubesmixedwithmask/extrapolate.md) — If true, then the filter extrapolates the color cube for any RGB component values outside the range 0.0 to 1.0.

## See Also

### Related Documentation

- [+ colorCubesMixedWithMaskFilter](<cifilter-swift.class/colorcubesmixedwithmask().md>) — Alters an image’s pixels using a three-dimensional color tables and a mask image.

### Protocols

- [CIColorCrossPolynomial](cicolorcrosspolynomial.md) — The properties you use to configure a color cross-polynomial filter.
- [CIColorCube](cicolorcube.md) — The properties you use to configure a color cube filter.
- [CIColorCubeWithColorSpace](cicolorcubewithcolorspace.md) — The properties you use to configure a color cube with color space filter.
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
