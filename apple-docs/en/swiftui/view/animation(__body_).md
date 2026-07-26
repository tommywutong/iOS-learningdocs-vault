---
title: 'animation(_:body:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/animation(_:body:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/animation(_:body:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/animation%28_%3Abody%3A%29.json'
content_hash: 'sha256:3a20fdb90b8c69bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# animation(_:body:)

<sub>Instance Method</sub>

Applies the given animation to all animatable values within the `body` closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func animation<V>(_ animation: Animation?, @ContentBuilder body: (PlaceholderContentView<Self>) -> V) -> some View where V : View

```

## Discussion

Any modifiers applied to the content of `body` will be applied to this view, and the `animation` will only be used on the modifiers defined in the `body`.

The following code animates the opacity changing with an easeInOut animation, while the contents of MyView are animated with the implicit transaction’s animation:

```swift
MyView(isActive: isActive)
    .animation(.easeInOut) { content in
        content.opacity(isActive ? 1.0 : 0.0)
    }
```

## See Also

### Adding state-based animation to a view

- [animation(_:)](<animation(__).md>) — Applies the given animation to this view when this view changes.
- [animation(_:value:)](<animation(__value_).md>) — Applies the given animation to this view when the specified value changes.
