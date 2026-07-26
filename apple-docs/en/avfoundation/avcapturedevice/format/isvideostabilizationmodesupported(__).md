---
title: 'isVideoStabilizationModeSupported(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedevice/format/isvideostabilizationmodesupported(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/isvideostabilizationmodesupported(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/isvideostabilizationmodesupported%28_%3A%29.json'
content_hash: 'sha256:b4ceaab3b24142da'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# isVideoStabilizationModeSupported(_:)

<sub>Instance Method</sub>

A Boolean value that indicates whether the format supports a given video stabilization mode.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func isVideoStabilizationModeSupported(_ videoStabilizationMode: AVCaptureVideoStabilizationMode) -> Bool
```

## Parameters

- `videoStabilizationMode` — The stabilization mode to test.

## Return Value

[true](../../../swift/true.md) if video stabilization is supported; otherwise, [false](../../../swift/false.md).

## See Also

### Determining video stabilization support

- [AVCaptureVideoStabilizationMode](../../avcapturevideostabilizationmode.md) — An enumeration of video stabilization modes that capture devices and formats support.
