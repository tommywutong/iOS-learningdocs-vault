---
title: 'isExposureModeSupported(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedevice/isexposuremodesupported(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/isexposuremodesupported(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/isexposuremodesupported%28_%3A%29.json'
content_hash: 'sha256:9e49babb26a92f07'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# isExposureModeSupported(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether a device supports the specified exposure mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func isExposureModeSupported(_ exposureMode: AVCaptureDevice.ExposureMode) -> Bool
```

## Parameters

- `exposureMode` — An exposure mode to query.

## Return Value

[true](../../swift/true.md) if `exposureMode` is supported; otherwise, [false](../../swift/false.md).

## See Also

### Managing the exposure mode

- [exposureMode](exposuremode-swift.property.md) — The exposure mode for the device.
- [ExposureMode](exposuremode-swift.enum.md) — Constants that specify the exposure mode of a capture device.
