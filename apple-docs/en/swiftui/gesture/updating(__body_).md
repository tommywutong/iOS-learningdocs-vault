---
title: 'updating(_:body:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/gesture/updating(_:body:)'
source_url: 'https://developer.apple.com/documentation/swiftui/gesture/updating(_:body:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/gesture/updating%28_%3Abody%3A%29.json'
content_hash: 'sha256:ad56ac9e1e33e026'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Gesture](../gesture.md)

# updating(_:body:)

<sub>Instance Method</sub>

Updates the provided gesture state property as the gesture’s value changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency func updating<State>(_ state: GestureState<State>, body: @escaping (Self.Value, inout State, inout Transaction) -> Void) -> GestureStateGesture<Self, State>
```

## Parameters

- `state` — A binding to a view’s [GestureState](../gesturestate.md) property.

- `body` — The callback that SwiftUI invokes as the gesture’s value changes. Its `currentState` parameter is the updated state of the gesture. The `gestureState` parameter is the previous state of the gesture, and the `transaction` is the context of the gesture.

## Return Value

A version of the gesture that updates the provided `state` as the originating gesture’s value changes and that resets the `state` to its initial value when the user or the system ends or cancels the gesture.

## Discussion

Use this callback to update transient UI state as described in [Adding interactivity with gestures](../adding-interactivity-with-gestures.md).

## See Also

### Performing the gesture

- [onChanged(_:)](<onchanged(__).md>) — Adds an action to perform when the gesture’s value changes.
- [onEnded(_:)](<onended(__).md>) — Adds an action to perform when the gesture ends.
- [Value](value.md) — The type representing the gesture’s value.
