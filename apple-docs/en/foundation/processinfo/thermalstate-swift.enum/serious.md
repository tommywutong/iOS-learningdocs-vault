---
title: ProcessInfo.ThermalState.serious
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.10.3+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/processinfo/thermalstate-swift.enum/serious
source_url: 'https://developer.apple.com/documentation/foundation/processinfo/thermalstate-swift.enum/serious'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/processinfo/thermalstate-swift.enum/serious.json'
content_hash: 'sha256:da9c0b8b9f4f78cb'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [ProcessInfo](../../processinfo.md) · [ThermalState](../thermalstate-swift.enum.md)

# ProcessInfo.ThermalState.serious

<sub>Case</sub>

The thermal state is high.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case serious
```

## Discussion

The system takes moderate steps to reduce thermal state, which reduces performance. Fans are running at maximum speed.

Reduce usage of resources that generate heat and consume battery, for example:

- Reduce or defer I/O operations, such as networking and Bluetooth
- Reduce the requested level of accuracy for location
- Reduce CPU and GPU usage by stopping or deferring work
- Reduce the target framerate from 60 FPS to 30 FPS
- Reduce the level of detail in rendered content by using fewer particles or lower-resolution textures

For more details on how to reduce your app’s use of these resources, see [Energy Efficiency Guide for iOS Apps](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/index.html#//apple_ref/doc/uid/TP40015243) and [Energy Efficiency Guide for Mac Apps](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/index.html#//apple_ref/doc/uid/TP40013929).

## See Also

### Constants

- [NSProcessInfoThermalStateNominal](nominal.md) — The thermal state is within normal limits.
- [NSProcessInfoThermalStateFair](fair.md) — The thermal state is slightly elevated.
- [NSProcessInfoThermalStateCritical](critical.md) — The thermal state is significantly impacting the performance of the system and the device needs to cool down.
