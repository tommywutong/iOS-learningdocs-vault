---
title: 'body(content:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/viewmodifier/body(content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/viewmodifier/body(content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/viewmodifier/body%28content%3A%29.json'
content_hash: 'sha256:81a65e238d753659'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ViewModifier](../viewmodifier.md)

# body(content:)

<sub>Instance Method</sub>

Gets the current body of the caller.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@ContentBuilder @MainActor @preconcurrency func body(content: Self.Content) -> Self.Body
```

## Discussion

`content` is a proxy for the view that will have the modifier represented by `Self` applied to it.

## Default Implementations

### ViewModifier Implementations

- [body(content:)](<body(content_)-70h6f.md>) — Gets the current body of the caller.

## See Also

### Creating a view modifier

- [Body](body.md) — The type of view representing the body.
- [Content](content.md) — The content view type passed to `body()`.
