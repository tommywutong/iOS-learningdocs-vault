---
title: 'init(_:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/anytransition/init(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/anytransition/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/anytransition/init%28_%3A%29.json'
content_hash: 'sha256:4fbe127516e70621'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AnyTransition](../anytransition.md)

# init(_:)

<sub>Initializer</sub>

Create an instance that type-erases `transition`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<T>(_ transition: T) where T : Transition
```

## See Also

### Creating a custom transition

- [modifier(active:identity:)](<modifier(active_identity_).md>) — Returns a transition defined between an active modifier and an identity modifier.
