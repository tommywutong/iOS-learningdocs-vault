---
title: NSUserCancelledError
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsusercancellederror-swift.var
source_url: 'https://developer.apple.com/documentation/foundation/nsusercancellederror-swift.var'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsusercancellederror-swift.var.json'
content_hash: 'sha256:de6c38939e4c8b41'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSUserCancelledError

<sub>Global Variable</sub>

The user canceled the operation (for example, by pressing Command-period).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var NSUserCancelledError: Int { get }
```

## Discussion

This code is for errors that do not require a dialog displayed and might be candidates for special-casing.
