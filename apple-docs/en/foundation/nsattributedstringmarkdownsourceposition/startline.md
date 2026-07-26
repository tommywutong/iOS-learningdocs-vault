---
title: startLine
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstringmarkdownsourceposition/startline
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstringmarkdownsourceposition/startline'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstringmarkdownsourceposition/startline.json'
content_hash: 'sha256:bc09069af3277a9d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedStringMarkdownSourcePosition](../nsattributedstringmarkdownsourceposition.md)

# startLine

<sub>Instance Property</sub>

The line where the text begins in the Markdown source.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (readonly) NSInteger startLine;
```

## Discussion

This property uses `1`-based counting.

## See Also

### Getting Markdown Source Position Properties

- [startColumn](startcolumn.md) — The column where the text begins in the Markdown source.
- [endLine](endline.md) — The line where the text ends in the Markdown source.
- [endColumn](endcolumn.md) — The column where the text ends in the Markdown source.
