---
title: NSTextTable
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstexttable
source_url: 'https://developer.apple.com/documentation/uikit/nstexttable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstexttable.json'
content_hash: 'sha256:a31034ebe896243a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSTextTable

<sub>Class</sub>

An object that represents a table of rows and columns in an attributed string.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class NSTextTable
```

## Overview

`NSTextTable` is a subclass of [NSTextBlock](nstextblock.md) that represents a complete table. You can configure the number of columns, whether adjacent cell borders collapse into one, and whether empty cells are hidden.

Each cell is an [NSTextTableBlock](nstexttableblock.md) that specifies its row, column, and span within the table. You don’t add cells directly to the table — instead, you apply each cell’s block to a paragraph using [textBlocks](nsparagraphstyle/textblocks.md).

Choose between two layout algorithms using the [layoutAlgorithm](nstexttable/layoutalgorithm-swift.property.md) property:

- [NSTextTableLayoutAlgorithmAutomatic](nstexttable/layoutalgorithm-swift.enum/automatic.md) distributes column widths based on content, similar to the HTML `auto` table layout.
- [NSTextTableLayoutAlgorithmFixed](nstexttable/layoutalgorithm-swift.enum/fixed.md) distributes column widths based on explicit values set on the first row of cells, similar to the HTML `fixed` table layout.

## Relationships

- **Inherits From**: [NSTextBlock](nstextblock.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Configuring the table

- [numberOfColumns](nstexttable/numberofcolumns.md)
- [layoutAlgorithm](nstexttable/layoutalgorithm-swift.property.md)
- [collapsesBorders](nstexttable/collapsesborders.md)
- [hidesEmptyCells](nstexttable/hidesemptycells.md)
- [LayoutAlgorithm](nstexttable/layoutalgorithm-swift.enum.md)

## See Also

### Tables

- [Adding tables to attributed strings in UIKit](adding-tables-to-attributed-strings.md) — Create and configure tables in attributed strings and display them in a text view.
- [NSTextTableBlock](nstexttableblock.md) — A text block that represents a single cell in a text table.
- [NSTextBlock](nstextblock.md) — An object that defines the size, spacing, and appearance of a block of text in an attributed string.
