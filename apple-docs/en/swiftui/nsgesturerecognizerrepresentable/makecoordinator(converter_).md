---
title: 'makeCoordinator(converter:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/nsgesturerecognizerrepresentable/makecoordinator(converter:)'
source_url: 'https://developer.apple.com/documentation/swiftui/nsgesturerecognizerrepresentable/makecoordinator(converter:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nsgesturerecognizerrepresentable/makecoordinator%28converter%3A%29.json'
content_hash: 'sha256:1600dc9dd9c274c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSGestureRecognizerRepresentable](../nsgesturerecognizerrepresentable.md)

# makeCoordinator(converter:)

<sub>Instance Method</sub>

Creates the custom object that you use to communicate state changes from your gesture recognizer to other parts of your SwiftUI interface.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency func makeCoordinator(converter: Self.CoordinateSpaceConverter) -> Self.Coordinator
```

## Parameters

- `converter` — A structure used to convert locations  to/from coordinate spaces in the hierarchy of the associated SwiftUI view.

## Discussion

You access the resulting coordinator via the `Context` passed into other methods in this protocol.

## Default Implementations

### NSGestureRecognizerRepresentable Implementations

- [makeCoordinator(converter:)](<makecoordinator(converter_)-8fzsl.md>)
