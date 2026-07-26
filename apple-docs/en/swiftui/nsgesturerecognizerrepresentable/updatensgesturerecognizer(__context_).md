---
title: 'updateNSGestureRecognizer(_:context:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/nsgesturerecognizerrepresentable/updatensgesturerecognizer(_:context:)'
source_url: 'https://developer.apple.com/documentation/swiftui/nsgesturerecognizerrepresentable/updatensgesturerecognizer(_:context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nsgesturerecognizerrepresentable/updatensgesturerecognizer%28_%3Acontext%3A%29.json'
content_hash: 'sha256:78834905ec82de42'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSGestureRecognizerRepresentable](../nsgesturerecognizerrepresentable.md)

# updateNSGestureRecognizer(_:context:)

<sub>Instance Method</sub>

Updates the `NSGestureRecognizer` (and coordinator) to the latest configuration.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency func updateNSGestureRecognizer(_ recognizer: Self.NSGestureRecognizerType, context: Self.Context)
```

## Parameters

- `recognizer` — An instance of the represented gesture recognizer.

- `context` — A context structure containing information about the current state of the system, such as the current coordinator instance.

## Default Implementations

### NSGestureRecognizerRepresentable Implementations

- [updateNSGestureRecognizer(_:context:)](<updatensgesturerecognizer(__context_)-1s5x4.md>) — Updates the `NSGestureRecognizer` (and coordinator) to the latest configuration.
