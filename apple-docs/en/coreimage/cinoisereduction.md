---
title: CINoiseReduction
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cinoisereduction
source_url: 'https://developer.apple.com/documentation/coreimage/cinoisereduction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cinoisereduction.json'
content_hash: 'sha256:13897326a8df9616'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CINoiseReduction

<sub>Protocol</sub>

The properties you use to configure a noise reduction filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CINoiseReduction : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [inputImage](cinoisereduction/inputimage.md) — The image to use as an input image.
- [noiseLevel](cinoisereduction/noiselevel.md) — The amount of noise reduction.
- [sharpness](cinoisereduction/sharpness.md) — The sharpness of the final image.

## See Also

### Related Documentation

- [+ noiseReductionFilter](<cifilter-swift.class/noisereduction().md>) — Reduces noise by sharpening the edges of objects.

### Protocols

- [CIBokehBlur](cibokehblur.md) — The properties you use to configure a bokeh blur filter.
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
- [CIZoomBlur](cizoomblur.md) — The properties you use to configure a zoom blur filter.
