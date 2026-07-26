---
title: videoFrameRateRangeForStudioLight
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/format/videoframeraterangeforstudiolight
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/videoframeraterangeforstudiolight'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/videoframeraterangeforstudiolight.json'
content_hash: 'sha256:8b6a929d000f09da'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# videoFrameRateRangeForStudioLight

<sub>Instance Property</sub>

A value that indicates the minimum and maximum frame rates available when a user enables Studio Light.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var videoFrameRateRangeForStudioLight: AVFrameRateRange? { get }
```

## Discussion

Devices may support a limited frame rate range when Studio Light is active. If the format doesn’t support Studio Light, this property is `nil`.

## See Also

### Determining Studio Light support

- [studioLightSupported](isstudiolightsupported.md) — A Boolean value that indicates whether the format supports Studio Light.
