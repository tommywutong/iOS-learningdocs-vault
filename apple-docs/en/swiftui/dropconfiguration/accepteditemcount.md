---
title: acceptedItemCount
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/dropconfiguration/accepteditemcount
source_url: 'https://developer.apple.com/documentation/swiftui/dropconfiguration/accepteditemcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dropconfiguration/accepteditemcount.json'
content_hash: 'sha256:d02f13bbbd7f3bbc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DropConfiguration](../dropconfiguration.md)

# acceptedItemCount

<sub>Instance Property</sub>

Specifies the number of items that the drop side wants to accept.

<sub>macOS</sub>

```swift
var acceptedItemCount: Int? { get set }
```

## Discussion

Some drop destinations can accept only a limited number of dropped items. On macOS, the number is displayed as a cursor badge.
