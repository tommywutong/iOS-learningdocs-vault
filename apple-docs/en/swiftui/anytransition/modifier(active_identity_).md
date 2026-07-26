---
title: 'modifier(active:identity:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/anytransition/modifier(active:identity:)'
source_url: 'https://developer.apple.com/documentation/swiftui/anytransition/modifier(active:identity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/anytransition/modifier%28active%3Aidentity%3A%29.json'
content_hash: 'sha256:8bcc7cc58f455219'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AnyTransition](../anytransition.md)

# modifier(active:identity:)

<sub>Type Method</sub>

Returns a transition defined between an active modifier and an identity modifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func modifier<E>(active: E, identity: E) -> AnyTransition where E : ViewModifier
```

## See Also

### Creating a custom transition

- [init(_:)](<init(__).md>) — Create an instance that type-erases `transition`.
