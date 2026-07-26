---
title: 'callAsFunction(value:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/dismisswindowaction/callasfunction(value:)'
source_url: 'https://developer.apple.com/documentation/swiftui/dismisswindowaction/callasfunction(value:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dismisswindowaction/callasfunction%28value%3A%29.json'
content_hash: 'sha256:dc932a92dbf3d19f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DismissWindowAction](../dismisswindowaction.md)

# callAsFunction(value:)

<sub>Instance Method</sub>

Dismisses the window defined by the window group that is presenting the specified value type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency func callAsFunction<D>(value: D) where D : Decodable, D : Encodable, D : Hashable
```

## Parameters

- `value` — The value which is currently presented.

## Discussion

If multiple windows match the provided value, then they all will be dismissed. For dismissing a specific window in a specific group, use `dismissWindow(id:value:)`.

Don’t call this method directly. SwiftUI calls it when you call the [dismissWindow](../environmentvalues/dismisswindow.md) action with an identifier and a value:

```swift
dismissWindow(value: message.id)
```

For information about how Swift uses the `callAsFunction()` method to simplify call site syntax, see [Methods with Special Names](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/declarations#Methods-with-Special-Names) in _The Swift Programming Language_.

## See Also

### Calling the action

- [callAsFunction()](<callasfunction().md>) — Dismisses the current window.
- [callAsFunction(id:)](<callasfunction(id_).md>) — Dismisses the window that’s associated with the specified identifier.
- [callAsFunction(id:value:)](<callasfunction(id_value_).md>) — Dismisses the window defined by the window group that is presenting the specified value type and that’s associated with the specified identifier.
