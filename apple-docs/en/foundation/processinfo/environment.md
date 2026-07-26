---
title: environment
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/processinfo/environment
source_url: 'https://developer.apple.com/documentation/foundation/processinfo/environment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/processinfo/environment.json'
content_hash: 'sha256:f990fdabf66dcbba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProcessInfo](../processinfo.md)

# environment

<sub>Instance Property</sub>

The variable names (keys) and their values in the environment from which the process was launched.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var environment: [String : String] { get }
```

## See Also

### Accessing process information

- [arguments](arguments.md) — Array of strings with the command-line arguments for the process.
- [globallyUniqueString](globallyuniquestring.md) — Global unique identifier for the process.
- [macCatalystApp](ismaccatalystapp.md) — A Boolean value that indicates whether the process originated as an iOS app and runs on macOS.
- [iOSAppOnMac](isiosapponmac.md) — A Boolean value that indicates whether the process is an iPhone or iPad app running on a Mac.
- [iOSAppOnVision](isiosapponvision.md) — A Boolean value that indicates whether the process is an iPhone or iPad app running on visionOS.
- [processIdentifier](processidentifier.md) — The identifier of the process (often called process ID).
- [processName](processname.md) — The name of the process.
