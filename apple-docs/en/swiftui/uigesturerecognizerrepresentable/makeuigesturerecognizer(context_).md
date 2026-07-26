---
title: 'makeUIGestureRecognizer(context:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/uigesturerecognizerrepresentable/makeuigesturerecognizer(context:)'
source_url: 'https://developer.apple.com/documentation/swiftui/uigesturerecognizerrepresentable/makeuigesturerecognizer(context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uigesturerecognizerrepresentable/makeuigesturerecognizer%28context%3A%29.json'
content_hash: 'sha256:04db79f3e6c8ddc6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UIGestureRecognizerRepresentable](../uigesturerecognizerrepresentable.md)

# makeUIGestureRecognizer(context:)

<sub>Instance Method</sub>

Creates an instance of the represented gesture recognizer.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor @preconcurrency func makeUIGestureRecognizer(context: Self.Context) -> Self.UIGestureRecognizerType
```

## Parameters

- `context` — A context structure containing information about the current state of the system, such as the current coordinator instance.

## Discussion

> [!note] Note
> Gesture recognizers are created on-demand and torn down when an event sequence ends, so do not perform expensive work in this method.
