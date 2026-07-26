---
title: cleanAperture
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideoaperturemode/cleanaperture
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideoaperturemode/cleanaperture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideoaperturemode/cleanaperture.json'
content_hash: 'sha256:bf60b189048222ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoApertureMode](../avvideoaperturemode.md)

# cleanAperture

<sub>Type Property</sub>

The pixel aspect ratio and clean aperture will be applied.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let cleanAperture: AVVideoApertureMode
```

## Discussion

An image’s clean aperture is a region of video free from transition artifacts caused by the encoding of the signal.

## See Also

### Aperture modes

- [AVVideoApertureModeEncodedPixels](encodedpixels.md) — The encoded dimensions of the image description are displayed.
- [AVVideoApertureModeProductionAperture](productionaperture.md) — The pixel aspect ratio will be applied.
