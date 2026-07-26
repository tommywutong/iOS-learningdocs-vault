---
title: deviceWhiteBalanceGains
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/devicewhitebalancegains
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicewhitebalancegains'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/devicewhitebalancegains.json'
content_hash: 'sha256:10afbd66f9c86bb8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# deviceWhiteBalanceGains

<sub>Instance Property</sub>

The current device-specific RGB white balance gain values in use.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var deviceWhiteBalanceGains: AVCaptureDevice.WhiteBalanceGains { get }
```

## Discussion

This property specifies the current red, green, and blue gain values used for white balance. You can use the values to adjust color casts for a given scene. Each channel supports values between 1.0 and -[maxWhiteBalanceGain](maxwhitebalancegain.md).

This property is key-value observable.

## See Also

### Inspecting gain levels

- [grayWorldDeviceWhiteBalanceGains](grayworlddevicewhitebalancegains.md) — The current device-specific white balance values required for a neutral gray white point.
- [maxWhiteBalanceGain](maxwhitebalancegain.md) — The maximum supported value to which you can set a color channel.
