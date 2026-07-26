---
title: encodedPixels
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetimagegenerator/aperturemode-swift.struct/encodedpixels
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/aperturemode-swift.struct/encodedpixels'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetimagegenerator/aperturemode-swift.struct/encodedpixels.json'
content_hash: 'sha256:0a015ee885adc7b0'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetImageGenerator](../../avassetimagegenerator.md) · [ApertureMode](../aperturemode-swift.struct.md)

# encodedPixels

<sub>Type Property</sub>

A mode that applies neither pixel aspect ratio nor clean aperture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let encodedPixels: AVAssetImageGenerator.ApertureMode
```

## Discussion

The image isn’t cropped to the clean aperture region and isn’t scaled according to the pixel aspect ratio. It displays the image according to its encoded dimensions.

## See Also

### Aperture modes

- [AVAssetImageGeneratorApertureModeCleanAperture](cleanaperture.md) — A mode that applies both pixel aspect ratio and clean aperture.
- [AVAssetImageGeneratorApertureModeProductionAperture](productionaperture.md) — A mode that applies only pixel aspect ratio.
