---
title: ProcessInfo.ThermalState.critical
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.10.3+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/processinfo/thermalstate-swift.enum/critical
source_url: 'https://developer.apple.com/documentation/foundation/processinfo/thermalstate-swift.enum/critical'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/processinfo/thermalstate-swift.enum/critical.json'
content_hash: 'sha256:6c7d6b98c35dbb49'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [ProcessInfo](../../processinfo.md) · [ThermalState](../thermalstate-swift.enum.md)

# ProcessInfo.ThermalState.critical

<sub>Case</sub>

The thermal state is significantly impacting the performance of the system and the device needs to cool down.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case critical
```

## Discussion

The system takes significant steps to reduce thermal state. Fans are running at maximum speed.

Reduce usage of the CPU, GPU, and I/O such as Bluetooth or network to the minimum level required for user interaction. If possible, stop using peripherals such as the camera, flash, microphone, and speaker.

## See Also

### Constants

- [NSProcessInfoThermalStateNominal](nominal.md) — The thermal state is within normal limits.
- [NSProcessInfoThermalStateFair](fair.md) — The thermal state is slightly elevated.
- [NSProcessInfoThermalStateSerious](serious.md) — The thermal state is high.
