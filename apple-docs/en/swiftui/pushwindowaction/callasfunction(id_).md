---
title: 'callAsFunction(id:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/pushwindowaction/callasfunction(id:)'
source_url: 'https://developer.apple.com/documentation/swiftui/pushwindowaction/callasfunction(id:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/pushwindowaction/callasfunction%28id%3A%29.json'
content_hash: 'sha256:47b0e029ae919641'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PushWindowAction](../pushwindowaction.md)

# callAsFunction(id:)

<sub>Instance Method</sub>

Pushes a window that is associated with the specified identifier.

<sub>visionOS</sub>

```swift
@MainActor func callAsFunction(id: String)
```

## Parameters

- `id` — The identifier of the scene to present.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the [pushWindow](../environmentvalues/pushwindow.md) action with an identifier:

```swift
pushWindow(id: "viewer")
```

For information about how Swift uses the `callAsFunction()` method to simplify call site syntax, see [Methods with Special Names](https://docs.swift.org/swift-book/ReferenceManual/Declarations.html#ID622) in _The Swift Programming Language_.
