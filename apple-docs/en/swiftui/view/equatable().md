---
title: equatable()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/view/equatable()
source_url: 'https://developer.apple.com/documentation/swiftui/view/equatable()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/equatable%28%29.json'
content_hash: 'sha256:7374b6d6d9fb4830'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# equatable()

<sub>Instance Method</sub>

Prevents the view from updating its child view when its new value is the same as its old value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func equatable() -> EquatableView<Self>
```

## See Also

### Managing the view hierarchy

- [id(_:)](<id(__).md>) — Binds a view’s identity to the given proxy value.
- [tag(_:includeOptional:)](<tag(__includeoptional_).md>) — Sets the unique tag value of this view.
