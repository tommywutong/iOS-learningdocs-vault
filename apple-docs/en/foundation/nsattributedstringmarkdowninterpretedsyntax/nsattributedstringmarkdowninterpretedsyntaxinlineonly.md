---
title: NSAttributedStringMarkdownInterpretedSyntaxInlineOnly
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstringmarkdowninterpretedsyntax/nsattributedstringmarkdowninterpretedsyntaxinlineonly
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstringmarkdowninterpretedsyntax/nsattributedstringmarkdowninterpretedsyntaxinlineonly'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstringmarkdowninterpretedsyntax/nsattributedstringmarkdowninterpretedsyntaxinlineonly.json'
content_hash: 'sha256:d63c674d6522f4c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedStringMarkdownInterpretedSyntax](../nsattributedstringmarkdowninterpretedsyntax.md)

# NSAttributedStringMarkdownInterpretedSyntaxInlineOnly

<sub>Enumeration Case</sub>

A syntax value that parses all Markdown text, but interprets only attributes that apply to inline spans.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
NSAttributedStringMarkdownInterpretedSyntaxInlineOnly
```

## Discussion

With this syntax, the parser doesn’t apply attributes that differentiate blocks, like [NSPresentationIntentAttributeName](../nsattributedstring/key/presentationintentattributename.md). However, extended attributes apply to inline spans, so the parser includes them, if the [allowsExtendedAttributes](../nsattributedstringmarkdownparsingoptions/allowsextendedattributes.md) property allows them.

## See Also

### Syntax Values

- [NSAttributedStringMarkdownInterpretedSyntaxFull](nsattributedstringmarkdowninterpretedsyntaxfull.md) — A syntax value that interprets the full Markdown syntax and produces all relevant attributes.
- [NSAttributedStringMarkdownInterpretedSyntaxInlineOnlyPreservingWhitespace](nsattributedstringmarkdowninterpretedsyntaxinlineonlypreservingwhitespace.md) — A syntax value that parses all Markdown text, but interprets only attributes that apply to inline spans, perserving white space.
