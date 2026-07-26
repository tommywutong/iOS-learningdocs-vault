---
title: isLockingWhiteBalanceWithCustomDeviceGainsSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/islockingwhitebalancewithcustomdevicegainssupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/islockingwhitebalancewithcustomdevicegainssupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/islockingwhitebalancewithcustomdevicegainssupported.json'
content_hash: 'sha256:13e70dbcf7cbcff3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# isLockingWhiteBalanceWithCustomDeviceGainsSupported

<sub>Instance Property</sub>

A Boolean value that indicates whether the device supports locking white balance to specific gain values.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isLockingWhiteBalanceWithCustomDeviceGainsSupported: Bool { get }
```

## Discussion

If the value is [false](../../swift/false.md), calling the [- setWhiteBalanceModeLockedWithDeviceWhiteBalanceGains:completionHandler:](<setwhitebalancemodelocked(with_completionhandler_).md>) method with a white balance gains value other than [AVCaptureWhiteBalanceGainsCurrent](currentwhitebalancegains.md) throws an exception.

## See Also

### Setting white balance manually

- [- setWhiteBalanceModeLockedWithDeviceWhiteBalanceGains:completionHandler:](<setwhitebalancemodelocked(with_completionhandler_).md>) — Sets the white balance to locked mode with the specified white balance gains.
- [- setWhiteBalanceModeLockedWithDeviceWhiteBalanceTemperatureAndTintValues:completionHandler:](<setwhitebalancemodelocked(whitebalancetemperatureandtintvalues_handler_).md>) — Sets white balance to locked mode with explicit temperature and tint values.
