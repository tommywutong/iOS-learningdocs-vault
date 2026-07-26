---
title: 'asymmetric(insertion:removal:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/anytransition/asymmetric(insertion:removal:)'
source_url: 'https://developer.apple.com/documentation/swiftui/anytransition/asymmetric(insertion:removal:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/anytransition/asymmetric%28insertion%3Aremoval%3A%29.json'
content_hash: 'sha256:7a4e0dcd8ff8b25d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AnyTransition](../anytransition.md)

# asymmetric(insertion:removal:)

<sub>Type Method</sub>

Provides a composite transition that uses a different transition for insertion versus removal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func asymmetric(insertion: AnyTransition, removal: AnyTransition) -> AnyTransition
```

## See Also

### Combining and configuring transitions

- [animation(_:)](<animation(__).md>) — Attaches an animation to this transition.
- [combined(with:)](<combined(with_).md>) — Combines this transition with another, returning a new transition that is the result of both transitions being applied.
