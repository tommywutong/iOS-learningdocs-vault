---
title: 'combined(with:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/anytransition/combined(with:)'
source_url: 'https://developer.apple.com/documentation/swiftui/anytransition/combined(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/anytransition/combined%28with%3A%29.json'
content_hash: 'sha256:e8d8b1d921c13bb6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AnyTransition](../anytransition.md)

# combined(with:)

<sub>Instance Method</sub>

Combines this transition with another, returning a new transition that is the result of both transitions being applied.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func combined(with other: AnyTransition) -> AnyTransition
```

## See Also

### Combining and configuring transitions

- [animation(_:)](<animation(__).md>) — Attaches an animation to this transition.
- [asymmetric(insertion:removal:)](<asymmetric(insertion_removal_).md>) — Provides a composite transition that uses a different transition for insertion versus removal.
