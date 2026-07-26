---
title: processName
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/processinfo/processname
source_url: 'https://developer.apple.com/documentation/foundation/processinfo/processname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/processinfo/processname.json'
content_hash: 'sha256:9c88e4be345a142b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProcessInfo](../processinfo.md)

# processName

<sub>Instance Property</sub>

The name of the process.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var processName: String { get set }
```

## Discussion

The process name is used to register application defaults and is used in error messages. It does not uniquely identify the process.

> [!warning] Warning
> User defaults and other aspects of the environment might depend on the process name, so be very careful if you change it. Setting the process name in this manner is not thread safe.

## See Also

### Accessing process information

- [arguments](arguments.md) — Array of strings with the command-line arguments for the process.
- [environment](environment.md) — The variable names (keys) and their values in the environment from which the process was launched.
- [globallyUniqueString](globallyuniquestring.md) — Global unique identifier for the process.
- [macCatalystApp](ismaccatalystapp.md) — A Boolean value that indicates whether the process originated as an iOS app and runs on macOS.
- [iOSAppOnMac](isiosapponmac.md) — A Boolean value that indicates whether the process is an iPhone or iPad app running on a Mac.
- [iOSAppOnVision](isiosapponvision.md) — A Boolean value that indicates whether the process is an iPhone or iPad app running on visionOS.
- [processIdentifier](processidentifier.md) — The identifier of the process (often called process ID).
