---
title: isMultiCamSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/format/ismulticamsupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/ismulticamsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/ismulticamsupported.json'
content_hash: 'sha256:2bb3e72545a7f35d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# isMultiCamSupported

<sub>Instance Property</sub>

A Boolean value that indicates whether a multi-camera capture session supports this format.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isMultiCamSupported: Bool { get }
```

## Discussion

When performing single-camera capture using [AVCaptureSession](../../avcapturesession.md), you may set any of the device’s formats as its [activeFormat](../activeformat.md). However, when using [AVCaptureMultiCamSession](../../avcapturemulticamsession.md), you may only set the device’s format to one in which [multiCamSupported](ismulticamsupported.md) is [true](../../../swift/true.md). Only this limited subset of capture formats can run sustainably in a multi-camera capture scenario.

## See Also

### Determining video capture support

- [autoVideoFrameRateSupported](isautovideoframeratesupported.md) — A Boolean value that Indicates whether the format supports performing automatic video frame rate adjustments.
- [videoSupportedFrameRateRanges](videosupportedframerateranges.md) — A list of frame rate ranges that a format supports.
- [AVFrameRateRange](../../avframeraterange.md) — An immutable type that represents a range of valid frame rates.
- [videoBinned](isvideobinned.md) — A Boolean value that indicates whether the format produces video data in a binned format.
- [videoHDRSupported](isvideohdrsupported.md) — A Boolean value that indicates whether the format supports high dynamic range streaming.
