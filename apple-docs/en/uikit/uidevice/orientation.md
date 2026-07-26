---
title: orientation
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidevice/orientation
source_url: 'https://developer.apple.com/documentation/uikit/uidevice/orientation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidevice/orientation.json'
content_hash: 'sha256:af7d643d8adbe7dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDevice](../uidevice.md)

# orientation

<sub>Instance Property</sub>

The physical orientation of the device.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var orientation: UIDeviceOrientation { get }
```

## Discussion

The value of the property is a constant that indicates the current orientation of the device. This value represents the physical orientation of the device and may be different from the current orientation of your application’s user interface. See [UIDeviceOrientation](../uideviceorientation.md) for descriptions of the possible values.

The value of this property always returns 0 unless orientation notifications have been enabled by calling [- beginGeneratingDeviceOrientationNotifications](<begingeneratingdeviceorientationnotifications().md>).

## See Also

### Tracking the device orientation

- [UIDeviceOrientation](../uideviceorientation.md) — Constants that describe the physical orientation of the device.
- [generatesDeviceOrientationNotifications](isgeneratingdeviceorientationnotifications.md) — A Boolean value that indicates whether the device generates orientation notifications.
- [- beginGeneratingDeviceOrientationNotifications](<begingeneratingdeviceorientationnotifications().md>) — Begins the generation of notifications of device orientation changes.
- [- endGeneratingDeviceOrientationNotifications](<endgeneratingdeviceorientationnotifications().md>) — Ends the generation of notifications of device orientation changes.
