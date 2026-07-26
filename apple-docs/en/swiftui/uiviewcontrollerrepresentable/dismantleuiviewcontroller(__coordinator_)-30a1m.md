---
title: 'dismantleUIViewController(_:coordinator:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/uiviewcontrollerrepresentable/dismantleuiviewcontroller(_:coordinator:)-30a1m'
source_url: 'https://developer.apple.com/documentation/swiftui/uiviewcontrollerrepresentable/dismantleuiviewcontroller(_:coordinator:)-30a1m'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uiviewcontrollerrepresentable/dismantleuiviewcontroller%28_%3Acoordinator%3A%29-30a1m.json'
content_hash: 'sha256:8b1397326b7a3e30'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UIViewControllerRepresentable](../uiviewcontrollerrepresentable.md)

# dismantleUIViewController(_:coordinator:)

<sub>Type Method</sub>

Cleans up the presented view controller (and coordinator) in anticipation of their removal.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency static func dismantleUIViewController(_ uiViewController: Self.UIViewControllerType, coordinator: Self.Coordinator)
```

## Parameters

- `uiViewController` — Your custom view controller object.

- `coordinator` — The custom coordinator instance you use to communicate changes back to SwiftUI. If you do not use a custom coordinator, the system provides a default instance.

## Discussion

Use this method to perform additional clean-up work related to your custom view controller. For example, you might use this method to remove observers or update other parts of your SwiftUI interface.
