---
title: processorCount
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/processinfo/processorcount
source_url: 'https://developer.apple.com/documentation/foundation/processinfo/processorcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/processinfo/processorcount.json'
content_hash: 'sha256:e0a783b480ff65db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProcessInfo](../processinfo.md)

# processorCount

<sub>Instance Property</sub>

The number of processing cores available on the computer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var processorCount: Int { get }
```

## Discussion

This property value is equal to the result of entering the command `sysctl -n hw.ncpu` on the current system.

## See Also

### Getting computer information

- [activeProcessorCount](activeprocessorcount.md) — The number of active processing cores available on the computer.
- [physicalMemory](physicalmemory.md) — The amount of physical memory on the computer in bytes.
- [- isDeviceCertifiedFor:](<isdevicecertified(for_).md>) — Indicates whether the device supports the requested performance tier.
- [- hasPerformanceProfile:](<hasperformanceprofile(__).md>) — Indicates whether an app is running under a known performance profile.
- [systemUptime](systemuptime.md) — The amount of time the system has been awake since the last time it was restarted.
