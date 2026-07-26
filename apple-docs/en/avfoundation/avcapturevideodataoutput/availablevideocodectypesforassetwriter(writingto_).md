---
title: 'availableVideoCodecTypesForAssetWriter(writingTo:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturevideodataoutput/availablevideocodectypesforassetwriter(writingto:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/availablevideocodectypesforassetwriter(writingto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturevideodataoutput/availablevideocodectypesforassetwriter%28writingto%3A%29.json'
content_hash: 'sha256:a6dd64a616f1dcb8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureVideoDataOutput](../avcapturevideodataoutput.md)

# availableVideoCodecTypesForAssetWriter(writingTo:)

<sub>Instance Method</sub>

The video codecs that the output supports for writing video to the output file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func availableVideoCodecTypesForAssetWriter(writingTo outputFileType: AVFileType) -> [AVVideoCodecType]
```

## Parameters

- `outputFileType` — The UTI of the output file type.

## Return Value

An array of video codecs.

## See Also

### Retrieving supported video types

- [availableVideoPixelFormatTypes](availablevideopixelformattypes.md) — The video pixel formats the output supports.
- [availableVideoCodecTypes](availablevideocodectypes.md) — The video codecs that the output supports.
- [AVVideoCodecType](../avvideocodectype.md) — A set of constants that describe the codecs the system supports for video capture.
