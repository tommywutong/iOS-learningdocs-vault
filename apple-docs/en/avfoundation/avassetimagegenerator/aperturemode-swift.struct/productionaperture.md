---
title: productionAperture
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetimagegenerator/aperturemode-swift.struct/productionaperture
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/aperturemode-swift.struct/productionaperture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetimagegenerator/aperturemode-swift.struct/productionaperture.json'
content_hash: 'sha256:dd9ca123ea4cff3b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetImageGenerator](../../avassetimagegenerator.md) · [ApertureMode](../aperturemode-swift.struct.md)

# productionAperture

<sub>Type Property</sub>

A mode that applies only pixel aspect ratio.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let productionAperture: AVAssetImageGenerator.ApertureMode
```

## Discussion

The image isn’t cropped to the clean aperture region, but it’s scaled according to the pixel aspect ratio. Use this option when you want to see all the pixels in your video, including the edges.

## See Also

### Aperture modes

- [AVAssetImageGeneratorApertureModeCleanAperture](cleanaperture.md) — A mode that applies both pixel aspect ratio and clean aperture.
- [AVAssetImageGeneratorApertureModeEncodedPixels](encodedpixels.md) — A mode that applies neither pixel aspect ratio nor clean aperture.
