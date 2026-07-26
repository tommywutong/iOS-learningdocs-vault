---
title: AttributedString.MarkdownParsingOptions.InterpretedSyntax.inlineOnlyPreservingWhitespace
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributedstring/markdownparsingoptions/interpretedsyntax-swift.enum/inlineonlypreservingwhitespace
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/markdownparsingoptions/interpretedsyntax-swift.enum/inlineonlypreservingwhitespace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/markdownparsingoptions/interpretedsyntax-swift.enum/inlineonlypreservingwhitespace.json'
content_hash: 'sha256:70da23a347107c9c'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [AttributedString](../../../attributedstring.md) · [MarkdownParsingOptions](../../markdownparsingoptions.md) · [InterpretedSyntax](../interpretedsyntax-swift.enum.md)

# AttributedString.MarkdownParsingOptions.InterpretedSyntax.inlineOnlyPreservingWhitespace

<sub>Case</sub>

A syntax value that parses all Markdown text, but interprets only attributes that apply to inline spans, preserving white space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case inlineOnlyPreservingWhitespace
```

## Discussion

This value behaves like [AttributedString.MarkdownParsingOptions.InterpretedSyntax.inlineOnly](inlineonly.md), but doesn’t interpret multiple consecutive instances of white space as a single separator space. All whitespace characters appear in the result as the source specifies.

## See Also

### Syntax Values

- [AttributedString.MarkdownParsingOptions.InterpretedSyntax.full](full.md) — A syntax value that interprets the full Markdown syntax and produces all relevant attributes.
- [AttributedString.MarkdownParsingOptions.InterpretedSyntax.inlineOnly](inlineonly.md) — A syntax value that parses all Markdown text, but interprets only attributes that apply to inline spans.
