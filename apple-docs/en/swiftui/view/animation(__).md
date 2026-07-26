---
title: 'animation(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/animation(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/animation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/animation%28_%3A%29.json'
content_hash: 'sha256:6b6dc0272d661867'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# animation(_:)

<sub>Instance Method</sub>

Applies the given animation to this view when this view changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func animation(_ animation: Animation?) -> some View

```

## Parameters

- `animation` — The animation to apply. If `animation` is `nil`, the view doesn’t animate.

## Return Value

A view that applies `animation` to this view whenever it changes.

## See Also

### Adding state-based animation to a view

- [animation(_:value:)](<animation(__value_).md>) — Applies the given animation to this view when the specified value changes.
- [animation(_:body:)](<animation(__body_).md>) — Applies the given animation to all animatable values within the `body` closure.
