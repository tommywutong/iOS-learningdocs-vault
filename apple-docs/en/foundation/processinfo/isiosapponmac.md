---
title: isiOSAppOnMac
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/processinfo/isiosapponmac
source_url: 'https://developer.apple.com/documentation/foundation/processinfo/isiosapponmac'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/processinfo/isiosapponmac.json'
content_hash: 'sha256:b398a9b82e465e51'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProcessInfo](../processinfo.md)

# isiOSAppOnMac

<sub>Instance Property</sub>

A Boolean value that indicates whether the process is an iPhone or iPad app running on a Mac.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isiOSAppOnMac: Bool { get }
```

## Discussion

The value of this property is [true](../../swift/true.md) only when the process is an iOS app running on a Mac. The value of the property is [false](../../swift/false.md) for all other apps on the Mac, including Mac apps built using Mac Catalyst. The property is also [false](../../swift/false.md) for processes running on platforms other than macOS.

## See Also

### Accessing process information

- [arguments](arguments.md) — Array of strings with the command-line arguments for the process.
- [environment](environment.md) — The variable names (keys) and their values in the environment from which the process was launched.
- [globallyUniqueString](globallyuniquestring.md) — Global unique identifier for the process.
- [macCatalystApp](ismaccatalystapp.md) — A Boolean value that indicates whether the process originated as an iOS app and runs on macOS.
- [iOSAppOnVision](isiosapponvision.md) — A Boolean value that indicates whether the process is an iPhone or iPad app running on visionOS.
- [processIdentifier](processidentifier.md) — The identifier of the process (often called process ID).
- [processName](processname.md) — The name of the process.
