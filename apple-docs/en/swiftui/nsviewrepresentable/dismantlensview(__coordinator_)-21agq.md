---
title: 'dismantleNSView(_:coordinator:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/nsviewrepresentable/dismantlensview(_:coordinator:)-21agq'
source_url: 'https://developer.apple.com/documentation/swiftui/nsviewrepresentable/dismantlensview(_:coordinator:)-21agq'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nsviewrepresentable/dismantlensview%28_%3Acoordinator%3A%29-21agq.json'
content_hash: 'sha256:18cc5738c369ba65'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSViewRepresentable](../nsviewrepresentable.md)

# dismantleNSView(_:coordinator:)

<sub>Type Method</sub>

Cleans up the presented AppKit view (and coordinator) in anticipation of their removal.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency static func dismantleNSView(_ nsView: Self.NSViewType, coordinator: Self.Coordinator)
```
