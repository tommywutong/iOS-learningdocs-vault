---
title: AttributedString.MarkdownParsingOptions.FailurePolicy
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributedstring/markdownparsingoptions/failurepolicy-swift.enum
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/markdownparsingoptions/failurepolicy-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/markdownparsingoptions/failurepolicy-swift.enum.json'
content_hash: 'sha256:69737970e7ce3b09'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [AttributedString](../../attributedstring.md) · [MarkdownParsingOptions](../markdownparsingoptions.md)

# AttributedString.MarkdownParsingOptions.FailurePolicy

<sub>Enumeration</sub>

A type that represents policies for handling parsing failures.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum FailurePolicy
```

## Relationships

- **Conforms To**: [Copyable](../../../swift/copyable.md), [Equatable](../../../swift/equatable.md), [Escapable](../../../swift/escapable.md), [Hashable](../../../swift/hashable.md), [RawRepresentable](../../../swift/rawrepresentable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Declaring Failure Policies

- [AttributedString.MarkdownParsingOptions.FailurePolicy.returnPartiallyParsedIfPossible](failurepolicy-swift.enum/returnpartiallyparsedifpossible.md) — A policy to return a partially-parsed string, if possible.
- [AttributedString.MarkdownParsingOptions.FailurePolicy.throwError](failurepolicy-swift.enum/throwerror.md) — A policy to throw an error from the initializer if parsing fails.

## See Also

### Accessing Options

- [allowsExtendedAttributes](allowsextendedattributes.md) — A Boolean value that indicates whether parsing allows extensions to Markdown that specify extended attributes.
- [appliesSourcePositionAttributes](appliessourcepositionattributes.md) — A Boolean value that indicates whether parsing applies attributes that indicate the position of attributed text in the original Markdown string.
- [failurePolicy](failurepolicy-swift.property.md) — The policy for handling a parsing failure.
- [interpretedSyntax](interpretedsyntax-swift.property.md) — The syntax for interpreting a Markdown string.
- [InterpretedSyntax](interpretedsyntax-swift.enum.md) — A type that represents the syntax for interpreting a Markdown string.
- [languageCode](languagecode.md) — The language code for this document.
