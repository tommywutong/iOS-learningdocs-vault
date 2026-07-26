---
title: AttributedTextFormatting
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/attributedtextformatting
source_url: 'https://developer.apple.com/documentation/swiftui/attributedtextformatting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/attributedtextformatting.json'
content_hash: 'sha256:ee8716e25ae3afe2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AttributedTextFormatting

<sub>Enumeration</sub>

A namespace for types related to attributed text formatting definitions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum AttributedTextFormatting
```

## Overview

> [!info] See Also
> [AttributedTextFormattingDefinition](attributedtextformattingdefinition.md), `View/attributedTextFormattingDefinition(_:)-uc57`

## Topics

### Structures

- [AnyDefinition](attributedtextformatting/anydefinition.md) — A type-erased text formatting definition.
- [AttributeContainerProxy](attributedtextformatting/attributecontainerproxy.md) — A proxy for a partially validated set of attributes.
- [DefinitionBuilder](attributedtextformatting/definitionbuilder.md) — A result builder for attributed text formatting definition.
- [EmptyDefinition](attributedtextformatting/emptydefinition.md) — A text formatting definition that places no constraints on the values of attributes.
- [Transferable](attributedtextformatting/transferable.md) — A transferable representation of an attributed string interpreted in a SwiftUI environment.
- [TupleDefinition](attributedtextformatting/tupledefinition.md) — A text formatting definition that enforces the constraints of a series of text formatting definitions.
- [ValueConstraint](attributedtextformatting/valueconstraint.md) — A text formatting definition that constrains the value of a single attribute to the members of a set.

## See Also

### Controlling text style

- [bold(_:)](<view/bold(__).md>) — Applies a bold font weight to the text in this view.
- [italic(_:)](<view/italic(__).md>) — Applies italics to the text in this view.
- [underline(_:pattern:color:)](<view/underline(__pattern_color_).md>) — Applies an underline to the text in this view.
- [strikethrough(_:pattern:color:)](<view/strikethrough(__pattern_color_).md>) — Applies a strikethrough to the text in this view.
- [textCase(_:)](<view/textcase(__).md>) — Sets a transform for the case of the text contained in this view when displayed.
- [textCase](environmentvalues/textcase.md) — A stylistic override to transform the case of `Text` when displayed, using the environment’s locale.
- [monospaced(_:)](<view/monospaced(__).md>) — Modifies the fonts of all child views to use the fixed-width variant of the current font, if possible.
- [monospacedDigit()](<view/monospaceddigit().md>) — Modifies the fonts of all child views to use fixed-width digits, if possible, while leaving other characters proportionally spaced.
- [AttributedTextFormattingDefinition](attributedtextformattingdefinition.md) — A protocol for defining how text can be styled in a view.
- [AttributedTextValueConstraint](attributedtextvalueconstraint.md) — A protocol for defining a constraint on the value of a certain attribute.
