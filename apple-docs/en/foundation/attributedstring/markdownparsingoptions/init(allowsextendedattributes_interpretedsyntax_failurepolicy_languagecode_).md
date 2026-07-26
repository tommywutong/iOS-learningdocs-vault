---
title: 'init(allowsExtendedAttributes:interpretedSyntax:failurePolicy:languageCode:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/markdownparsingoptions/init(allowsextendedattributes:interpretedsyntax:failurepolicy:languagecode:)'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/markdownparsingoptions/init(allowsextendedattributes:interpretedsyntax:failurepolicy:languagecode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/markdownparsingoptions/init%28allowsextendedattributes%3Ainterpretedsyntax%3Afailurepolicy%3Alanguagecode%3A%29.json'
content_hash: 'sha256:cc8062f091ebcd44'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [AttributedString](../../attributedstring.md) · [MarkdownParsingOptions](../markdownparsingoptions.md)

# init(allowsExtendedAttributes:interpretedSyntax:failurePolicy:languageCode:)

<sub>Initializer</sub>

Creates a Markdown parsing options instance with the specified values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(allowsExtendedAttributes: Bool = false, interpretedSyntax: AttributedString.MarkdownParsingOptions.InterpretedSyntax = .full, failurePolicy: AttributedString.MarkdownParsingOptions.FailurePolicy = .throwError, languageCode: String? = nil)
```

## Parameters

- `allowsExtendedAttributes` — A Boolean value that indicates whether parsing allows extensions to Markdown that specify extended attributes.

- `interpretedSyntax` — The syntax for intepreting a Markdown string.

- `failurePolicy` — The policy for handling a parsing failure.

- `languageCode` — The [BCP-47](https://tools.ietf.org/search/bcp47) language code for this document.

## See Also

### Creating Markdown Parsing Options

- [init(allowsExtendedAttributes:interpretedSyntax:failurePolicy:languageCode:appliesSourcePositionAttributes:)](<init(allowsextendedattributes_interpretedsyntax_failurepolicy_languagecode_appliessourcepositionattributes_).md>) — Creates a Markdown parsing options instance with the specified values, optionally marking the source position of attributed text.
