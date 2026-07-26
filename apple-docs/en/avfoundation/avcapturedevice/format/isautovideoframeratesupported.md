---
title: isAutoVideoFrameRateSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/format/isautovideoframeratesupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/isautovideoframeratesupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/isautovideoframeratesupported.json'
content_hash: 'sha256:aa7fb2647df476b5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# isAutoVideoFrameRateSupported

<sub>Instance Property</sub>

A Boolean value that Indicates whether the format supports performing automatic video frame rate adjustments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isAutoVideoFrameRateSupported: Bool { get }
```

## Discussion

This property determines whether you can enable a capture device’s [autoVideoFrameRateEnabled](../isautovideoframerateenabled.md) property.

## See Also

### Determining video capture support

- [videoSupportedFrameRateRanges](videosupportedframerateranges.md) — A list of frame rate ranges that a format supports.
- [AVFrameRateRange](../../avframeraterange.md) — An immutable type that represents a range of valid frame rates.
- [videoBinned](isvideobinned.md) — A Boolean value that indicates whether the format produces video data in a binned format.
- [videoHDRSupported](isvideohdrsupported.md) — A Boolean value that indicates whether the format supports high dynamic range streaming.
- [multiCamSupported](ismulticamsupported.md) — A Boolean value that indicates whether a multi-camera capture session supports this format.
