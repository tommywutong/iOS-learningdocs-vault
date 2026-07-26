---
title: 'concat(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/viewmodifier/concat(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/viewmodifier/concat(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/viewmodifier/concat%28_%3A%29.json'
content_hash: 'sha256:8d2a7aea91cb7f51'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ViewModifier](../viewmodifier.md)

# concat(_:)

<sub>Instance Method</sub>

Returns a new modifier that is the result of concatenating `self` with `modifier`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func concat<T>(_ modifier: T) -> ModifiedContent<Self, T>
```

## See Also

### Adding animations to a view

- [animation(_:)](<animation(__).md>) — Returns a new version of the modifier that will apply `animation` to all animatable values within the modifier.
