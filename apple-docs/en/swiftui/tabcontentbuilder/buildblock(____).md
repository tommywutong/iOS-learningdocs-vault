---
title: 'buildBlock(_:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tabcontentbuilder/buildblock(_:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tabcontentbuilder/buildblock(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabcontentbuilder/buildblock%28_%3A_%3A%29.json'
content_hash: 'sha256:eeab5b253fed5cf3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TabContentBuilder](../tabcontentbuilder.md)

# buildBlock(_:_:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func buildBlock<C0, C1>(_ c0: C0, _ c1: C1) -> some TabContent<TabValue> where TabValue == C0.TabValue, C0 : TabContent, C1 : TabContent, C0.TabValue == C1.TabValue

```
