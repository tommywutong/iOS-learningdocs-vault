---
title: NSAttributedStringMarkdownSourcePosition
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstringmarkdownsourceposition
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstringmarkdownsourceposition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstringmarkdownsourceposition.json'
content_hash: 'sha256:030b24abe0456b00'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSAttributedStringMarkdownSourcePosition

<sub>Class</sub>

The position of attributed string text in its original Markdown source string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@interface NSAttributedStringMarkdownSourcePosition : NSObject
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [NSCopying](nscopying.md), [NSSecureCoding](nssecurecoding.md)

## Topics

### Creating an Attributed String Markdown Source Position Instance

- [initWithStartLine:startColumn:endLine:endColumn:](nsattributedstringmarkdownsourceposition/initwithstartline_startcolumn_endline_endcolumn_.md) — Creates a Markdown source position instance from its start and end line and column.

### Getting Markdown Source Position Properties

- [startLine](nsattributedstringmarkdownsourceposition/startline.md) — The line where the text begins in the Markdown source.
- [startColumn](nsattributedstringmarkdownsourceposition/startcolumn.md) — The column where the text begins in the Markdown source.
- [endLine](nsattributedstringmarkdownsourceposition/endline.md) — The line where the text ends in the Markdown source.
- [endColumn](nsattributedstringmarkdownsourceposition/endcolumn.md) — The column where the text ends in the Markdown source.

### Getting a Range from a Markdown Source Position Attribute

- [rangeInString:](nsattributedstringmarkdownsourceposition/rangeinstring_.md) — Returns a range indicating the source portion within a Markdown string.

## See Also

### Representing markdown attributes

- [InlinePresentationIntent](inlinepresentationintent.md) — A type that defines presentation intent for runs of characters for traits like emphasis, strikethrough, and code voice.
- [NSPresentationIntent](nspresentationintent.md) — A type that contains the Markdown formatting for blocks of text, like paragraphs, lists, code blocks, and parts of tables.
- [NSPresentationIntentKind](nspresentationintentkind.md) — An enumeration of intended display styles for blocks of text like paragraphs, lists, and code blocks.
- [NSPresentationIntentTableColumnAlignment](nspresentationintenttablecolumnalignment.md) — An enumeration of values for aligning the contents of table columns.
