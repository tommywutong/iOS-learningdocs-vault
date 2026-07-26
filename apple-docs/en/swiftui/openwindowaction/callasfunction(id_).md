---
title: 'callAsFunction(id:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/openwindowaction/callasfunction(id:)'
source_url: 'https://developer.apple.com/documentation/swiftui/openwindowaction/callasfunction(id:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/openwindowaction/callasfunction%28id%3A%29.json'
content_hash: 'sha256:4360f0e7a60e0691'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [OpenWindowAction](../openwindowaction.md)

# callAsFunction(id:)

<sub>Instance Method</sub>

Opens a window that’s associated with the specified identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency func callAsFunction(id: String)
```

## Parameters

- `id` — The identifier of the scene to present.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the [openWindow](../environmentvalues/openwindow.md) action with an identifier:

```swift
openWindow(id: "message")
```

For information about how Swift uses the `callAsFunction()` method to simplify call site syntax, see [Methods with Special Names](https://docs.swift.org/swift-book/ReferenceManual/Declarations.html#ID622) in _The Swift Programming Language_.

## See Also

### Calling the action

- [callAsFunction(id:value:)](<callasfunction(id_value_).md>) — Opens a window defined by the window group that presents the specified value type and that’s associated with the specified identifier.
- [callAsFunction(value:)](<callasfunction(value_).md>) — Opens a window defined by a window group that presents the type of the specified value.
