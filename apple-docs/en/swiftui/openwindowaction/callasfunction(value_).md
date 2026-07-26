---
title: 'callAsFunction(value:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/openwindowaction/callasfunction(value:)'
source_url: 'https://developer.apple.com/documentation/swiftui/openwindowaction/callasfunction(value:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/openwindowaction/callasfunction%28value%3A%29.json'
content_hash: 'sha256:92992c80e76097e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [OpenWindowAction](../openwindowaction.md)

# callAsFunction(value:)

<sub>Instance Method</sub>

Opens a window defined by a window group that presents the type of the specified value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency func callAsFunction<D>(value: D) where D : Decodable, D : Encodable, D : Hashable
```

## Parameters

- `value` — The value to present.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the [openWindow](../environmentvalues/openwindow.md) action with a value:

```swift
openWindow(value: message.id)
```

For information about how Swift uses the `callAsFunction()` method to simplify call site syntax, see [Methods with Special Names](https://docs.swift.org/swift-book/ReferenceManual/Declarations.html#ID622) in _The Swift Programming Language_.

## See Also

### Calling the action

- [callAsFunction(id:)](<callasfunction(id_).md>) — Opens a window that’s associated with the specified identifier.
- [callAsFunction(id:value:)](<callasfunction(id_value_).md>) — Opens a window defined by the window group that presents the specified value type and that’s associated with the specified identifier.
