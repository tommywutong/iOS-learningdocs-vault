---
title: 'init(text:in:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/attributedtextformatting/transferable/init(text:in:)'
source_url: 'https://developer.apple.com/documentation/swiftui/attributedtextformatting/transferable/init(text:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/attributedtextformatting/transferable/init%28text%3Ain%3A%29.json'
content_hash: 'sha256:4f6a6300199bd879'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [AttributedTextFormatting](../../attributedtextformatting.md) · [Transferable](../transferable.md)

# init(text:in:)

<sub>Initializer</sub>

Create a transferable representation of an attributed string as interpreted in a SwiftUI environment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(text: AttributedString, in environment: EnvironmentValues)
```

## Discussion

When exporting the `text` into different data formats, the transfer representation may use the given `environment` to resolve semantic attribute values, such as certain colors or fonts to concrete values. This means that depending on the representation used during transfer, some semantic information may be lost in that step.

> [!note] Note
> The transferable representation applies the [AttributedTextFormattingDefinition](../../attributedtextformattingdefinition.md) in the `environment` before exporting the content.

> [!info] See Also
> `View/attributedTextFormattingDefinition(_:)-uc57`, `AttributedTextValueConstraint/constrain(_:)-6cp64`
