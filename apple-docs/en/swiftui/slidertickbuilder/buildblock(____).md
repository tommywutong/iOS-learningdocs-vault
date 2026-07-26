---
title: 'buildBlock(_:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/slidertickbuilder/buildblock(_:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/slidertickbuilder/buildblock(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/slidertickbuilder/buildblock%28_%3A_%3A%29.json'
content_hash: 'sha256:c9f7b7f43c7af897'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SliderTickBuilder](../slidertickbuilder.md)

# buildBlock(_:_:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func buildBlock<C0, C1>(_ c0: C0, _ c1: C1) -> some SliderTickContent<V> where V == C0.Value, C0 : SliderTickContent, C1 : SliderTickContent, C0.Value == C1.Value

```
