---
title: thermalState
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.10.3+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/processinfo/thermalstate-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/processinfo/thermalstate-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/processinfo/thermalstate-swift.property.json'
content_hash: 'sha256:14564d47834c633f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProcessInfo](../processinfo.md)

# thermalState

<sub>Instance Property</sub>

The current thermal state of the system.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var thermalState: ProcessInfo.ThermalState { get }
```

## Discussion

At higher thermal states your app should reduce usage of system resources. For more information, see [ThermalState](thermalstate-swift.enum.md).

## See Also

### Getting the thermal state

- [ThermalState](thermalstate-swift.enum.md) — Values used to indicate the system’s thermal state.
