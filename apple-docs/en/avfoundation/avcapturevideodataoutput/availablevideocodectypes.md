---
title: availableVideoCodecTypes
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturevideodataoutput/availablevideocodectypes
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/availablevideocodectypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturevideodataoutput/availablevideocodectypes.json'
content_hash: 'sha256:f1442aeafc76bfb8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureVideoDataOutput](../avcapturevideodataoutput.md)

# availableVideoCodecTypes

<sub>Instance Property</sub>

The video codecs that the output supports.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var availableVideoCodecTypes: [AVVideoCodecType] { get }
```

## Discussion

The value contains an array of video codecs that the output supports. Specify the codec it uses by setting a supported value for the [AVVideoCodecKey](../avvideocodeckey.md) entry in its [videoSettings](videosettings.md) dictionary. The first format in the returned list is the most efficient output format.

## See Also

### Retrieving supported video types

- [availableVideoPixelFormatTypes](availablevideopixelformattypes.md) — The video pixel formats the output supports.
- [- availableVideoCodecTypesForAssetWriterWithOutputFileType:](<availablevideocodectypesforassetwriter(writingto_).md>) — The video codecs that the output supports for writing video to the output file.
- [AVVideoCodecType](../avvideocodectype.md) — A set of constants that describe the codecs the system supports for video capture.
