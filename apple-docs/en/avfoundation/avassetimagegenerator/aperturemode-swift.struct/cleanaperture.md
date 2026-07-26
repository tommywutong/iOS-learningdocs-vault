---
title: cleanAperture
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetimagegenerator/aperturemode-swift.struct/cleanaperture
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/aperturemode-swift.struct/cleanaperture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetimagegenerator/aperturemode-swift.struct/cleanaperture.json'
content_hash: 'sha256:3b51bd95ff7deafa'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetImageGenerator](../../avassetimagegenerator.md) · [ApertureMode](../aperturemode-swift.struct.md)

# cleanAperture

<sub>Type Property</sub>

A mode that applies both pixel aspect ratio and clean aperture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let cleanAperture: AVAssetImageGenerator.ApertureMode
```

## Discussion

An image’s clean aperture is a region of video free from transition artifacts caused by the encoding of the signal.

## See Also

### Aperture modes

- [AVAssetImageGeneratorApertureModeEncodedPixels](encodedpixels.md) — A mode that applies neither pixel aspect ratio nor clean aperture.
- [AVAssetImageGeneratorApertureModeProductionAperture](productionaperture.md) — A mode that applies only pixel aspect ratio.
