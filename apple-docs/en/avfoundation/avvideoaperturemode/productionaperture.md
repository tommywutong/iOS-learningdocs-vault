---
title: productionAperture
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideoaperturemode/productionaperture
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideoaperturemode/productionaperture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideoaperturemode/productionaperture.json'
content_hash: 'sha256:a5446653173b5714'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoApertureMode](../avvideoaperturemode.md)

# productionAperture

<sub>Type Property</sub>

The pixel aspect ratio will be applied.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let productionAperture: AVVideoApertureMode
```

## Discussion

The image is not cropped to the clean aperture region, but it is scaled according to the pixel aspect ratio. Use this option when you want to see all the pixels in your video, including the edges.

## See Also

### Aperture modes

- [AVVideoApertureModeCleanAperture](cleanaperture.md) — The pixel aspect ratio and clean aperture will be applied.
- [AVVideoApertureModeEncodedPixels](encodedpixels.md) — The encoded dimensions of the image description are displayed.
