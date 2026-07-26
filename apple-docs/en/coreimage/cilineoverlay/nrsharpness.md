---
title: nrSharpness
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cilineoverlay/nrsharpness
source_url: 'https://developer.apple.com/documentation/coreimage/cilineoverlay/nrsharpness'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cilineoverlay/nrsharpness.json'
content_hash: 'sha256:e7eb80aad8cc4a8e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CILineOverlay](../cilineoverlay.md)

# nrSharpness

<sub>Instance Property</sub>

The amount of sharpening done when removing noise in the image before tracing the edges of the image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var nrSharpness: Float { get set }
```

## Discussion

This improves the edge acquisition.

## See Also

### Instance Properties

- [NRNoiseLevel](nrnoiselevel.md) — The noise level of the image, used with camera data, that’s removed before tracing the edges of the image.
- [contrast](contrast.md) — The amount of antialiasing to use on the edges produced by this filter.
- [edgeIntensity](edgeintensity.md) — The accentuation factor of the Sobel gradient information when tracing the edges of the image.
- [inputImage](inputimage.md) — The image to use as an input image.
- [threshold](threshold.md) — A value that determines edge visibility.
