---
title: allowsSelection
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/textselectability/allowsselection
source_url: 'https://developer.apple.com/documentation/swiftui/textselectability/allowsselection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/textselectability/allowsselection.json'
content_hash: 'sha256:180772ba6b802d83'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TextSelectability](../textselectability.md)

# allowsSelection

<sub>Type Property</sub>

A Boolean value that indicates whether the selectability type allows selection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static var allowsSelection: Bool { get }
```

## Discussion

Conforming types, such as [EnabledTextSelectability](../enabledtextselectability.md) and [DisabledTextSelectability](../disabledtextselectability.md), return `true` or `false` for this property as appropriate. SwiftUI expects this value for a given selectability type to be constant, unaffected by global state.
