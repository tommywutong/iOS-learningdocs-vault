---
title: isiOSAppOnVision
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.1+, iPadOS 26.1+, Mac Catalyst 26.1+, macOS 26.1+, tvOS 26.1+, visionOS 26.1+, watchOS 26.1+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/processinfo/isiosapponvision
source_url: 'https://developer.apple.com/documentation/foundation/processinfo/isiosapponvision'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/processinfo/isiosapponvision.json'
content_hash: 'sha256:a657638c9058f050'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProcessInfo](../processinfo.md)

# isiOSAppOnVision

<sub>Instance Property</sub>

A Boolean value that indicates whether the process is an iPhone or iPad app running on visionOS.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isiOSAppOnVision: Bool { get }
```

## Discussion

The value of this property is [true](../../swift/true.md) only when the process is an iOS app running on a visionOS device. The value of the property is [false](../../swift/false.md) for all other apps on visionOS. The property is also [false](../../swift/false.md) for processes running on platforms other than visonOS.

## See Also

### Accessing process information

- [arguments](arguments.md) — Array of strings with the command-line arguments for the process.
- [environment](environment.md) — The variable names (keys) and their values in the environment from which the process was launched.
- [globallyUniqueString](globallyuniquestring.md) — Global unique identifier for the process.
- [macCatalystApp](ismaccatalystapp.md) — A Boolean value that indicates whether the process originated as an iOS app and runs on macOS.
- [iOSAppOnMac](isiosapponmac.md) — A Boolean value that indicates whether the process is an iPhone or iPad app running on a Mac.
- [processIdentifier](processidentifier.md) — The identifier of the process (often called process ID).
- [processName](processname.md) — The name of the process.
