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
doc_path: /documentation/swiftui/nsviewcontrollerrepresentable/makecoordinator()-72re2
source_url: 'https://developer.apple.com/documentation/swiftui/nsviewcontrollerrepresentable/makecoordinator()-72re2'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nsviewcontrollerrepresentable/makecoordinator%28%29-72re2.json'
content_hash: 'sha256:1875b72ec2fe23b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSViewControllerRepresentable](../nsviewcontrollerrepresentable.md)

# makeCoordinator()

<sub>Instance Method</sub>

Creates an object to coordinate with the AppKit view controller.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency func makeCoordinator() -> Self.Coordinator
```

## Discussion

`Coordinator` can be accessed via `Context`.
