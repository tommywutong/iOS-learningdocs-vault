---
title: 'makeCoordinator(converter:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/uigesturerecognizerrepresentable/makecoordinator(converter:)'
source_url: 'https://developer.apple.com/documentation/swiftui/uigesturerecognizerrepresentable/makecoordinator(converter:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uigesturerecognizerrepresentable/makecoordinator%28converter%3A%29.json'
content_hash: 'sha256:92df416fadbce74e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UIGestureRecognizerRepresentable](../uigesturerecognizerrepresentable.md)

# makeCoordinator(converter:)

<sub>Instance Method</sub>

Creates the custom object that you use to communicate state changes from your gesture recognizer to other parts of your SwiftUI interface.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor @preconcurrency func makeCoordinator(converter: Self.CoordinateSpaceConverter) -> Self.Coordinator
```

## Parameters

- `converter` — A structure used to convert locations  to/from coordinate spaces in the hierarchy of the associated SwiftUI view.

## Discussion

You access the resulting coordinator via the `Context` passed into other methods in this protocol.

## Default Implementations

### UIGestureRecognizerRepresentable Implementations

- [makeCoordinator(converter:)](<makecoordinator(converter_)-504ge.md>)
