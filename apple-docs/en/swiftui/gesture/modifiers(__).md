---
title: 'modifiers(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/gesture/modifiers(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/gesture/modifiers(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/gesture/modifiers%28_%3A%29.json'
content_hash: 'sha256:fee1c1f62c97a233'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Gesture](../gesture.md)

# modifiers(_:)

<sub>Instance Method</sub>

Combines a gesture with keyboard modifiers.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency func modifiers(_ modifiers: EventModifiers) -> _ModifiersGesture<Self>
```

## Parameters

- `modifiers` — A set of flags that correspond to the modifier keys that the user needs to hold down.

## Return Value

A new gesture that combines a gesture with keyboard modifiers.

## Discussion

The gesture receives updates while the user presses the modifier keys that correspond to the given modifiers option set.
