---
title: globallyUniqueString
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/processinfo/globallyuniquestring
source_url: 'https://developer.apple.com/documentation/foundation/processinfo/globallyuniquestring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/processinfo/globallyuniquestring.json'
content_hash: 'sha256:16abbcb9972be596'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProcessInfo](../processinfo.md)

# globallyUniqueString

<sub>Instance Property</sub>

Global unique identifier for the process.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var globallyUniqueString: String { get }
```

## Discussion

The global ID for the process includes the host name, process ID, and a time stamp, which ensures that the ID is unique for the network. This property generates a new string each time its getter is invoked, and it uses a counter to guarantee that strings created from the same process are unique.

## See Also

### Accessing process information

- [arguments](arguments.md) — Array of strings with the command-line arguments for the process.
- [environment](environment.md) — The variable names (keys) and their values in the environment from which the process was launched.
- [macCatalystApp](ismaccatalystapp.md) — A Boolean value that indicates whether the process originated as an iOS app and runs on macOS.
- [iOSAppOnMac](isiosapponmac.md) — A Boolean value that indicates whether the process is an iPhone or iPad app running on a Mac.
- [iOSAppOnVision](isiosapponvision.md) — A Boolean value that indicates whether the process is an iPhone or iPad app running on visionOS.
- [processIdentifier](processidentifier.md) — The identifier of the process (often called process ID).
- [processName](processname.md) — The name of the process.
