---
title: 'withState(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/animationcontext/withstate(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/animationcontext/withstate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/animationcontext/withstate%28_%3A%29.json'
content_hash: 'sha256:c02165500b40de89'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AnimationContext](../animationcontext.md)

# withState(_:)

<sub>Instance Method</sub>

Creates a new context from another one with a state that you provide.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withState<T>(_ state: AnimationState<T>) -> AnimationContext<T> where T : VectorArithmetic
```

## Parameters

- `state` — The initial state for the new context.

## Return Value

A new context that contains the specified state.

## Discussion

Use this method to create a new context that contains the state that you provide and view environment values from the original context.
