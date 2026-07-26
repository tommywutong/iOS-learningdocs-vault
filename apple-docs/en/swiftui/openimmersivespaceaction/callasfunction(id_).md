---
title: 'callAsFunction(id:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 26.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/openimmersivespaceaction/callasfunction(id:)'
source_url: 'https://developer.apple.com/documentation/swiftui/openimmersivespaceaction/callasfunction(id:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/openimmersivespaceaction/callasfunction%28id%3A%29.json'
content_hash: 'sha256:e5e1b615cb561548'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [OpenImmersiveSpaceAction](../openimmersivespaceaction.md)

# callAsFunction(id:)

<sub>Instance Method</sub>

Presents an immersive space for the scene with the specified identifier.

<sub>macOS, visionOS</sub>

```swift
@discardableResult @MainActor func callAsFunction(id: String) async -> OpenImmersiveSpaceAction.Result
```

## Parameters

- `id` — The identifier of the immersive space to present.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the [openImmersiveSpace](../environmentvalues/openimmersivespace.md) action with a string identifier:

```swift
await openImmersiveSpace(id: "planet")
```

For information about how Swift uses the `callAsFunction()` method to simplify call site syntax, see [Methods with Special Names](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/declarations/#Methods-with-Special-Names) in _The Swift Programming Language_.

## See Also

### Calling the action

- [callAsFunction(id:value:)](<callasfunction(id_value_).md>) — Presents the immersive space that your app defines for the specified identifier and that handles the type of the presented value.
- [callAsFunction(value:)](<callasfunction(value_).md>) — Presents the immersive space that handles the type of the presented value.
