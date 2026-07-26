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
doc_path: '/documentation/swiftui/nsviewrepresentable/dismantlensview(_:coordinator:)'
source_url: 'https://developer.apple.com/documentation/swiftui/nsviewrepresentable/dismantlensview(_:coordinator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nsviewrepresentable/dismantlensview%28_%3Acoordinator%3A%29.json'
content_hash: 'sha256:50411f3081ddade4'
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

## Parameters

- `nsView` — Your custom view object.

- `coordinator` — The custom coordinator you use to communicate changes back to SwiftUI. If you do not use a custom coordinator instance, the system provides a default instance.

## Discussion

Use this method to perform additional clean-up work related to your custom view. For example, you might use this method to remove observers or update other parts of your SwiftUI interface.

## Default Implementations

### NSViewRepresentable Implementations

- [dismantleNSView(_:coordinator:)](<dismantlensview(__coordinator_)-21agq.md>) — Cleans up the presented AppKit view (and coordinator) in anticipation of their removal.
