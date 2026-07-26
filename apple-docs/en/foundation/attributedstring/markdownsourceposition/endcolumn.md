---
title: endColumn
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributedstring/markdownsourceposition/endcolumn
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/markdownsourceposition/endcolumn'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/markdownsourceposition/endcolumn.json'
content_hash: 'sha256:30a0e8f2fedc7574'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [AttributedString](../../attributedstring.md) · [MarkdownSourcePosition](../markdownsourceposition.md)

# endColumn

<sub>Instance Property</sub>

The column where the text ends in the Markdown source.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let endColumn: Int
```

## Discussion

This property uses `1`-based counting. Columns represent UTF-8 indices; for multi-byte characters, the column indicates the first byte.

## See Also

### Inspecting Markdown Source Position Properties

- [startLine](startline.md) — The line where the text begins in the Markdown source.
- [startColumn](startcolumn.md) — The column where the text begins in the Markdown source.
- [endLine](endline.md) — The line where the text ends in the Markdown source.
