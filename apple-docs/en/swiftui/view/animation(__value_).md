---
title: 'animation(_:value:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/animation(_:value:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/animation(_:value:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/animation%28_%3Avalue%3A%29.json'
content_hash: 'sha256:54f676982b8705d7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# animation(_:value:)

<sub>Instance Method</sub>

Applies the given animation to this view when the specified value changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func animation<V>(_ animation: Animation?, value: V) -> some View where V : Equatable

```

## Parameters

- `animation` — The animation to apply. If `animation` is `nil`, the view doesn’t animate.

- `value` — A value to monitor for changes.

## Return Value

A view that applies `animation` to this view whenever `value` changes.

## See Also

### Adding state-based animation to a view

- [animation(_:)](<animation(__).md>) — Applies the given animation to this view when this view changes.
- [animation(_:body:)](<animation(__body_).md>) — Applies the given animation to all animatable values within the `body` closure.
