---
title: 'updateUIGestureRecognizer(_:context:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/uigesturerecognizerrepresentable/updateuigesturerecognizer(_:context:)-10jv'
source_url: 'https://developer.apple.com/documentation/swiftui/uigesturerecognizerrepresentable/updateuigesturerecognizer(_:context:)-10jv'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uigesturerecognizerrepresentable/updateuigesturerecognizer%28_%3Acontext%3A%29-10jv.json'
content_hash: 'sha256:99b6f797d88f3335'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UIGestureRecognizerRepresentable](../uigesturerecognizerrepresentable.md)

# updateUIGestureRecognizer(_:context:)

<sub>Instance Method</sub>

Updates the `UIGestureRecognizer` (and coordinator) to the latest configuration.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor @preconcurrency func updateUIGestureRecognizer(_ recognizer: Self.UIGestureRecognizerType, context: Self.Context)
```

## Parameters

- `recognizer` — An instance of the represented gesture recognizer.

- `context` — A context structure containing information about the current state of the system, such as the current coordinator instance.
