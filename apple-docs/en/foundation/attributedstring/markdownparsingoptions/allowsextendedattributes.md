---
title: allowsExtendedAttributes
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributedstring/markdownparsingoptions/allowsextendedattributes
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/markdownparsingoptions/allowsextendedattributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/markdownparsingoptions/allowsextendedattributes.json'
content_hash: 'sha256:e2de5a84134b4a81'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [AttributedString](../../attributedstring.md) · [MarkdownParsingOptions](../markdownparsingoptions.md)

# allowsExtendedAttributes

<sub>Instance Property</sub>

A Boolean value that indicates whether parsing allows extensions to Markdown that specify extended attributes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var allowsExtendedAttributes: Bool
```

## Discussion

If this value is `false`, the Markdown parser supports only the CommonMark syntax. The default is `false`.

## See Also

### Accessing Options

- [appliesSourcePositionAttributes](appliessourcepositionattributes.md) — A Boolean value that indicates whether parsing applies attributes that indicate the position of attributed text in the original Markdown string.
- [failurePolicy](failurepolicy-swift.property.md) — The policy for handling a parsing failure.
- [FailurePolicy](failurepolicy-swift.enum.md) — A type that represents policies for handling parsing failures.
- [interpretedSyntax](interpretedsyntax-swift.property.md) — The syntax for interpreting a Markdown string.
- [InterpretedSyntax](interpretedsyntax-swift.enum.md) — A type that represents the syntax for interpreting a Markdown string.
- [languageCode](languagecode.md) — The language code for this document.
