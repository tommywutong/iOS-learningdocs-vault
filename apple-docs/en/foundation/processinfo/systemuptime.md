---
title: systemUptime
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/processinfo/systemuptime
source_url: 'https://developer.apple.com/documentation/foundation/processinfo/systemuptime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/processinfo/systemuptime.json'
content_hash: 'sha256:bb707fbb15650fa1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProcessInfo](../processinfo.md)

# systemUptime

<sub>Instance Property</sub>

The amount of time the system has been awake since the last time it was restarted.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var systemUptime: TimeInterval { get }
```

## Discussion

> [!important] Important
> This API has the potential of being misused to access device signals to try to identify the device or user, also known as fingerprinting. Regardless of whether a user gives your app permission to track, fingerprinting is not allowed. When you use this API in your app or third-party SDK (an SDK not provided by Apple), declare your usage and the reason for using the API in your app or third-party SDK’s `PrivacyInfo.xcprivacy` file. For more information, including the list of valid reasons for using the API, see [Describing use of required reason API](../../bundleresources/describing-use-of-required-reason-api.md).

## See Also

### Getting computer information

- [processorCount](processorcount.md) — The number of processing cores available on the computer.
- [activeProcessorCount](activeprocessorcount.md) — The number of active processing cores available on the computer.
- [physicalMemory](physicalmemory.md) — The amount of physical memory on the computer in bytes.
- [- isDeviceCertifiedFor:](<isdevicecertified(for_).md>) — Indicates whether the device supports the requested performance tier.
- [- hasPerformanceProfile:](<hasperformanceprofile(__).md>) — Indicates whether an app is running under a known performance profile.
