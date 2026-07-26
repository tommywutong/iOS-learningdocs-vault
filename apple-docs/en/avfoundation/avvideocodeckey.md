---
title: AVVideoCodecKey
framework: AVFoundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocodeckey
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocodeckey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocodeckey.json'
content_hash: 'sha256:4fec53f43601364f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVVideoCodecKey

<sub>Global Variable</sub>

A key to access the name of the codec for compressing video.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let AVVideoCodecKey: String
```

## Discussion

The value for this key is an instance of [NSString](../foundation/nsstring.md), equivalent to [CMVideoCodecType](../coremedia/cmvideocodectype.md). Use this key to set the video compression format to H.264, HEVC, or JPEG, depending on the video codec types available in [AVCaptureMovieFileOutput](avcapturemoviefileoutput.md). Check available video codec types by consulting [availableVideoCodecTypes](avcapturemoviefileoutput/availablevideocodectypes.md).

## See Also

### Video codecs

- [AVVideoCodecType](avvideocodectype.md) — A set of constants that describe the codecs the system supports for video capture.
