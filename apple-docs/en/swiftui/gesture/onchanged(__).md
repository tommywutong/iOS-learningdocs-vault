---
title: 'onChanged(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/gesture/onchanged(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/gesture/onchanged(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/gesture/onchanged%28_%3A%29.json'
content_hash: 'sha256:ab83b07f64be6279'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Gesture](../gesture.md)

# onChanged(_:)

<sub>Instance Method</sub>

Adds an action to perform when the gesture’s value changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func onChanged(_ action: @escaping (Self.Value) -> Void) -> _ChangedGesture<Self>
```

## Parameters

- `action` — The action to perform when this gesture’s value changes. The `action` closure’s parameter contains the gesture’s new value.

## Return Value

A gesture that triggers `action` when this gesture’s value changes.

## See Also

### Performing the gesture

- [updating(_:body:)](<updating(__body_).md>) — Updates the provided gesture state property as the gesture’s value changes.
- [onEnded(_:)](<onended(__).md>) — Adds an action to perform when the gesture ends.
- [Value](value.md) — The type representing the gesture’s value.
