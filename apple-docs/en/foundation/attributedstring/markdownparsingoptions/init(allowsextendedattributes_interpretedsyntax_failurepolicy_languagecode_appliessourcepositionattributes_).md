---
title: 'init(allowsExtendedAttributes:interpretedSyntax:failurePolicy:languageCode:appliesSourcePositionAttributes:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/markdownparsingoptions/init(allowsextendedattributes:interpretedsyntax:failurepolicy:languagecode:appliessourcepositionattributes:)'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/markdownparsingoptions/init(allowsextendedattributes:interpretedsyntax:failurepolicy:languagecode:appliessourcepositionattributes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/markdownparsingoptions/init%28allowsextendedattributes%3Ainterpretedsyntax%3Afailurepolicy%3Alanguagecode%3Aappliessourcepositionattributes%3A%29.json'
content_hash: 'sha256:834e9533a0e94016'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [AttributedString](../../attributedstring.md) · [MarkdownParsingOptions](../markdownparsingoptions.md)

# init(allowsExtendedAttributes:interpretedSyntax:failurePolicy:languageCode:appliesSourcePositionAttributes:)

<sub>Initializer</sub>

Creates a Markdown parsing options instance with the specified values, optionally marking the source position of attributed text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(allowsExtendedAttributes: Bool = false, interpretedSyntax: AttributedString.MarkdownParsingOptions.InterpretedSyntax = .full, failurePolicy: AttributedString.MarkdownParsingOptions.FailurePolicy = .throwError, languageCode: String? = nil, appliesSourcePositionAttributes: Bool = false)
```

## Parameters

- `allowsExtendedAttributes` — A Boolean value that indicates whether parsing allows extensions to Markdown that specify extended attributes.

- `interpretedSyntax` — The syntax for intepreting a Markdown string.

- `failurePolicy` — The policy for handling a parsing failure.

- `languageCode` — The [BCP-47](https://tools.ietf.org/search/bcp47) language code for this document.

- `appliesSourcePositionAttributes` — A Boolean value that indicates whether parsing applies attributes that indicate the position of attribute text in the original Markdown string. If this value is `true`, the resulting string may contain attributes of type [MarkdownSourcePositionAttribute](../../attributescopes/foundationattributes/markdownsourcepositionattribute.md).

## See Also

### Creating Markdown Parsing Options

- [init(allowsExtendedAttributes:interpretedSyntax:failurePolicy:languageCode:)](<init(allowsextendedattributes_interpretedsyntax_failurepolicy_languagecode_).md>) — Creates a Markdown parsing options instance with the specified values.
