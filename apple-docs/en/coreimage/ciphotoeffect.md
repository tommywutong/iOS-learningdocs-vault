---
title: CIPhotoEffect
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciphotoeffect
source_url: 'https://developer.apple.com/documentation/coreimage/ciphotoeffect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciphotoeffect.json'
content_hash: 'sha256:d4e9052a4a56c7bf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIPhotoEffect

<sub>Protocol</sub>

The properties you use to configure a photo-effect filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIPhotoEffect : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [inputImage](ciphotoeffect/inputimage.md) — The image to use as an input image.
- [extrapolate](ciphotoeffect/extrapolate.md) — Extrapolate for RGB values outside of the range 0.0 to 1.0.

## See Also

### Related Documentation

- [+ photoEffectChromeFilter](<cifilter-swift.class/photoeffectchrome().md>) — Exaggerates an image’s colors.
- [+ photoEffectFadeFilter](<cifilter-swift.class/photoeffectfade().md>) — Diminishes an image’s colors.
- [+ photoEffectInstantFilter](<cifilter-swift.class/photoeffectinstant().md>) — Desaturates an image’s colors.
- [+ photoEffectMonoFilter](<cifilter-swift.class/photoeffectmono().md>) — Adjust an image’s colors to black and white.
- [+ photoEffectNoirFilter](<cifilter-swift.class/photoeffectnoir().md>) — Adjusts an image’s colors to black and white and intensifies the contrast.
- [+ photoEffectProcessFilter](<cifilter-swift.class/photoeffectprocess().md>) — Lowers the contrast of the input image.
- [+ photoEffectTonalFilter](<cifilter-swift.class/photoeffecttonal().md>) — Adjusts an image’s colors to black and white.
- [+ photoEffectTransferFilter](<cifilter-swift.class/photoeffecttransfer().md>) — Brightens an image’s colors.

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
