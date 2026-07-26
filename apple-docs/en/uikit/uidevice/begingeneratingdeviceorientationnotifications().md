---
title: beginGeneratingDeviceOrientationNotifications()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidevice/begingeneratingdeviceorientationnotifications()
source_url: 'https://developer.apple.com/documentation/uikit/uidevice/begingeneratingdeviceorientationnotifications()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidevice/begingeneratingdeviceorientationnotifications%28%29.json'
content_hash: 'sha256:d3a3e9a4c7e72784'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDevice](../uidevice.md)

# beginGeneratingDeviceOrientationNotifications()

<sub>Instance Method</sub>

Begins the generation of notifications of device orientation changes.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func beginGeneratingDeviceOrientationNotifications()
```

## Discussion

You must call this method before attempting to get orientation data from the device. This method enables the device’s accelerometer hardware and begins the delivery of acceleration events to the device. The device subsequently uses these events to post [UIDeviceOrientationDidChangeNotification](orientationdidchangenotification.md) notifications when the device orientation changes and to update the [orientation](orientation.md) property.

You may nest calls to this method safely, but you should always match each call with a corresponding call to the [- endGeneratingDeviceOrientationNotifications](<endgeneratingdeviceorientationnotifications().md>) method.

## See Also

### Tracking the device orientation

- [orientation](orientation.md) — The physical orientation of the device.
- [UIDeviceOrientation](../uideviceorientation.md) — Constants that describe the physical orientation of the device.
- [generatesDeviceOrientationNotifications](isgeneratingdeviceorientationnotifications.md) — A Boolean value that indicates whether the device generates orientation notifications.
- [- endGeneratingDeviceOrientationNotifications](<endgeneratingdeviceorientationnotifications().md>) — Ends the generation of notifications of device orientation changes.
