---
title: 'onEnded(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/gesture/onended(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/gesture/onended(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/gesture/onended%28_%3A%29.json'
content_hash: 'sha256:b4565f8c2c280183'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Gesture](../gesture.md)

# onEnded(_:)

<sub>Instance Method</sub>

Adds an action to perform when the gesture ends.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func onEnded(_ action: @escaping (Self.Value) -> Void) -> _EndedGesture<Self>
```

## Parameters

- `action` — The action to perform when this gesture ends. The `action` closure’s parameter contains the final value of the gesture.

## Return Value

A gesture that triggers `action` when the gesture ends.

## Discussion

> [!important] Important
> The action is only performed if the gesture ends successfully. Use a `@GestureState` property to track state that is reset regardless of how the gesture ends.

## See Also

### Performing the gesture

- [updating(_:body:)](<updating(__body_).md>) — Updates the provided gesture state property as the gesture’s value changes.
- [onChanged(_:)](<onchanged(__).md>) — Adds an action to perform when the gesture’s value changes.
- [Value](value.md) — The type representing the gesture’s value.
