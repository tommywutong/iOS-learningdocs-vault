---
title: maxWhiteBalanceGain
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/maxwhitebalancegain
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/maxwhitebalancegain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/maxwhitebalancegain.json'
content_hash: 'sha256:5976a3dd74b4909b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# maxWhiteBalanceGain

<sub>Instance Property</sub>

The maximum supported value to which you can set a color channel.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var maxWhiteBalanceGain: Float { get }
```

## Discussion

This property doesn’t change for the life of the object.

## See Also

### Inspecting gain levels

- [deviceWhiteBalanceGains](devicewhitebalancegains.md) — The current device-specific RGB white balance gain values in use.
- [grayWorldDeviceWhiteBalanceGains](grayworlddevicewhitebalancegains.md) — The current device-specific white balance values required for a neutral gray white point.
