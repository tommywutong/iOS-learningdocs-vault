---
title: 'makeNSGestureRecognizer(context:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/nsgesturerecognizerrepresentable/makensgesturerecognizer(context:)'
source_url: 'https://developer.apple.com/documentation/swiftui/nsgesturerecognizerrepresentable/makensgesturerecognizer(context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nsgesturerecognizerrepresentable/makensgesturerecognizer%28context%3A%29.json'
content_hash: 'sha256:a0b4490a4332d4e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSGestureRecognizerRepresentable](../nsgesturerecognizerrepresentable.md)

# makeNSGestureRecognizer(context:)

<sub>Instance Method</sub>

Creates an instance of the represented gesture recognizer.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency func makeNSGestureRecognizer(context: Self.Context) -> Self.NSGestureRecognizerType
```

## Parameters

- `context` — A context structure containing information about the current state of the system, such as the current coordinator instance.

## Discussion

> [!note] Note
> Gesture recognizers are created on-demand and torn down when an event sequence ends, so do not perform expensive work in this method.
