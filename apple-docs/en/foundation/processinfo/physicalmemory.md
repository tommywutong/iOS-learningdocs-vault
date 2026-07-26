---
title: physicalMemory
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/processinfo/physicalmemory
source_url: 'https://developer.apple.com/documentation/foundation/processinfo/physicalmemory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/processinfo/physicalmemory.json'
content_hash: 'sha256:41afe355845d16e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProcessInfo](../processinfo.md)

# physicalMemory

<sub>Instance Property</sub>

The amount of physical memory on the computer in bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var physicalMemory: UInt64 { get }
```

## See Also

### Getting computer information

- [processorCount](processorcount.md) — The number of processing cores available on the computer.
- [activeProcessorCount](activeprocessorcount.md) — The number of active processing cores available on the computer.
- [- isDeviceCertifiedFor:](<isdevicecertified(for_).md>) — Indicates whether the device supports the requested performance tier.
- [- hasPerformanceProfile:](<hasperformanceprofile(__).md>) — Indicates whether an app is running under a known performance profile.
- [systemUptime](systemuptime.md) — The amount of time the system has been awake since the last time it was restarted.
