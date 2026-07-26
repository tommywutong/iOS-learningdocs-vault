---
title: 'callAsFunction(value:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/pushwindowaction/callasfunction(value:)'
source_url: 'https://developer.apple.com/documentation/swiftui/pushwindowaction/callasfunction(value:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/pushwindowaction/callasfunction%28value%3A%29.json'
content_hash: 'sha256:6a93ef8fd65bd4af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PushWindowAction](../pushwindowaction.md)

# callAsFunction(value:)

<sub>Instance Method</sub>

Pushes a window defined by a window group that presents the type of the specified value.

<sub>visionOS</sub>

```swift
@MainActor func callAsFunction<D>(value: D) where D : Decodable, D : Encodable, D : Hashable
```

## Parameters

- `value` — The value to present.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the [pushWindow](../environmentvalues/pushwindow.md) action with a value:

```swift
pushWindow(value: video.id)
```

For information about how Swift uses the `callAsFunction()` method to simplify call site syntax, see [Methods with Special Names](https://docs.swift.org/swift-book/ReferenceManual/Declarations.html#ID622) in _The Swift Programming Language_.
