---
title: grayWorldDeviceWhiteBalanceGains
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/grayworlddevicewhitebalancegains
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/grayworlddevicewhitebalancegains'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/grayworlddevicewhitebalancegains.json'
content_hash: 'sha256:a96a851af59f8c72'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# grayWorldDeviceWhiteBalanceGains

<sub>Instance Property</sub>

The current device-specific white balance values required for a neutral gray white point.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var grayWorldDeviceWhiteBalanceGains: AVCaptureDevice.WhiteBalanceGains { get }
```

## Discussion

This property specifies the current red, green, and blue gain values derived from the current scene to deliver a neutral (or gray world) white point for white balance.

Gray world values assume you’ve placed a neutral subject (for example, a gray card) in the middle of the subject area, and fills the center 50% of the frame. Apps can read these values and apply them to the device using [- setWhiteBalanceModeLockedWithDeviceWhiteBalanceGains:completionHandler:](<setwhitebalancemodelocked(with_completionhandler_).md>).

Each change supports values between `1.0` and [maxWhiteBalanceGain](maxwhitebalancegain.md). You can read the value at any time, regardless of white balance mode.

This property is key-value observable.

## See Also

### Inspecting gain levels

- [deviceWhiteBalanceGains](devicewhitebalancegains.md) — The current device-specific RGB white balance gain values in use.
- [maxWhiteBalanceGain](maxwhitebalancegain.md) — The maximum supported value to which you can set a color channel.
