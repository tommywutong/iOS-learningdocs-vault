---
title: 'isWhiteBalanceModeSupported(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedevice/iswhitebalancemodesupported(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/iswhitebalancemodesupported(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/iswhitebalancemodesupported%28_%3A%29.json'
content_hash: 'sha256:510ddeb67578e5a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# isWhiteBalanceModeSupported(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the device supports the specified white balance mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func isWhiteBalanceModeSupported(_ whiteBalanceMode: AVCaptureDevice.WhiteBalanceMode) -> Bool
```

## Parameters

- `whiteBalanceMode` — A white balance mode to use.

## Return Value

[true](../../swift/true.md) if the device supports the white balance mode; otherwise, [false](../../swift/false.md).

## See Also

### Configuring automatic white balance

- [whiteBalanceMode](whitebalancemode-swift.property.md) — The current white balance mode.
- [WhiteBalanceMode](whitebalancemode-swift.enum.md) — Constants to specify the white balance mode of a capture device.
