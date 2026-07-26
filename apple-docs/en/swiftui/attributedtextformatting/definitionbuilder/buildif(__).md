---
title: 'buildIf(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/attributedtextformatting/definitionbuilder/buildif(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/attributedtextformatting/definitionbuilder/buildif(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/attributedtextformatting/definitionbuilder/buildif%28_%3A%29.json'
content_hash: 'sha256:b1bf392e356f5804'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [AttributedTextFormatting](../../attributedtextformatting.md) · [DefinitionBuilder](../definitionbuilder.md)

# buildIf(_:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func buildIf<D>(_ definition: D?) -> D? where Scope == D.Scope, D : AttributedTextFormattingDefinition
```
