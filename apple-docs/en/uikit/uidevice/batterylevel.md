---
title: batteryLevel
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidevice/batterylevel
source_url: 'https://developer.apple.com/documentation/uikit/uidevice/batterylevel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidevice/batterylevel.json'
content_hash: 'sha256:0491a4353bb9b707'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDevice](../uidevice.md)

# batteryLevel

<sub>Instance Property</sub>

The battery charge level for the device.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var batteryLevel: Float { get }
```

## Discussion

Battery level ranges from 0.0 (fully discharged) to 1.0 (100% charged). Before accessing this property, ensure that battery monitoring is enabled.

If battery monitoring is not enabled, battery state is [UIDeviceBatteryStateUnknown](batterystate-swift.enum/unknown.md) and the value of this property is –1.0.

## See Also

### Getting the device battery state

- [batteryMonitoringEnabled](isbatterymonitoringenabled.md) — A Boolean value that indicates whether battery monitoring is enabled.
- [batteryState](batterystate-swift.property.md) — The battery state for the device.
- [BatteryState](batterystate-swift.enum.md) — Constants that describe the battery power state of the device.
