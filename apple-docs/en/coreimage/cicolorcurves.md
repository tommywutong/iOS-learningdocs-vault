---
title: CIColorCurves
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicolorcurves
source_url: 'https://developer.apple.com/documentation/coreimage/cicolorcurves'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicolorcurves.json'
content_hash: 'sha256:9e7cf5c5948c484e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIColorCurves

<sub>Protocol</sub>

The properties you use to configure a color curves filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIColorCurves : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [colorSpace](cicolorcurves/colorspace.md) — The working color space.
- [curvesData](cicolorcurves/curvesdata.md) — Color values that determine the color curves transform.
- [curvesDomain](cicolorcurves/curvesdomain.md) — A two-element vector that defines the minimum and maximum values of the curve data.
- [inputImage](cicolorcurves/inputimage.md) — The image to use as an input image.

## See Also

### Related Documentation

- [+ colorCurvesFilter](<cifilter-swift.class/colorcurves().md>) — Adjusts an image’s color curves.

### Protocols

- [CIColorCrossPolynomial](cicolorcrosspolynomial.md) — The properties you use to configure a color cross-polynomial filter.
- [CIColorCube](cicolorcube.md) — The properties you use to configure a color cube filter.
- [CIColorCubeWithColorSpace](cicolorcubewithcolorspace.md) — The properties you use to configure a color cube with color space filter.
- [CIColorCubesMixedWithMask](cicolorcubesmixedwithmask.md) — The properties you use to configure a color cube mixed with mask filter.
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
