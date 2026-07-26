---
title: CIGaussianBlur
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cigaussianblur
source_url: 'https://developer.apple.com/documentation/coreimage/cigaussianblur'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cigaussianblur.json'
content_hash: 'sha256:c928db85bd065115'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIGaussianBlur

<sub>Protocol</sub>

The properties you use to configure a Gaussian blur filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIGaussianBlur : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [inputImage](cigaussianblur/inputimage.md) — The image to use as an input image.
- [radius](cigaussianblur/radius.md) — The radius of the blur, in pixels.

## See Also

### Related Documentation

- [+ gaussianBlurFilter](<cifilter-swift.class/gaussianblur().md>) — Blurs an image with a Gaussian distribution pattern.

### Protocols

- [CIBokehBlur](cibokehblur.md) — The properties you use to configure a bokeh blur filter.
- [CIBoxBlur](ciboxblur.md) — The properties you use to configure a box blur filter.
- [CIDiscBlur](cidiscblur.md) — The properties you use to configure a disc blur filter.
- [CIMaskedVariableBlur](cimaskedvariableblur.md) — The properties you use to configure a masked variable blur filter.
- [CIMedian](cimedian.md) — The properties you use to configure a median filter.
- [CIMorphologyGradient](cimorphologygradient.md) — The properties you use to configure a morphology gradient filter.
- [CIMorphologyMaximum](cimorphologymaximum.md) — The properties you use to configure a morphology maximum filter.
- [CIMorphologyMinimum](cimorphologyminimum.md) — The properties you use to configure a morphology minimum filter.
- [CIMorphologyRectangleMaximum](cimorphologyrectanglemaximum.md) — The properties you use to configure a morphology rectangle maximum filter.
- [CIMorphologyRectangleMinimum](cimorphologyrectangleminimum.md) — The properties you use to configure a morphology rectangle minimum filter.
- [CIMotionBlur](cimotionblur.md) — The properties you use to configure a motion blur filter.
- [CINoiseReduction](cinoisereduction.md) — The properties you use to configure a noise reduction filter.
- [CIZoomBlur](cizoomblur.md) — The properties you use to configure a zoom blur filter.
