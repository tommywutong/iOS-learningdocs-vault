---
title: batteryStateDidChangeNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidevice/batterystatedidchangenotification
source_url: 'https://developer.apple.com/documentation/uikit/uidevice/batterystatedidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidevice/batterystatedidchangenotification.json'
content_hash: 'sha256:017fb2a7d8112f90'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDevice](../uidevice.md)

# batteryStateDidChangeNotification

<sub>Type Property</sub>

A notification that posts when battery state changes.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
nonisolated class let batteryStateDidChangeNotification: NSNotification.Name
```

## Discussion

For this notification to be sent, you must set the [batteryMonitoringEnabled](isbatterymonitoringenabled.md) property to [true](../../swift/true.md).

You can obtain the battery state by getting the value of the [batteryState](batterystate-swift.property.md) property.

## See Also

### Managing notifications

- [UIDeviceBatteryLevelDidChangeNotification](batteryleveldidchangenotification.md) — A notification that posts when the battery level changes.
- [UIDeviceOrientationDidChangeNotification](orientationdidchangenotification.md) — A notification that posts when the orientation of the device changes.
- [UIDeviceProximityStateDidChangeNotification](proximitystatedidchangenotification.md) — A notification that posts when the state of the proximity sensor changes.
