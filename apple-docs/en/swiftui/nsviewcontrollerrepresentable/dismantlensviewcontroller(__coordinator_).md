---
title: 'dismantleNSViewController(_:coordinator:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/nsviewcontrollerrepresentable/dismantlensviewcontroller(_:coordinator:)'
source_url: 'https://developer.apple.com/documentation/swiftui/nsviewcontrollerrepresentable/dismantlensviewcontroller(_:coordinator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nsviewcontrollerrepresentable/dismantlensviewcontroller%28_%3Acoordinator%3A%29.json'
content_hash: 'sha256:eed7d2cee2329c43'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSViewControllerRepresentable](../nsviewcontrollerrepresentable.md)

# dismantleNSViewController(_:coordinator:)

<sub>Type Method</sub>

Cleans up the presented view controller (and coordinator) in anticipation of its removal.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency static func dismantleNSViewController(_ nsViewController: Self.NSViewControllerType, coordinator: Self.Coordinator)
```

## Parameters

- `nsViewController` — Your custom view controller object.

- `coordinator` — The custom coordinator instance you use to communicate changes back to SwiftUI. If you do not use a custom coordinator, the system provides a default instance.

## Discussion

Use this method to perform additional clean-up work related to your custom view controller. For example, you might use this method to remove observers or update other parts of your SwiftUI interface.

## Default Implementations

### NSViewControllerRepresentable Implementations

- [dismantleNSViewController(_:coordinator:)](<dismantlensviewcontroller(__coordinator_)-t6ob.md>) — Cleans up the presented `NSViewController` (and coordinator) in anticipation of their removal.
