---
title: isBatteryMonitoringEnabled
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidevice/isbatterymonitoringenabled
source_url: 'https://developer.apple.com/documentation/uikit/uidevice/isbatterymonitoringenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidevice/isbatterymonitoringenabled.json'
content_hash: 'sha256:0ebd1e8884cc26df'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDevice](../uidevice.md)

# isBatteryMonitoringEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether battery monitoring is enabled.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var isBatteryMonitoringEnabled: Bool { get set }
```

## Discussion

Enable battery monitoring if your app needs to be notified of changes to the battery state, or if you want to check the battery charge level.

The default value of this property is [false](../../swift/false.md), which:

- Disables the posting of battery-related notifications
- Disables the ability to read battery charge level and battery state

## See Also

### Related Documentation

- [UIDeviceBatteryLevelDidChangeNotification](batteryleveldidchangenotification.md) — A notification that posts when the battery level changes.
- [UIDeviceBatteryStateDidChangeNotification](batterystatedidchangenotification.md) — A notification that posts when battery state changes.

### Getting the device battery state

- [batteryLevel](batterylevel.md) — The battery charge level for the device.
- [batteryState](batterystate-swift.property.md) — The battery state for the device.
- [BatteryState](batterystate-swift.enum.md) — Constants that describe the battery power state of the device.
