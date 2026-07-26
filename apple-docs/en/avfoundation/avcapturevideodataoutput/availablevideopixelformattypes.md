---
title: availableVideoPixelFormatTypes
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturevideodataoutput/availablevideopixelformattypes
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/availablevideopixelformattypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturevideodataoutput/availablevideopixelformattypes.json'
content_hash: 'sha256:5b6cba016efbeb05'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureVideoDataOutput](../avcapturevideodataoutput.md)

# availableVideoPixelFormatTypes

<sub>Instance Property</sub>

The video pixel formats the output supports.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
@nonobjc var availableVideoPixelFormatTypes: [OSType] { get }
```

## Discussion

This value contains an array of video formats, in unspecified order, that the output supports. You can set the format by specifying it as the [kCVPixelBufferPixelFormatTypeKey](../../corevideo/kcvpixelbufferpixelformattypekey.md) entry in the output’s [videoSettings](videosettings.md) dictionary.

> [!note] Note
> The contents of this list may change if the video capture device’s [activeFormat](../avcapturedevice/activeformat.md) value changes.

## See Also

### Retrieving supported video types

- [availableVideoCodecTypes](availablevideocodectypes.md) — The video codecs that the output supports.
- [- availableVideoCodecTypesForAssetWriterWithOutputFileType:](<availablevideocodectypesforassetwriter(writingto_).md>) — The video codecs that the output supports for writing video to the output file.
- [AVVideoCodecType](../avvideocodectype.md) — A set of constants that describe the codecs the system supports for video capture.
