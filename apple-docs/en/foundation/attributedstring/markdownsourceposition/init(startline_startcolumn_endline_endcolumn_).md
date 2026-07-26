---
title: 'init(startLine:startColumn:endLine:endColumn:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/markdownsourceposition/init(startline:startcolumn:endline:endcolumn:)'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/markdownsourceposition/init(startline:startcolumn:endline:endcolumn:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/markdownsourceposition/init%28startline%3Astartcolumn%3Aendline%3Aendcolumn%3A%29.json'
content_hash: 'sha256:21f5ad8e0c691321'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [AttributedString](../../attributedstring.md) · [MarkdownSourcePosition](../markdownsourceposition.md)

# init(startLine:startColumn:endLine:endColumn:)

<sub>Initializer</sub>

Creates a Markdown source position instance from its start and end line and column.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(startLine: Int, startColumn: Int, endLine: Int, endColumn: Int)
```

## Parameters

- `startLine` — The line where the text begins in the Markdown source.

- `startColumn` — The column where the text begins in the Markdown source.

- `endLine` — The line where the text ends in the Markdown source.

- `endColumn` — The column where the text ends in the Markdown source.
