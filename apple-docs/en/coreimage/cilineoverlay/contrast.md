---
title: contrast
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cilineoverlay/contrast
source_url: 'https://developer.apple.com/documentation/coreimage/cilineoverlay/contrast'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cilineoverlay/contrast.json'
content_hash: 'sha256:62febdb1af141f15'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CILineOverlay](../cilineoverlay.md)

# contrast

<sub>Instance Property</sub>

The amount of antialiasing to use on the edges produced by this filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var contrast: Float { get set }
```

## Discussion

Higher values produce higher contrast edges, that is, they’re less antialiased.

## See Also

### Instance Properties

- [NRNoiseLevel](nrnoiselevel.md) — The noise level of the image, used with camera data, that’s removed before tracing the edges of the image.
- [NRSharpness](nrsharpness.md) — The amount of sharpening done when removing noise in the image before tracing the edges of the image.
- [edgeIntensity](edgeintensity.md) — The accentuation factor of the Sobel gradient information when tracing the edges of the image.
- [inputImage](inputimage.md) — The image to use as an input image.
- [threshold](threshold.md) — A value that determines edge visibility.
