---
title: inputImage
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cilineoverlay/inputimage
source_url: 'https://developer.apple.com/documentation/coreimage/cilineoverlay/inputimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cilineoverlay/inputimage.json'
content_hash: 'sha256:2216aa7b762898a2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CILineOverlay](../cilineoverlay.md)

# inputImage

<sub>Instance Property</sub>

The image to use as an input image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var inputImage: CIImage? { get set }
```

## See Also

### Instance Properties

- [NRNoiseLevel](nrnoiselevel.md) — The noise level of the image, used with camera data, that’s removed before tracing the edges of the image.
- [NRSharpness](nrsharpness.md) — The amount of sharpening done when removing noise in the image before tracing the edges of the image.
- [contrast](contrast.md) — The amount of antialiasing to use on the edges produced by this filter.
- [edgeIntensity](edgeintensity.md) — The accentuation factor of the Sobel gradient information when tracing the edges of the image.
- [threshold](threshold.md) — A value that determines edge visibility.
