---
title: orientationDidChangeNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidevice/orientationdidchangenotification
source_url: 'https://developer.apple.com/documentation/uikit/uidevice/orientationdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidevice/orientationdidchangenotification.json'
content_hash: 'sha256:5a9b47fe8d1938af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDevice](../uidevice.md)

# orientationDidChangeNotification

<sub>Type Property</sub>

A notification that posts when the orientation of the device changes.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
nonisolated class let orientationDidChangeNotification: NSNotification.Name
```

## Discussion

You can obtain the new orientation by getting the value of the [orientation](orientation.md) property.

## See Also

### Managing notifications

- [UIDeviceBatteryLevelDidChangeNotification](batteryleveldidchangenotification.md) — A notification that posts when the battery level changes.
- [UIDeviceBatteryStateDidChangeNotification](batterystatedidchangenotification.md) — A notification that posts when battery state changes.
- [UIDeviceProximityStateDidChangeNotification](proximitystatedidchangenotification.md) — A notification that posts when the state of the proximity sensor changes.
