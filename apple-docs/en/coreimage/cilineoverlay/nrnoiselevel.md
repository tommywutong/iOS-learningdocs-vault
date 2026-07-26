---
title: nrNoiseLevel
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cilineoverlay/nrnoiselevel
source_url: 'https://developer.apple.com/documentation/coreimage/cilineoverlay/nrnoiselevel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cilineoverlay/nrnoiselevel.json'
content_hash: 'sha256:6f267f4fa1496f6c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CILineOverlay](../cilineoverlay.md)

# nrNoiseLevel

<sub>Instance Property</sub>

The noise level of the image, used with camera data, that’s removed before tracing the edges of the image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var nrNoiseLevel: Float { get set }
```

## Discussion

Increasing the noise level helps to clean up the traced edges of the image.

## See Also

### Instance Properties

- [NRSharpness](nrsharpness.md) — The amount of sharpening done when removing noise in the image before tracing the edges of the image.
- [contrast](contrast.md) — The amount of antialiasing to use on the edges produced by this filter.
- [edgeIntensity](edgeintensity.md) — The accentuation factor of the Sobel gradient information when tracing the edges of the image.
- [inputImage](inputimage.md) — The image to use as an input image.
- [threshold](threshold.md) — A value that determines edge visibility.
