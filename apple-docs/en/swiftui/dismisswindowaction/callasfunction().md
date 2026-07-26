---
title: callAsFunction()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/dismisswindowaction/callasfunction()
source_url: 'https://developer.apple.com/documentation/swiftui/dismisswindowaction/callasfunction()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dismisswindowaction/callasfunction%28%29.json'
content_hash: 'sha256:82f2cc1d9b44c5c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DismissWindowAction](../dismisswindowaction.md)

# callAsFunction()

<sub>Instance Method</sub>

Dismisses the current window.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency func callAsFunction()
```

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the [dismissWindow](../environmentvalues/dismisswindow.md) action:

```swift
dismissWindow()
```

For information about how Swift uses the `callAsFunction()` method to simplify call site syntax, see [Methods with Special Names](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/declarations#Methods-with-Special-Names) in _The Swift Programming Language_.

## See Also

### Calling the action

- [callAsFunction(id:)](<callasfunction(id_).md>) — Dismisses the window that’s associated with the specified identifier.
- [callAsFunction(id:value:)](<callasfunction(id_value_).md>) — Dismisses the window defined by the window group that is presenting the specified value type and that’s associated with the specified identifier.
- [callAsFunction(value:)](<callasfunction(value_).md>) — Dismisses the window defined by the window group that is presenting the specified value type.
