---
title: interpretedSyntax
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributedstring/markdownparsingoptions/interpretedsyntax-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/markdownparsingoptions/interpretedsyntax-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/markdownparsingoptions/interpretedsyntax-swift.property.json'
content_hash: 'sha256:d8794c2ebab09fe3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [AttributedString](../../attributedstring.md) · [MarkdownParsingOptions](../markdownparsingoptions.md)

# interpretedSyntax

<sub>Instance Property</sub>

The syntax for interpreting a Markdown string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var interpretedSyntax: AttributedString.MarkdownParsingOptions.InterpretedSyntax
```

## Discussion

If your Markdown data uses syntax that this setting excludes, the parser still parses it and includes its text in the final result. However, the relevant text won’t have attributes.

## See Also

### Accessing Options

- [allowsExtendedAttributes](allowsextendedattributes.md) — A Boolean value that indicates whether parsing allows extensions to Markdown that specify extended attributes.
- [appliesSourcePositionAttributes](appliessourcepositionattributes.md) — A Boolean value that indicates whether parsing applies attributes that indicate the position of attributed text in the original Markdown string.
- [failurePolicy](failurepolicy-swift.property.md) — The policy for handling a parsing failure.
- [FailurePolicy](failurepolicy-swift.enum.md) — A type that represents policies for handling parsing failures.
- [InterpretedSyntax](interpretedsyntax-swift.enum.md) — A type that represents the syntax for interpreting a Markdown string.
- [languageCode](languagecode.md) — The language code for this document.
