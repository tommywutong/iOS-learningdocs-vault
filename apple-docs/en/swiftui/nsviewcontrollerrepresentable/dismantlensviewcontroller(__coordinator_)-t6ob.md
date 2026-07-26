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
doc_path: '/documentation/swiftui/nsviewcontrollerrepresentable/dismantlensviewcontroller(_:coordinator:)-t6ob'
source_url: 'https://developer.apple.com/documentation/swiftui/nsviewcontrollerrepresentable/dismantlensviewcontroller(_:coordinator:)-t6ob'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nsviewcontrollerrepresentable/dismantlensviewcontroller%28_%3Acoordinator%3A%29-t6ob.json'
content_hash: 'sha256:7a61c8ec8b8ce6ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSViewControllerRepresentable](../nsviewcontrollerrepresentable.md)

# dismantleNSViewController(_:coordinator:)

<sub>Type Method</sub>

Cleans up the presented `NSViewController` (and coordinator) in anticipation of their removal.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency static func dismantleNSViewController(_ nsViewController: Self.NSViewControllerType, coordinator: Self.Coordinator)
```
