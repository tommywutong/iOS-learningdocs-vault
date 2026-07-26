---
title: NSProcessInfoPowerStateDidChange
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 12.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/nsprocessinfopowerstatedidchange
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nsprocessinfopowerstatedidchange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/nsprocessinfopowerstatedidchange.json'
content_hash: 'sha256:d29a5484bffe7805'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# NSProcessInfoPowerStateDidChange

<sub>Type Property</sub>

Posts when the power state of a device changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let NSProcessInfoPowerStateDidChange: NSNotification.Name
```

## Discussion

After your observer receives this notification, query the [lowPowerModeEnabled](../../processinfo/islowpowermodeenabled.md) property to determine the current power state of the device. If Low Power Mode is active, take appropriate steps to reduce activity in your app. Otherwise, your app can resume normal operations.

The notification object is a [ProcessInfo](../../processinfo.md) instance.

## See Also

### Related Documentation

- [- addObserver:selector:name:object:](<../../notificationcenter/addobserver(__selector_name_object_).md>) — Adds an entry to the notification center to call the provided selector with the notification.
- [lowPowerModeEnabled](../../processinfo/islowpowermodeenabled.md) — A Boolean value that indicates the current state of Low Power Mode.
- [NotificationCenter](../../notificationcenter.md) — A notification dispatch mechanism that enables the broadcast of information to registered observers.

### Working with notifications

- [NSProcessInfoThermalStateDidChangeNotification](../../processinfo/thermalstatedidchangenotification.md) — Posts when the thermal state of the system changes.
