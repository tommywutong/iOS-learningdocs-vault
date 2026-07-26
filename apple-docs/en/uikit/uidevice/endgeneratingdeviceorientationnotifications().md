---
title: endGeneratingDeviceOrientationNotifications()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidevice/endgeneratingdeviceorientationnotifications()
source_url: 'https://developer.apple.com/documentation/uikit/uidevice/endgeneratingdeviceorientationnotifications()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidevice/endgeneratingdeviceorientationnotifications%28%29.json'
content_hash: 'sha256:7770f4f947177488'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDevice](../uidevice.md)

# endGeneratingDeviceOrientationNotifications()

<sub>Instance Method</sub>

Ends the generation of notifications of device orientation changes.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func endGeneratingDeviceOrientationNotifications()
```

## Discussion

This method stops the posting of [UIDeviceOrientationDidChangeNotification](orientationdidchangenotification.md) notifications and notifies the system that it can power down the accelerometer hardware if it isn’t in use elsewhere. You call this method after a previous call to the [- beginGeneratingDeviceOrientationNotifications](<begingeneratingdeviceorientationnotifications().md>) method.

## See Also

### Tracking the device orientation

- [orientation](orientation.md) — The physical orientation of the device.
- [UIDeviceOrientation](../uideviceorientation.md) — Constants that describe the physical orientation of the device.
- [generatesDeviceOrientationNotifications](isgeneratingdeviceorientationnotifications.md) — A Boolean value that indicates whether the device generates orientation notifications.
- [- beginGeneratingDeviceOrientationNotifications](<begingeneratingdeviceorientationnotifications().md>) — Begins the generation of notifications of device orientation changes.
