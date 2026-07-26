---
title: NSAttributedStringMarkdownInterpretedSyntaxInlineOnlyPreservingWhitespace
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstringmarkdowninterpretedsyntax/nsattributedstringmarkdowninterpretedsyntaxinlineonlypreservingwhitespace
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstringmarkdowninterpretedsyntax/nsattributedstringmarkdowninterpretedsyntaxinlineonlypreservingwhitespace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstringmarkdowninterpretedsyntax/nsattributedstringmarkdowninterpretedsyntaxinlineonlypreservingwhitespace.json'
content_hash: 'sha256:a8f606d8e88631af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedStringMarkdownInterpretedSyntax](../nsattributedstringmarkdowninterpretedsyntax.md)

# NSAttributedStringMarkdownInterpretedSyntaxInlineOnlyPreservingWhitespace

<sub>Enumeration Case</sub>

A syntax value that parses all Markdown text, but interprets only attributes that apply to inline spans, perserving white space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
NSAttributedStringMarkdownInterpretedSyntaxInlineOnlyPreservingWhitespace
```

## Discussion

This value behaves like [NSAttributedStringMarkdownInterpretedSyntaxInlineOnly](nsattributedstringmarkdowninterpretedsyntaxinlineonly.md), but doesn’t interpret multiple consecutive instances of white space as a single separator space. All whitespace characters appear in the result as the source specifies.

## See Also

### Syntax Values

- [NSAttributedStringMarkdownInterpretedSyntaxFull](nsattributedstringmarkdowninterpretedsyntaxfull.md) — A syntax value that interprets the full Markdown syntax and produces all relevant attributes.
- [NSAttributedStringMarkdownInterpretedSyntaxInlineOnly](nsattributedstringmarkdowninterpretedsyntaxinlineonly.md) — A syntax value that parses all Markdown text, but interprets only attributes that apply to inline spans.
