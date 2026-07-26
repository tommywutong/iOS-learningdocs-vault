---
title: 'dismantleUIView(_:coordinator:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/uiviewrepresentable/dismantleuiview(_:coordinator:)'
source_url: 'https://developer.apple.com/documentation/swiftui/uiviewrepresentable/dismantleuiview(_:coordinator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uiviewrepresentable/dismantleuiview%28_%3Acoordinator%3A%29.json'
content_hash: 'sha256:cb0c8284c8835cf3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UIViewRepresentable](../uiviewrepresentable.md)

# dismantleUIView(_:coordinator:)

<sub>Type Method</sub>

Cleans up the presented UIKit view (and coordinator) in anticipation of their removal.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency static func dismantleUIView(_ uiView: Self.UIViewType, coordinator: Self.Coordinator)
```

## Parameters

- `uiView` — Your custom view object.

- `coordinator` — The custom coordinator instance you use to communicate changes back to SwiftUI. If you do not use a custom coordinator, the system provides a default instance.

## Discussion

Use this method to perform additional clean-up work related to your custom view. For example, you might use this method to remove observers or update other parts of your SwiftUI interface.

## Default Implementations

### UIViewRepresentable Implementations

- [dismantleUIView(_:coordinator:)](<dismantleuiview(__coordinator_)-94s0o.md>) — Cleans up the presented UIKit view (and coordinator) in anticipation of their removal.
