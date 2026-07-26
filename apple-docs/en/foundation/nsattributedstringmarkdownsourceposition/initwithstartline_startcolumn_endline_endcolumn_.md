---
title: 'initWithStartLine:startColumn:endLine:endColumn:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstringmarkdownsourceposition/initwithstartline:startcolumn:endline:endcolumn:'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstringmarkdownsourceposition/initwithstartline:startcolumn:endline:endcolumn:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstringmarkdownsourceposition/initwithstartline%3Astartcolumn%3Aendline%3Aendcolumn%3A.json'
content_hash: 'sha256:a8ed1edf3a5df3d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedStringMarkdownSourcePosition](../nsattributedstringmarkdownsourceposition.md)

# initWithStartLine:startColumn:endLine:endColumn:

<sub>Instance Method</sub>

Creates a Markdown source position instance from its start and end line and column.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (instancetype) initWithStartLine:(NSInteger) startLine startColumn:(NSInteger) startColumn endLine:(NSInteger) endLine endColumn:(NSInteger) endColumn;
```

## Parameters

- `startLine` — The line number where text begins in the Markdown source. Specify a 1-based number. For example, the number for the first row is 1, for the second row is 2, and so on.

- `startColumn` — The column number where text begins in the Markdown source. Specify a 1-based number. For example, the number for the first column is 1, for the second column is 2, and so on. Columns represent UTF-8 indices; for multi-byte characters, the column indicates the first byte.

- `endLine` — The line number where the Markdown source ends. Specify a 1-based number.

- `endColumn` — The column number where the Markdown source ends. Specify a 1-based number.
