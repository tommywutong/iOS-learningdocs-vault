---
title: makeCoordinator()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/nsviewrepresentable/makecoordinator()-6l2eg
source_url: 'https://developer.apple.com/documentation/swiftui/nsviewrepresentable/makecoordinator()-6l2eg'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nsviewrepresentable/makecoordinator%28%29-6l2eg.json'
content_hash: 'sha256:ebd206cbb8412c90'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSViewRepresentable](../nsviewrepresentable.md)

# makeCoordinator()

<sub>Instance Method</sub>

Creates a `Coordinator` instance to coordinate with the `NSView`.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency func makeCoordinator() -> Self.Coordinator
```

## Discussion

`Coordinator` can be accessed via `Context`.
