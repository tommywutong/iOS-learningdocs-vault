---
title: currentWhiteBalanceGains
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/currentwhitebalancegains
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/currentwhitebalancegains'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/currentwhitebalancegains.json'
content_hash: 'sha256:d9a15071c8c4a425'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# currentWhiteBalanceGains

<sub>Type Property</sub>

A special constant representing the current white balance setting.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
class let currentWhiteBalanceGains: AVCaptureDevice.WhiteBalanceGains
```

## Discussion

Pass this value to [- setWhiteBalanceModeLockedWithDeviceWhiteBalanceGains:completionHandler:](<setwhitebalancemodelocked(with_completionhandler_).md>) to lock white balance gains to their current value (that is, disable automatic white balancing).
