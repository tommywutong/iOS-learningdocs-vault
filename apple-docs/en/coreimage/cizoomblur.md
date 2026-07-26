---
title: CIZoomBlur
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cizoomblur
source_url: 'https://developer.apple.com/documentation/coreimage/cizoomblur'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cizoomblur.json'
content_hash: 'sha256:83e52416c6851f1e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIZoomBlur

<sub>Protocol</sub>

The properties you use to configure a zoom blur filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIZoomBlur : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [amount](cizoomblur/amount.md) — The zoom-in amount.
- [center](cizoomblur/center.md) — The center of the effect, as x and y coordinates.
- [inputImage](cizoomblur/inputimage.md) — The image to use as an input image.

## See Also

### Related Documentation

- [+ zoomBlurFilter](<cifilter-swift.class/zoomblur().md>) — Creates a zoom blur centered around a single point on the image.

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
- [CINoiseReduction](cinoisereduction.md) — The properties you use to configure a noise reduction filter.
