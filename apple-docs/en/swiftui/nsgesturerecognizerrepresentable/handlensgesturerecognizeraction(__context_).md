---
title: 'handleNSGestureRecognizerAction(_:context:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/nsgesturerecognizerrepresentable/handlensgesturerecognizeraction(_:context:)'
source_url: 'https://developer.apple.com/documentation/swiftui/nsgesturerecognizerrepresentable/handlensgesturerecognizeraction(_:context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nsgesturerecognizerrepresentable/handlensgesturerecognizeraction%28_%3Acontext%3A%29.json'
content_hash: 'sha256:11d2270fc9388652'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSGestureRecognizerRepresentable](../nsgesturerecognizerrepresentable.md)

# handleNSGestureRecognizerAction(_:context:)

<sub>Instance Method</sub>

Handles recognition of the represented `NSGestureRecognizer`.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency func handleNSGestureRecognizerAction(_ recognizer: Self.NSGestureRecognizerType, context: Self.Context)
```

## Parameters

- `recognizer` — An instance of the represented gesture recognizer.

- `context` — A context structure containing information about the current state of the system, such as the current coordinator instance.

## Discussion

If you implement this method, SwiftUI calls it when the wrapped gesture recognizer is recognized.

## Default Implementations

### NSGestureRecognizerRepresentable Implementations

- [handleNSGestureRecognizerAction(_:context:)](<handlensgesturerecognizeraction(__context_)-8n3is.md>) — Handles recognition of the represented `NSGestureRecognizer`.
