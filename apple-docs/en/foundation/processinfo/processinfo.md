---
title: processInfo
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/processinfo/processinfo
source_url: 'https://developer.apple.com/documentation/foundation/processinfo/processinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/processinfo/processinfo.json'
content_hash: 'sha256:6db132eba013dd20'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProcessInfo](../processinfo.md)

# processInfo

<sub>Type Property</sub>

Returns the process information agent for the process.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var processInfo: ProcessInfo { get }
```

## Return Value

Shared process information agent for the process.

## Discussion

An [ProcessInfo](../processinfo.md) object is created the first time this method is invoked, and that same object is returned on each subsequent invocation.
