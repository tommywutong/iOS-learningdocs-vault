---
title: 'callAsFunction(id:value:sharingBehavior:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/openwindowaction/callasfunction(id:value:sharingbehavior:)'
source_url: 'https://developer.apple.com/documentation/swiftui/openwindowaction/callasfunction(id:value:sharingbehavior:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/openwindowaction/callasfunction%28id%3Avalue%3Asharingbehavior%3A%29.json'
content_hash: 'sha256:76ce36470bf78372'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [OpenWindowAction](../openwindowaction.md)

# callAsFunction(id:value:sharingBehavior:)

<sub>Instance Method</sub>

Opens a window defined by the window group that presents the specified value type and that’s associated with the specified identifier, using the specified sharingBehavior.

<sub>macOS</sub>

```swift
@MainActor func callAsFunction<D>(id: String, value: D, sharingBehavior: OpenWindowAction.SharingBehavior) async throws where D : Decodable, D : Encodable, D : Hashable
```

## Parameters

- `id` — The identifier of the scene to present.

- `value` — The value to present.

- `sharingBehavior` — The sharing behavior for the opened window.

## Discussion

If sharingBehavior is requested or required, the window is shared if there is an available sharingSession and the person using your app confirms the offer to share. If sharingBehavior is requested and the window is not shared, it is opened normally. If sharingBehavior is required and the window is not shared, it is not opened, and an error is thrown. Regardless of sharingBehavior, an error is thrown if the window fails to open.

Don’t call this method directly. SwiftUI calls it when you call the [openWindow](../environmentvalues/openwindow.md) action with an identifier and a value:

```swift
try await openWindow(id: "message", value: message.id,
    sharingBehavior: .required)
```

For information about how Swift uses the `callAsFunction()` method to simplify call site syntax, see [Methods with Special Names](https://docs.swift.org/swift-book/ReferenceManual/Declarations.html#ID622) in _The Swift Programming Language_.
