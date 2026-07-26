---
title: threshold
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cilineoverlay/threshold
source_url: 'https://developer.apple.com/documentation/coreimage/cilineoverlay/threshold'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cilineoverlay/threshold.json'
content_hash: 'sha256:a8449719e8bbe320'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CILineOverlay](../cilineoverlay.md)

# threshold

<sub>Instance Property</sub>

A value that determines edge visibility.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var threshold: Float { get set }
```

## Discussion

Larger values thin out the edges.

## See Also

### Instance Properties

- [NRNoiseLevel](nrnoiselevel.md) — The noise level of the image, used with camera data, that’s removed before tracing the edges of the image.
- [NRSharpness](nrsharpness.md) — The amount of sharpening done when removing noise in the image before tracing the edges of the image.
- [contrast](contrast.md) — The amount of antialiasing to use on the edges produced by this filter.
- [edgeIntensity](edgeintensity.md) — The accentuation factor of the Sobel gradient information when tracing the edges of the image.
- [inputImage](inputimage.md) — The image to use as an input image.
