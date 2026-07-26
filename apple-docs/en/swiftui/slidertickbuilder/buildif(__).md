---
title: 'buildIf(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/slidertickbuilder/buildif(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/slidertickbuilder/buildif(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/slidertickbuilder/buildif%28_%3A%29.json'
content_hash: 'sha256:92243690dd461b95'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SliderTickBuilder](../slidertickbuilder.md)

# buildIf(_:)

<sub>Type Method</sub>

Produces an optional slider content for conditional statements in multi-statement closures that’s only visible when the condition evaluates to true.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func buildIf(_ content: some SliderTickContent<V>) -> some SliderTickContent<V>

```
