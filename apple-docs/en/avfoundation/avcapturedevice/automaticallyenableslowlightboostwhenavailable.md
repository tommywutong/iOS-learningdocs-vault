---
title: automaticallyEnablesLowLightBoostWhenAvailable
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/automaticallyenableslowlightboostwhenavailable
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/automaticallyenableslowlightboostwhenavailable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/automaticallyenableslowlightboostwhenavailable.json'
content_hash: 'sha256:d228e193cdb8f4d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# automaticallyEnablesLowLightBoostWhenAvailable

<sub>Instance Property</sub>

A Boolean value that indicates whether the capture device automatically switches to low-light boost mode when necessary.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var automaticallyEnablesLowLightBoostWhenAvailable: Bool { get set }
```

## Discussion

The default value is [false](../../swift/false.md). When it’s [true](../../swift/true.md), the device may engage a special low-light boost mode to improve image quality. It switches, at its discretion, to a special boost mode under low light, and back to normal operation when the scene becomes sufficiently lit.

Setting a value for this property throws an exception if the value of [lowLightBoostSupported](islowlightboostsupported.md) is false.

A capture device that supports this feature may only engage boost mode for certain source formats or resolutions. The switch between normal operation and low light boost mode may drop one or more video frames.

Before changing the value of this property, you must call [- lockForConfiguration:](<lockforconfiguration().md>) to acquire exclusive access to the device’s configuration properties. Otherwise, setting the value of this property raises an exception. When you finish configuring the device, call [- unlockForConfiguration](<unlockforconfiguration().md>) to release the lock and allow other devices to configure the settings.

This property is key-value observable.

## See Also

### Configuring low light settings

- [lowLightBoostSupported](islowlightboostsupported.md) — A Boolean value that indicates whether the capture device supports boosting images in low-light conditions.
- [lowLightBoostEnabled](islowlightboostenabled.md) — A Boolean value that indicates whether the capture device’s low light boost feature is in an enabled state.
