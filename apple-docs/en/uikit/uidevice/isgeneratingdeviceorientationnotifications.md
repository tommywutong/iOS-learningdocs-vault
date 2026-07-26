---
title: isGeneratingDeviceOrientationNotifications
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidevice/isgeneratingdeviceorientationnotifications
source_url: 'https://developer.apple.com/documentation/uikit/uidevice/isgeneratingdeviceorientationnotifications'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidevice/isgeneratingdeviceorientationnotifications.json'
content_hash: 'sha256:aeb35582432eb484'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDevice](../uidevice.md)

# isGeneratingDeviceOrientationNotifications

<sub>Instance Property</sub>

A Boolean value that indicates whether the device generates orientation notifications.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var isGeneratingDeviceOrientationNotifications: Bool { get }
```

## Discussion

If the value of this property is [true](../../swift/true.md), the shared [UIDevice](../uidevice.md) object posts a [UIDeviceOrientationDidChangeNotification](orientationdidchangenotification.md) notification when the device changes orientation. If the value is [false](../../swift/false.md), it generates no orientation notifications. Device orientation notifications can only be generated between calls to the [- beginGeneratingDeviceOrientationNotifications](<begingeneratingdeviceorientationnotifications().md>) and [- endGeneratingDeviceOrientationNotifications](<endgeneratingdeviceorientationnotifications().md>) methods.

## See Also

### Tracking the device orientation

- [orientation](orientation.md) — The physical orientation of the device.
- [UIDeviceOrientation](../uideviceorientation.md) — Constants that describe the physical orientation of the device.
- [- beginGeneratingDeviceOrientationNotifications](<begingeneratingdeviceorientationnotifications().md>) — Begins the generation of notifications of device orientation changes.
- [- endGeneratingDeviceOrientationNotifications](<endgeneratingdeviceorientationnotifications().md>) — Ends the generation of notifications of device orientation changes.
