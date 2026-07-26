---
title: CIBokehBlur
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cibokehblur
source_url: 'https://developer.apple.com/documentation/coreimage/cibokehblur'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cibokehblur.json'
content_hash: 'sha256:d893de7694acd61d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIBokehBlur

<sub>Protocol</sub>

The properties you use to configure a bokeh blur filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIBokehBlur : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [inputImage](cibokehblur/inputimage.md) — The image to use as an input image.
- [radius](cibokehblur/radius.md) — The radius of the blur, in pixels.
- [ringAmount](cibokehblur/ringamount.md) — The amount of extra emphasis at the ring of the bokeh.
- [ringSize](cibokehblur/ringsize.md) — The radius of the extra emphasis at the ring of the bokeh.
- [softness](cibokehblur/softness.md) — The softness of the bokeh effect.

## See Also

### Related Documentation

- [+ bokehBlurFilter](<cifilter-swift.class/bokehblur().md>) — Applies a bokeh effect to an image.

### Protocols

- [CIBoxBlur](ciboxblur.md) — The properties you use to configure a box blur filter.
- [CIDiscBlur](cidiscblur.md) — The properties you use to configure a disc blur filter.
- [CIGaussianBlur](cigaussianblur.md) — The properties you use to configure a Gaussian blur filter.
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
