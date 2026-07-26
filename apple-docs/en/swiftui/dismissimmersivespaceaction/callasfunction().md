---
title: callAsFunction()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 26.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/dismissimmersivespaceaction/callasfunction()
source_url: 'https://developer.apple.com/documentation/swiftui/dismissimmersivespaceaction/callasfunction()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dismissimmersivespaceaction/callasfunction%28%29.json'
content_hash: 'sha256:9cc09eae9ab74c7c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DismissImmersiveSpaceAction](../dismissimmersivespaceaction.md)

# callAsFunction()

<sub>Instance Method</sub>

Dismisses the currently opened immersive space.

<sub>macOS, visionOS</sub>

```swift
@MainActor func callAsFunction() async
```

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the [dismissImmersiveSpace](../environmentvalues/dismissimmersivespace.md) action:

```swift
await dismissImmersiveSpace()
```

For information about how Swift uses the `callAsFunction()` method to simplify call site syntax, see [Methods with Special Names](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/declarations/#Methods-with-Special-Names) in _The Swift Programming Language_.
