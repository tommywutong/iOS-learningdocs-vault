---
title: 'subscript(_:)'
framework: RealityKit
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/binding/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/binding/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/binding/subscript%28_%3A%29.json'
content_hash: 'sha256:a8b1aaea8b1305bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Binding](../binding.md)

# subscript(_:)

<sub>Instance Subscript</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
subscript<C>(componentType: C.Type) -> Binding<C?> where C : Component { get }
```
