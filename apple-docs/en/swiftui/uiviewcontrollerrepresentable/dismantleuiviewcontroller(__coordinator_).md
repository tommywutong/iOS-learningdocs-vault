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
doc_path: '/documentation/swiftui/uiviewcontrollerrepresentable/dismantleuiviewcontroller(_:coordinator:)'
source_url: 'https://developer.apple.com/documentation/swiftui/uiviewcontrollerrepresentable/dismantleuiviewcontroller(_:coordinator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uiviewcontrollerrepresentable/dismantleuiviewcontroller%28_%3Acoordinator%3A%29.json'
content_hash: 'sha256:ae9a23b9ac13053c'
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

## Default Implementations

### UIViewControllerRepresentable Implementations

- [dismantleUIViewController(_:coordinator:)](<dismantleuiviewcontroller(__coordinator_)-30a1m.md>) — Cleans up the presented view controller (and coordinator) in anticipation of their removal.
