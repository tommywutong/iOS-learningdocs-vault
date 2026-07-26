---
title: AttributedString.MarkdownParsingOptions.InterpretedSyntax
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributedstring/markdownparsingoptions/interpretedsyntax-swift.enum
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/markdownparsingoptions/interpretedsyntax-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/markdownparsingoptions/interpretedsyntax-swift.enum.json'
content_hash: 'sha256:0bc2bbd99e5ab62d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [AttributedString](../../attributedstring.md) · [MarkdownParsingOptions](../markdownparsingoptions.md)

# AttributedString.MarkdownParsingOptions.InterpretedSyntax

<sub>Enumeration</sub>

A type that represents the syntax for interpreting a Markdown string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum InterpretedSyntax
```

## Relationships

- **Conforms To**: [Copyable](../../../swift/copyable.md), [Equatable](../../../swift/equatable.md), [Escapable](../../../swift/escapable.md), [Hashable](../../../swift/hashable.md), [RawRepresentable](../../../swift/rawrepresentable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Syntax Values

- [AttributedString.MarkdownParsingOptions.InterpretedSyntax.full](interpretedsyntax-swift.enum/full.md) — A syntax value that interprets the full Markdown syntax and produces all relevant attributes.
- [AttributedString.MarkdownParsingOptions.InterpretedSyntax.inlineOnly](interpretedsyntax-swift.enum/inlineonly.md) — A syntax value that parses all Markdown text, but interprets only attributes that apply to inline spans.
- [AttributedString.MarkdownParsingOptions.InterpretedSyntax.inlineOnlyPreservingWhitespace](interpretedsyntax-swift.enum/inlineonlypreservingwhitespace.md) — A syntax value that parses all Markdown text, but interprets only attributes that apply to inline spans, preserving white space.

## See Also

### Accessing Options

- [allowsExtendedAttributes](allowsextendedattributes.md) — A Boolean value that indicates whether parsing allows extensions to Markdown that specify extended attributes.
- [appliesSourcePositionAttributes](appliessourcepositionattributes.md) — A Boolean value that indicates whether parsing applies attributes that indicate the position of attributed text in the original Markdown string.
- [failurePolicy](failurepolicy-swift.property.md) — The policy for handling a parsing failure.
- [FailurePolicy](failurepolicy-swift.enum.md) — A type that represents policies for handling parsing failures.
- [interpretedSyntax](interpretedsyntax-swift.property.md) — The syntax for interpreting a Markdown string.
- [languageCode](languagecode.md) — The language code for this document.
