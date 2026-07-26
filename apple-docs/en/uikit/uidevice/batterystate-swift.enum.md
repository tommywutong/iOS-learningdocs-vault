---
title: UIDevice.BatteryState
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidevice/batterystate-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uidevice/batterystate-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidevice/batterystate-swift.enum.json'
content_hash: 'sha256:d6797dee3d2a26e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDevice](../uidevice.md)

# UIDevice.BatteryState

<sub>Enumeration</sub>

Constants that describe the battery power state of the device.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum BatteryState
```

## Overview

These constants are used by the [batteryState](batterystate-swift.property.md) property.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIDeviceBatteryStateUnknown](batterystate-swift.enum/unknown.md) — The battery state for the device can’t be determined.
- [UIDeviceBatteryStateUnplugged](batterystate-swift.enum/unplugged.md) — The device isn’t plugged into power; the battery is discharging.
- [UIDeviceBatteryStateCharging](batterystate-swift.enum/charging.md) — The device is plugged into power and the battery is less than 100% charged.
- [UIDeviceBatteryStateFull](batterystate-swift.enum/full.md) — The device is plugged into power and the battery is 100% charged.

### Initializers

- [init(rawValue:)](<batterystate-swift.enum/init(rawvalue_).md>)

## See Also

### Getting the device battery state

- [batteryLevel](batterylevel.md) — The battery charge level for the device.
- [batteryMonitoringEnabled](isbatterymonitoringenabled.md) — A Boolean value that indicates whether battery monitoring is enabled.
- [batteryState](batterystate-swift.property.md) — The battery state for the device.
