---
title: 'hasPerformanceProfile(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/processinfo/hasperformanceprofile(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/processinfo/hasperformanceprofile(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/processinfo/hasperformanceprofile%28_%3A%29.json'
content_hash: 'sha256:c2d821b15f79b07f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProcessInfo](../processinfo.md)

# hasPerformanceProfile(_:)

<sub>Instance Method</sub>

Indicates whether an app is running under a known performance profile.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func hasPerformanceProfile(_ performanceProfile: NSProcessPerformanceProfile) -> Bool
```

## Parameters

- `performanceProfile` — The desired performance profile. Choose between: [default](../../metal/nsprocessperformanceprofile/default.md) and [sustained](../../metal/nsprocessperformanceprofile/sustained.md).

## Return Value

True if the system is running under the given performance profile. If the profile isn’t [sustained](../../metal/nsprocessperformanceprofile/sustained.md), the app might cause the device to throttle under a heavy workload.

## See Also

### Getting computer information

- [processorCount](processorcount.md) — The number of processing cores available on the computer.
- [activeProcessorCount](activeprocessorcount.md) — The number of active processing cores available on the computer.
- [physicalMemory](physicalmemory.md) — The amount of physical memory on the computer in bytes.
- [- isDeviceCertifiedFor:](<isdevicecertified(for_).md>) — Indicates whether the device supports the requested performance tier.
- [systemUptime](systemuptime.md) — The amount of time the system has been awake since the last time it was restarted.
