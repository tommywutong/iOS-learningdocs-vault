---
title: edgeIntensity
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cilineoverlay/edgeintensity
source_url: 'https://developer.apple.com/documentation/coreimage/cilineoverlay/edgeintensity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cilineoverlay/edgeintensity.json'
content_hash: 'sha256:5ef67663059f6364'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CILineOverlay](../cilineoverlay.md)

# edgeIntensity

<sub>Instance Property</sub>

The accentuation factor of the Sobel gradient information when tracing the edges of the image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var edgeIntensity: Float { get set }
```

## Discussion

Higher values find more edges, although typically, you’d use a low value (such as 1.0).

## See Also

### Instance Properties

- [NRNoiseLevel](nrnoiselevel.md) — The noise level of the image, used with camera data, that’s removed before tracing the edges of the image.
- [NRSharpness](nrsharpness.md) — The amount of sharpening done when removing noise in the image before tracing the edges of the image.
- [contrast](contrast.md) — The amount of antialiasing to use on the edges produced by this filter.
- [inputImage](inputimage.md) — The image to use as an input image.
- [threshold](threshold.md) — A value that determines edge visibility.
