---
title: batteryState
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidevice/batterystate-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uidevice/batterystate-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidevice/batterystate-swift.property.json'
content_hash: 'sha256:1fc60c069f5ecd99'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDevice](../uidevice.md)

# batteryState

<sub>Instance Property</sub>

The battery state for the device.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var batteryState: UIDevice.BatteryState { get }
```

## Discussion

The value for [batteryState](batterystate-swift.property.md) is one of the constants in [BatteryState](batterystate-swift.enum.md).

If battery monitoring is not enabled, the value of this property is [UIDeviceBatteryStateUnknown](batterystate-swift.enum/unknown.md).

## See Also

### Getting the device battery state

- [batteryLevel](batterylevel.md) — The battery charge level for the device.
- [batteryMonitoringEnabled](isbatterymonitoringenabled.md) — A Boolean value that indicates whether battery monitoring is enabled.
- [BatteryState](batterystate-swift.enum.md) — Constants that describe the battery power state of the device.
