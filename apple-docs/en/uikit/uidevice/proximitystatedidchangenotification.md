---
title: proximityStateDidChangeNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidevice/proximitystatedidchangenotification
source_url: 'https://developer.apple.com/documentation/uikit/uidevice/proximitystatedidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidevice/proximitystatedidchangenotification.json'
content_hash: 'sha256:d6efbaffaa6b2e2a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDevice](../uidevice.md)

# proximityStateDidChangeNotification

<sub>Type Property</sub>

A notification that posts when the state of the proximity sensor changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated class let proximityStateDidChangeNotification: NSNotification.Name
```

## Discussion

You can obtain the proximity state by getting the value of the [proximityState](proximitystate.md) property.

## See Also

### Managing notifications

- [UIDeviceBatteryLevelDidChangeNotification](batteryleveldidchangenotification.md) — A notification that posts when the battery level changes.
- [UIDeviceBatteryStateDidChangeNotification](batterystatedidchangenotification.md) — A notification that posts when battery state changes.
- [UIDeviceOrientationDidChangeNotification](orientationdidchangenotification.md) — A notification that posts when the orientation of the device changes.
