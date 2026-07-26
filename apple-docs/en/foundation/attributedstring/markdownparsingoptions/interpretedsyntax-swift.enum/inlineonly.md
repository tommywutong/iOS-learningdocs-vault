---
title: AttributedString.MarkdownParsingOptions.InterpretedSyntax.inlineOnly
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributedstring/markdownparsingoptions/interpretedsyntax-swift.enum/inlineonly
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/markdownparsingoptions/interpretedsyntax-swift.enum/inlineonly'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/markdownparsingoptions/interpretedsyntax-swift.enum/inlineonly.json'
content_hash: 'sha256:b8516539394c2acb'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [AttributedString](../../../attributedstring.md) · [MarkdownParsingOptions](../../markdownparsingoptions.md) · [InterpretedSyntax](../interpretedsyntax-swift.enum.md)

# AttributedString.MarkdownParsingOptions.InterpretedSyntax.inlineOnly

<sub>Case</sub>

A syntax value that parses all Markdown text, but interprets only attributes that apply to inline spans.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case inlineOnly
```

## Discussion

With this syntax, the parser doesn’t apply attributes that differentiate blocks. However, extended attributes apply to inline spans, so the parser includes them, if the [allowsExtendedAttributes](../allowsextendedattributes.md) property allows them.

## See Also

### Syntax Values

- [AttributedString.MarkdownParsingOptions.InterpretedSyntax.full](full.md) — A syntax value that interprets the full Markdown syntax and produces all relevant attributes.
- [AttributedString.MarkdownParsingOptions.InterpretedSyntax.inlineOnlyPreservingWhitespace](inlineonlypreservingwhitespace.md) — A syntax value that parses all Markdown text, but interprets only attributes that apply to inline spans, preserving white space.
