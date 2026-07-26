---
title: 'isDeviceCertified(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/processinfo/isdevicecertified(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/processinfo/isdevicecertified(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/processinfo/isdevicecertified%28for%3A%29.json'
content_hash: 'sha256:9146ecea728b0f25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProcessInfo](../processinfo.md)

# isDeviceCertified(for:)

<sub>Instance Method</sub>

Indicates whether the device supports the requested performance tier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func isDeviceCertified(for performanceTier: NSDeviceCertification) -> Bool
```

## Parameters

- `performanceTier` — The desired system performance tier. [iPhonePerformanceGaming](../../metal/nsdevicecertification/iphoneperformancegaming.md) is the only performance tier.

## Return Value

`True` if the device meets the requirements for the given performance tier.

## See Also

### Getting computer information

- [processorCount](processorcount.md) — The number of processing cores available on the computer.
- [activeProcessorCount](activeprocessorcount.md) — The number of active processing cores available on the computer.
- [physicalMemory](physicalmemory.md) — The amount of physical memory on the computer in bytes.
- [- hasPerformanceProfile:](<hasperformanceprofile(__).md>) — Indicates whether an app is running under a known performance profile.
- [systemUptime](systemuptime.md) — The amount of time the system has been awake since the last time it was restarted.
