---
title: videoSupportedFrameRateRanges
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/format/videosupportedframerateranges
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/videosupportedframerateranges'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/videosupportedframerateranges.json'
content_hash: 'sha256:829a04e40c5bfba0'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# videoSupportedFrameRateRanges

<sub>Instance Property</sub>

A list of frame rate ranges that a format supports.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var videoSupportedFrameRateRanges: [AVFrameRateRange] { get }
```

## Discussion

The value is an array of [AVFrameRateRange](../../avframeraterange.md) objects, one for each of the format’s supported video frame rate ranges.

## See Also

### Determining video capture support

- [autoVideoFrameRateSupported](isautovideoframeratesupported.md) — A Boolean value that Indicates whether the format supports performing automatic video frame rate adjustments.
- [AVFrameRateRange](../../avframeraterange.md) — An immutable type that represents a range of valid frame rates.
- [videoBinned](isvideobinned.md) — A Boolean value that indicates whether the format produces video data in a binned format.
- [videoHDRSupported](isvideohdrsupported.md) — A Boolean value that indicates whether the format supports high dynamic range streaming.
- [multiCamSupported](ismulticamsupported.md) — A Boolean value that indicates whether a multi-camera capture session supports this format.
