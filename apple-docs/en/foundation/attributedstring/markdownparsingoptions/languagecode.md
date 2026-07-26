---
title: languageCode
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributedstring/markdownparsingoptions/languagecode
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/markdownparsingoptions/languagecode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/markdownparsingoptions/languagecode.json'
content_hash: 'sha256:937b050dbaeac1df'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [AttributedString](../../attributedstring.md) · [MarkdownParsingOptions](../markdownparsingoptions.md)

# languageCode

<sub>Instance Property</sub>

The language code for this document.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var languageCode: String?
```

## Discussion

This value is a [BCP-47](https://tools.ietf.org/search/bcp47) language code. If not `nil`, the string applies the [NSLanguageIdentifierAttributeName](../../nsattributedstring/key/languageidentifier.md) attribute to any range in the returned string that doesn’t otherwise specify a language attribute. The default is `nil`, which applies no attributes.

## See Also

### Accessing Options

- [allowsExtendedAttributes](allowsextendedattributes.md) — A Boolean value that indicates whether parsing allows extensions to Markdown that specify extended attributes.
- [appliesSourcePositionAttributes](appliessourcepositionattributes.md) — A Boolean value that indicates whether parsing applies attributes that indicate the position of attributed text in the original Markdown string.
- [failurePolicy](failurepolicy-swift.property.md) — The policy for handling a parsing failure.
- [FailurePolicy](failurepolicy-swift.enum.md) — A type that represents policies for handling parsing failures.
- [interpretedSyntax](interpretedsyntax-swift.property.md) — The syntax for interpreting a Markdown string.
- [InterpretedSyntax](interpretedsyntax-swift.enum.md) — A type that represents the syntax for interpreting a Markdown string.
