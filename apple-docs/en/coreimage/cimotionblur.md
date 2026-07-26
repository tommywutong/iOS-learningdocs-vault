---
title: CIMotionBlur
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cimotionblur
source_url: 'https://developer.apple.com/documentation/coreimage/cimotionblur'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cimotionblur.json'
content_hash: 'sha256:1bc01eef4665ea25'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIMotionBlur

<sub>Protocol</sub>

The properties you use to configure a motion blur filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIMotionBlur : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [angle](cimotionblur/angle.md) — The angle of the motion, in radians, that determines which direction the blur smears.
- [inputImage](cimotionblur/inputimage.md) — The image to use as an input image.
- [radius](cimotionblur/radius.md) — The radius of the blur, in pixels.

## See Also

### Related Documentation

- [+ motionBlurFilter](<cifilter-swift.class/motionblur().md>) — Creates motion blur on an image.

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
- [CINoiseReduction](cinoisereduction.md) — The properties you use to configure a noise reduction filter.
- [CIZoomBlur](cizoomblur.md) — The properties you use to configure a zoom blur filter.
