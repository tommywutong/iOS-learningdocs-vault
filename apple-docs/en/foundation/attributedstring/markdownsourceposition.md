---
title: AttributedString.MarkdownSourcePosition
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributedstring/markdownsourceposition
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/markdownsourceposition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/markdownsourceposition.json'
content_hash: 'sha256:ad5da23ad3611950'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# AttributedString.MarkdownSourcePosition

<sub>Structure</sub>

The position of attributed string text in its original Markdown source string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MarkdownSourcePosition
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a Markdown Source Position

- [init(startLine:startColumn:endLine:endColumn:)](<markdownsourceposition/init(startline_startcolumn_endline_endcolumn_).md>) — Creates a Markdown source position instance from its start and end line and column.

### Inspecting Markdown Source Position Properties

- [startLine](markdownsourceposition/startline.md) — The line where the text begins in the Markdown source.
- [startColumn](markdownsourceposition/startcolumn.md) — The column where the text begins in the Markdown source.
- [endLine](markdownsourceposition/endline.md) — The line where the text ends in the Markdown source.
- [endColumn](markdownsourceposition/endcolumn.md) — The column where the text ends in the Markdown source.
