---
title: 'animation(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/viewmodifier/animation(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/viewmodifier/animation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/viewmodifier/animation%28_%3A%29.json'
content_hash: 'sha256:88d421d3073c9664'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ViewModifier](../viewmodifier.md)

# animation(_:)

<sub>Instance Method</sub>

Returns a new version of the modifier that will apply `animation` to all animatable values within the modifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency func animation(_ animation: Animation?) -> some ViewModifier

```

## See Also

### Adding animations to a view

- [concat(_:)](<concat(__).md>) — Returns a new modifier that is the result of concatenating `self` with `modifier`.
