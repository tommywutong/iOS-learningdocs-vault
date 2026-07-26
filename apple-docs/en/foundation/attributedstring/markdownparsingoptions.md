---
title: AttributedString.MarkdownParsingOptions
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributedstring/markdownparsingoptions
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/markdownparsingoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/markdownparsingoptions.json'
content_hash: 'sha256:ad6432966ed6b3e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# AttributedString.MarkdownParsingOptions

<sub>Structure</sub>

Options that affect the parsing of Markdown content into an attributed string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MarkdownParsingOptions
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [Escapable](../../swift/escapable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating Markdown Parsing Options

- [init(allowsExtendedAttributes:interpretedSyntax:failurePolicy:languageCode:)](<markdownparsingoptions/init(allowsextendedattributes_interpretedsyntax_failurepolicy_languagecode_).md>) — Creates a Markdown parsing options instance with the specified values.
- [init(allowsExtendedAttributes:interpretedSyntax:failurePolicy:languageCode:appliesSourcePositionAttributes:)](<markdownparsingoptions/init(allowsextendedattributes_interpretedsyntax_failurepolicy_languagecode_appliessourcepositionattributes_).md>) — Creates a Markdown parsing options instance with the specified values, optionally marking the source position of attributed text.

### Accessing Options

- [allowsExtendedAttributes](markdownparsingoptions/allowsextendedattributes.md) — A Boolean value that indicates whether parsing allows extensions to Markdown that specify extended attributes.
- [appliesSourcePositionAttributes](markdownparsingoptions/appliessourcepositionattributes.md) — A Boolean value that indicates whether parsing applies attributes that indicate the position of attributed text in the original Markdown string.
- [failurePolicy](markdownparsingoptions/failurepolicy-swift.property.md) — The policy for handling a parsing failure.
- [FailurePolicy](markdownparsingoptions/failurepolicy-swift.enum.md) — A type that represents policies for handling parsing failures.
- [interpretedSyntax](markdownparsingoptions/interpretedsyntax-swift.property.md) — The syntax for interpreting a Markdown string.
- [InterpretedSyntax](markdownparsingoptions/interpretedsyntax-swift.enum.md) — A type that represents the syntax for interpreting a Markdown string.
- [languageCode](markdownparsingoptions/languagecode.md) — The language code for this document.
