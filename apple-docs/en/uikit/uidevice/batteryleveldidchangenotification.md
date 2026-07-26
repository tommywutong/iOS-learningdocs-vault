---
title: batteryLevelDidChangeNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidevice/batteryleveldidchangenotification
source_url: 'https://developer.apple.com/documentation/uikit/uidevice/batteryleveldidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidevice/batteryleveldidchangenotification.json'
content_hash: 'sha256:af2bcaa62f413968'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDevice](../uidevice.md)

# batteryLevelDidChangeNotification

<sub>Type Property</sub>

A notification that posts when the battery level changes.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
nonisolated class let batteryLevelDidChangeNotification: NSNotification.Name
```

## Discussion

For this notification to be sent, you must set the [batteryMonitoringEnabled](isbatterymonitoringenabled.md) property to [true](../../swift/true.md).

Notifications for battery level change are sent no more frequently than once per minute. Don’t attempt to calculate battery drainage rate or battery time remaining; drainage rate can change frequently depending on built-in applications as well as your application.

You can obtain the battery level by getting the value of the [batteryLevel](batterylevel.md) property.

## See Also

### Managing notifications

- [UIDeviceBatteryStateDidChangeNotification](batterystatedidchangenotification.md) — A notification that posts when battery state changes.
- [UIDeviceOrientationDidChangeNotification](orientationdidchangenotification.md) — A notification that posts when the orientation of the device changes.
- [UIDeviceProximityStateDidChangeNotification](proximitystatedidchangenotification.md) — A notification that posts when the state of the proximity sensor changes.
