---
title: row
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nspresentationintent/row
source_url: 'https://developer.apple.com/documentation/foundation/nspresentationintent/row'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspresentationintent/row.json'
content_hash: 'sha256:b1cb15cfb183ab67'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPresentationIntent](../nspresentationintent.md)

# row

<sub>Instance Property</sub>

The row number to which this cell belongs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (readonly) NSInteger row;
```

## Discussion

The value of this property is `0`-based, with the first row at `0`, the second row at `1`, and so on. If The intent is not a cell, this value is `0`.

## See Also

### Getting table information

- [column](column.md) — The column number to which the cell belongs.
- [columnCount](columncount.md) — The number of columns in a table.
- [columnAlignments](columnalignments.md) — The alignments for the columns in a table.
