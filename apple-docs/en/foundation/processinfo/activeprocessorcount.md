---
title: activeProcessorCount
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/processinfo/activeprocessorcount
source_url: 'https://developer.apple.com/documentation/foundation/processinfo/activeprocessorcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/processinfo/activeprocessorcount.json'
content_hash: 'sha256:fb6f5ea29c8a6fd0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProcessInfo](../processinfo.md)

# activeProcessorCount

<sub>Instance Property</sub>

The number of active processing cores available on the computer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var activeProcessorCount: Int { get }
```

## Discussion

Whereas the [processorCount](processorcount.md) property reports the number of advertised processing cores, the [activeProcessorCount](activeprocessorcount.md) property reflects the actual number of active processing cores on the system. There are a number of different factors that may cause a core to not be active, including boot arguments, thermal throttling, or a manufacturing defect.

This property value is equal to the result of entering the command `sysctl -n hw.logicalcpu` on the current system.

## See Also

### Getting computer information

- [processorCount](processorcount.md) — The number of processing cores available on the computer.
- [physicalMemory](physicalmemory.md) — The amount of physical memory on the computer in bytes.
- [- isDeviceCertifiedFor:](<isdevicecertified(for_).md>) — Indicates whether the device supports the requested performance tier.
- [- hasPerformanceProfile:](<hasperformanceprofile(__).md>) — Indicates whether an app is running under a known performance profile.
- [systemUptime](systemuptime.md) — The amount of time the system has been awake since the last time it was restarted.
