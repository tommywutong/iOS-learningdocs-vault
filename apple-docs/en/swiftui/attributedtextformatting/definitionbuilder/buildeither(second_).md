---
title: 'buildEither(second:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/attributedtextformatting/definitionbuilder/buildeither(second:)'
source_url: 'https://developer.apple.com/documentation/swiftui/attributedtextformatting/definitionbuilder/buildeither(second:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/attributedtextformatting/definitionbuilder/buildeither%28second%3A%29.json'
content_hash: 'sha256:ea068096e2dbb030'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [AttributedTextFormatting](../../attributedtextformatting.md) · [DefinitionBuilder](../definitionbuilder.md)

# buildEither(second:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func buildEither<T, F>(second: F) -> _ConditionalContent<T, F> where Scope == T.Scope, T : AttributedTextFormattingDefinition, F : AttributedTextFormattingDefinition, T.Scope == F.Scope
```
