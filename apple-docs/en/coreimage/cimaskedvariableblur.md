---
title: CIMaskedVariableBlur
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cimaskedvariableblur
source_url: 'https://developer.apple.com/documentation/coreimage/cimaskedvariableblur'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cimaskedvariableblur.json'
content_hash: 'sha256:d904b84979581420'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIMaskedVariableBlur

<sub>Protocol</sub>

The properties you use to configure a masked variable blur filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIMaskedVariableBlur : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [inputImage](cimaskedvariableblur/inputimage.md) — The image to use as an input image.
- [mask](cimaskedvariableblur/mask.md) — A grayscale mask that defines the blur amount.
- [radius](cimaskedvariableblur/radius.md) — The distance from the center of the effect.

## See Also

### Related Documentation

- [+ maskedVariableBlurFilter](<cifilter-swift.class/maskedvariableblur().md>) — Blurs a specified portion of an image.

### Protocols

- [CIBokehBlur](cibokehblur.md) — The properties you use to configure a bokeh blur filter.
- [CIBoxBlur](ciboxblur.md) — The properties you use to configure a box blur filter.
- [CIDiscBlur](cidiscblur.md) — The properties you use to configure a disc blur filter.
- [CIGaussianBlur](cigaussianblur.md) — The properties you use to configure a Gaussian blur filter.
- [CIMedian](cimedian.md) — The properties you use to configure a median filter.
- [CIMorphologyGradient](cimorphologygradient.md) — The properties you use to configure a morphology gradient filter.
- [CIMorphologyMaximum](cimorphologymaximum.md) — The properties you use to configure a morphology maximum filter.
- [CIMorphologyMinimum](cimorphologyminimum.md) — The properties you use to configure a morphology minimum filter.
- [CIMorphologyRectangleMaximum](cimorphologyrectanglemaximum.md) — The properties you use to configure a morphology rectangle maximum filter.
- [CIMorphologyRectangleMinimum](cimorphologyrectangleminimum.md) — The properties you use to configure a morphology rectangle minimum filter.
- [CIMotionBlur](cimotionblur.md) — The properties you use to configure a motion blur filter.
- [CINoiseReduction](cinoisereduction.md) — The properties you use to configure a noise reduction filter.
- [CIZoomBlur](cizoomblur.md) — The properties you use to configure a zoom blur filter.
