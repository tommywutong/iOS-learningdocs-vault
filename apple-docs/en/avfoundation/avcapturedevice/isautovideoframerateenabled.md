---
title: isAutoVideoFrameRateEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/isautovideoframerateenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/isautovideoframerateenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/isautovideoframerateenabled.json'
content_hash: 'sha256:88ea456ab730a917'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# isAutoVideoFrameRateEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether the capture device performs automatic video frame rate adjustments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isAutoVideoFrameRateEnabled: Bool { get set }
```

## Discussion

You can enable this property on a device when its active format’s [autoVideoFrameRateSupported](format/isautovideoframeratesupported.md) property is [true](../../swift/true.md). When enabled, a capture device automatically adjusts the active frame rate based on light level. Under low light conditions, it decreases the frame rate to properly expose the scene. For formats with a maximum frame rate of 30 fps, the frame rate switches between 30-24. For formats with a maximum frame rate of 60 fps, the frame rate switches between 60-30-24.

> [!important] Important
> After enabling automatic frame rate adjustments, attempting to set a device’s [activeVideoMinFrameDuration](activevideominframeduration.md) or [activeVideoMaxFrameDuration](activevideomaxframeduration.md) throws an exception.

Changing the device’s active format resets this property to its default value of [false](../../swift/false.md).
