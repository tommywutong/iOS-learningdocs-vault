---
title: isVideoBinned
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/format/isvideobinned
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/isvideobinned'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/isvideobinned.json'
content_hash: 'sha256:75662702b0e0662a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# isVideoBinned

<sub>Instance Property</sub>

A Boolean value that indicates whether the format produces video data in a binned format.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isVideoBinned: Bool { get }
```

## Discussion

Binning is a pixel-combining process which can result in greater low light sensitivity at the cost of reduced resolution.

## See Also

### Determining video capture support

- [autoVideoFrameRateSupported](isautovideoframeratesupported.md) — A Boolean value that Indicates whether the format supports performing automatic video frame rate adjustments.
- [videoSupportedFrameRateRanges](videosupportedframerateranges.md) — A list of frame rate ranges that a format supports.
- [AVFrameRateRange](../../avframeraterange.md) — An immutable type that represents a range of valid frame rates.
- [videoHDRSupported](isvideohdrsupported.md) — A Boolean value that indicates whether the format supports high dynamic range streaming.
- [multiCamSupported](ismulticamsupported.md) — A Boolean value that indicates whether a multi-camera capture session supports this format.
