---
title: isLowPowerModeEnabled
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 12.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/processinfo/islowpowermodeenabled
source_url: 'https://developer.apple.com/documentation/foundation/processinfo/islowpowermodeenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/processinfo/islowpowermodeenabled.json'
content_hash: 'sha256:bf2a837d6f31df3c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProcessInfo](../processinfo.md)

# isLowPowerModeEnabled

<sub>Instance Property</sub>

A Boolean value that indicates the current state of Low Power Mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isLowPowerModeEnabled: Bool { get }
```

## Discussion

Users who wish to prolong their device’s battery life can enable Low Power Mode under Settings \> Battery. In Low Power Mode, the system conserves battery life by enacting certain energy-saving measures, such as:

- Reducing CPU and GPU performance.
- Reducing screen brightness.
- Pausing discretionary and background activities.

Your app can query the [lowPowerModeEnabled](islowpowermodeenabled.md) property at any time to determine whether Low Power Mode is active.

Your app can also register to receive notifications when the Low Power Mode state of a device changes. To register for power state notifications, send the message [- addObserver:selector:name:object:](<../notificationcenter/addobserver(__selector_name_object_).md>) to the default notification center of your app (an instance of [NotificationCenter](../notificationcenter.md)). Pass it a selector to call and a notification name of [NSProcessInfoPowerStateDidChangeNotification](../nsnotification/name-swift.struct/nsprocessinfopowerstatedidchange.md). When your app receives a notification of a power state change, query [lowPowerModeEnabled](islowpowermodeenabled.md) to determine the current power state. If Low Power Mode is active, take appropriate steps to reduce activity in your app. Otherwise, your app can resume normal operations.

For additional information, see [React to Low Power Mode on iPhones](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/LowPowerMode.html#//apple_ref/doc/uid/TP40015243-CH31) in [Energy Efficiency Guide for iOS Apps](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/index.html#//apple_ref/doc/uid/TP40015243).

## See Also

### Related Documentation

- [NSProcessInfoPowerStateDidChangeNotification](../nsnotification/name-swift.struct/nsprocessinfopowerstatedidchange.md) — Posts when the power state of a device changes.
- [- addObserver:selector:name:object:](<../notificationcenter/addobserver(__selector_name_object_).md>) — Adds an entry to the notification center to call the provided selector with the notification.
- [NotificationCenter](../notificationcenter.md) — A notification dispatch mechanism that enables the broadcast of information to registered observers.
