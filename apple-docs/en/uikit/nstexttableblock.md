---
title: NSTextTableBlock
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstexttableblock
source_url: 'https://developer.apple.com/documentation/uikit/nstexttableblock'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstexttableblock.json'
content_hash: 'sha256:648d88670d07728e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSTextTableBlock

<sub>Class</sub>

A text block that represents a single cell in a text table.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class NSTextTableBlock
```

## Overview

`NSTextTableBlock` is a subclass of [NSTextBlock](nstextblock.md) that places a paragraph in a cell of an [NSTextTable](nstexttable.md). When you create an `NSTextTableBlock`, you specify the table it belongs to, the cell’s starting row and column, and how many rows and columns the cell spans.

To build a table, create an [NSTextTable](nstexttable.md), then create an `NSTextTableBlock` for each cell. Assign each block to a paragraph by setting [textBlocks](nsparagraphstyle/textblocks.md) on an [NSMutableParagraphStyle](nsmutableparagraphstyle.md) and applying that style to the paragraph’s range in your attributed string.

## Relationships

- **Inherits From**: [NSTextBlock](nstextblock.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a text table block

- [- initWithTable:startingRow:rowSpan:startingColumn:columnSpan:](<nstexttableblock/init(table_startingrow_rowspan_startingcolumn_columnspan_).md>)
- [- initWithCoder:](<nstexttableblock/init(coder_).md>)

### Accessing the parent table

- [table](nstexttableblock/table.md)

### Accessing cell position

- [startingRow](nstexttableblock/startingrow.md)
- [rowSpan](nstexttableblock/rowspan.md)
- [startingColumn](nstexttableblock/startingcolumn.md)
- [columnSpan](nstexttableblock/columnspan.md)

## See Also

### Tables

- [Adding tables to attributed strings in UIKit](adding-tables-to-attributed-strings.md) — Create and configure tables in attributed strings and display them in a text view.
- [NSTextTable](nstexttable.md) — An object that represents a table of rows and columns in an attributed string.
- [NSTextBlock](nstextblock.md) — An object that defines the size, spacing, and appearance of a block of text in an attributed string.
