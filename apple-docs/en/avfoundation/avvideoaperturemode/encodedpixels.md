---
title: encodedPixels
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideoaperturemode/encodedpixels
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideoaperturemode/encodedpixels'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideoaperturemode/encodedpixels.json'
content_hash: 'sha256:6baa8fc6360aceb6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoApertureMode](../avvideoaperturemode.md)

# encodedPixels

<sub>Type Property</sub>

The encoded dimensions of the image description are displayed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let encodedPixels: AVVideoApertureMode
```

## Discussion

The image is not cropped to the clean aperture region and is not scaled according to the pixel aspect ratio.

## See Also

### Aperture modes

- [AVVideoApertureModeCleanAperture](cleanaperture.md) — The pixel aspect ratio and clean aperture will be applied.
- [AVVideoApertureModeProductionAperture](productionaperture.md) — The pixel aspect ratio will be applied.
