---
title: AttributedTextFormatting.TupleDefinition
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/attributedtextformatting/tupledefinition
source_url: 'https://developer.apple.com/documentation/swiftui/attributedtextformatting/tupledefinition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/attributedtextformatting/tupledefinition.json'
content_hash: 'sha256:53be0cff3026c061'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AttributedTextFormatting](../attributedtextformatting.md)

# AttributedTextFormatting.TupleDefinition

<sub>Structure</sub>

A text formatting definition that enforces the constraints of a series of text formatting definitions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct TupleDefinition<Scope, each Definition> where Scope : AttributeScope, repeat each Definition : AttributedTextFormattingDefinition
```

## Overview

> [!note] Note
> All sub-definitions are required to have the same `Scope`.

## Relationships

- **Conforms To**: [AttributedTextFormattingDefinition](../attributedtextformattingdefinition.md)

## Topics

### Initializers

- [init(definition:)](<tupledefinition/init(definition_).md>)
