---
title: isVideoHDRSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/format/isvideohdrsupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/isvideohdrsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/isvideohdrsupported.json'
content_hash: 'sha256:355372adeec27854'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# isVideoHDRSupported

<sub>Instance Property</sub>

A Boolean value that indicates whether the format supports high dynamic range streaming.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isVideoHDRSupported: Bool { get }
```

## See Also

### Determining video capture support

- [autoVideoFrameRateSupported](isautovideoframeratesupported.md) — A Boolean value that Indicates whether the format supports performing automatic video frame rate adjustments.
- [videoSupportedFrameRateRanges](videosupportedframerateranges.md) — A list of frame rate ranges that a format supports.
- [AVFrameRateRange](../../avframeraterange.md) — An immutable type that represents a range of valid frame rates.
- [videoBinned](isvideobinned.md) — A Boolean value that indicates whether the format produces video data in a binned format.
- [multiCamSupported](ismulticamsupported.md) — A Boolean value that indicates whether a multi-camera capture session supports this format.
