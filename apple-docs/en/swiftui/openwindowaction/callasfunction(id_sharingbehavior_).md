---
title: 'callAsFunction(id:sharingBehavior:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/openwindowaction/callasfunction(id:sharingbehavior:)'
source_url: 'https://developer.apple.com/documentation/swiftui/openwindowaction/callasfunction(id:sharingbehavior:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/openwindowaction/callasfunction%28id%3Asharingbehavior%3A%29.json'
content_hash: 'sha256:7c26af0bfee1c9ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [OpenWindowAction](../openwindowaction.md)

# callAsFunction(id:sharingBehavior:)

<sub>Instance Method</sub>

Opens a window that’s associated with the specified identifier, using the specified sharing sharingBehavior..

<sub>macOS</sub>

```swift
@MainActor func callAsFunction(id: String, sharingBehavior: OpenWindowAction.SharingBehavior) async throws
```

## Parameters

- `id` — The identifier of the scene to present.

- `sharingBehavior` — The sharing behavior for the opened window.

## Discussion

If sharingBehavior is requested or required, the window is shared if there is an available sharingSession and the person using your app confirms the offer to share. If sharingBehavior is requested and the window is not shared, it is opened normally. If sharingBehavior is required and the window is not shared, it is not opened, and an error is thrown. Regardless of sharingBehavior, an error is thrown if the window fails to open.

Don’t call this method directly. SwiftUI calls it when you call the [openWindow](../environmentvalues/openwindow.md) action with an identifier:

```swift
try await openWindow(id: "message", sharingBehavior: .requested)
```

For information about how Swift uses the `callAsFunction()` method to simplify call site syntax, see [Methods with Special Names](https://docs.swift.org/swift-book/ReferenceManual/Declarations.html#ID622) in _The Swift Programming Language_.
