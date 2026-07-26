---
title: startColumn
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributedstring/markdownsourceposition/startcolumn
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/markdownsourceposition/startcolumn'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/markdownsourceposition/startcolumn.json'
content_hash: 'sha256:9210e2ff3555c26e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [AttributedString](../../attributedstring.md) · [MarkdownSourcePosition](../markdownsourceposition.md)

# startColumn

<sub>Instance Property</sub>

The column where the text begins in the Markdown source.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let startColumn: Int
```

## Discussion

This property uses `1`-based counting. Columns represent UTF-8 indices; for multi-byte characters, the column indicates the first byte.

## See Also

### Inspecting Markdown Source Position Properties

- [startLine](startline.md) — The line where the text begins in the Markdown source.
- [endLine](endline.md) — The line where the text ends in the Markdown source.
- [endColumn](endcolumn.md) — The column where the text ends in the Markdown source.
