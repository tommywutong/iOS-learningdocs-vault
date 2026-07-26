---
title: 'buildBlock(_:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/attributedtextformatting/definitionbuilder/buildblock(_:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/attributedtextformatting/definitionbuilder/buildblock(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/attributedtextformatting/definitionbuilder/buildblock%28_%3A_%3A%29.json'
content_hash: 'sha256:58efaa7b353d4dda'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [AttributedTextFormatting](../../attributedtextformatting.md) · [DefinitionBuilder](../definitionbuilder.md)

# buildBlock(_:_:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func buildBlock<F, each D>(_ first: F, _ definition: repeat each D) -> AttributedTextFormatting.TupleDefinition<F.Scope, F, repeat each D> where F : AttributedTextFormattingDefinition, repeat each D : AttributedTextFormattingDefinition
```
