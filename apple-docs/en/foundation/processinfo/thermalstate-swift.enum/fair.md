---
title: ProcessInfo.ThermalState.fair
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.10.3+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/processinfo/thermalstate-swift.enum/fair
source_url: 'https://developer.apple.com/documentation/foundation/processinfo/thermalstate-swift.enum/fair'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/processinfo/thermalstate-swift.enum/fair.json'
content_hash: 'sha256:cc2c946877d4cf95'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [ProcessInfo](../../processinfo.md) · [ThermalState](../thermalstate-swift.enum.md)

# ProcessInfo.ThermalState.fair

<sub>Case</sub>

The thermal state is slightly elevated.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case fair
```

## Discussion

The system takes steps to reduce thermal state, like running fans and stopping background services that aren’t doing work immediately needed by the user.

Reduce or defer background work, like prefetching content over the network or updating database indexes.

## See Also

### Constants

- [NSProcessInfoThermalStateNominal](nominal.md) — The thermal state is within normal limits.
- [NSProcessInfoThermalStateSerious](serious.md) — The thermal state is high.
- [NSProcessInfoThermalStateCritical](critical.md) — The thermal state is significantly impacting the performance of the system and the device needs to cool down.
