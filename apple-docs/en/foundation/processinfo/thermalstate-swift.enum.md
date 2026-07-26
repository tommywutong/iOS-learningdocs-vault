---
title: ProcessInfo.ThermalState
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.10.3+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/processinfo/thermalstate-swift.enum
source_url: 'https://developer.apple.com/documentation/foundation/processinfo/thermalstate-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/processinfo/thermalstate-swift.enum.json'
content_hash: 'sha256:da97bb091a1a09a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProcessInfo](../processinfo.md)

# ProcessInfo.ThermalState

<sub>Enumeration</sub>

Values used to indicate the system’s thermal state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum ThermalState
```

## Overview

These values are used by the [ProcessInfo](../processinfo.md) class as return values for [thermalState](thermalstate-swift.property.md).

For information about testing your app under different thermal states, see [Test under adverse device conditions](https://help.apple.com/xcode/mac/current/#/dev308429d42).

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [NSProcessInfoThermalStateNominal](thermalstate-swift.enum/nominal.md) — The thermal state is within normal limits.
- [NSProcessInfoThermalStateFair](thermalstate-swift.enum/fair.md) — The thermal state is slightly elevated.
- [NSProcessInfoThermalStateSerious](thermalstate-swift.enum/serious.md) — The thermal state is high.
- [NSProcessInfoThermalStateCritical](thermalstate-swift.enum/critical.md) — The thermal state is significantly impacting the performance of the system and the device needs to cool down.

### Initializers

- [init(rawValue:)](<thermalstate-swift.enum/init(rawvalue_).md>)

## See Also

### Getting the thermal state

- [thermalState](thermalstate-swift.property.md) — The current thermal state of the system.
