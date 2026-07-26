---
title: 'handleUIGestureRecognizerAction(_:context:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/uigesturerecognizerrepresentable/handleuigesturerecognizeraction(_:context:)-8u4zs'
source_url: 'https://developer.apple.com/documentation/swiftui/uigesturerecognizerrepresentable/handleuigesturerecognizeraction(_:context:)-8u4zs'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uigesturerecognizerrepresentable/handleuigesturerecognizeraction%28_%3Acontext%3A%29-8u4zs.json'
content_hash: 'sha256:8185828a1a058a83'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UIGestureRecognizerRepresentable](../uigesturerecognizerrepresentable.md)

# handleUIGestureRecognizerAction(_:context:)

<sub>Instance Method</sub>

Handles recognition of the represented `UIGestureRecognizer`.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor @preconcurrency func handleUIGestureRecognizerAction(_ recognizer: Self.UIGestureRecognizerType, context: Self.Context)
```

## Parameters

- `recognizer` — An instance of the represented gesture recognizer.

- `context` — A context structure containing information about the current state of the system, such as the current coordinator instance.

## Discussion

If you implement this method, SwiftUI calls it when the wrapped gesture recognizer is recognized.
