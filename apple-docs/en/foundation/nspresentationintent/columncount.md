---
title: columnCount
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nspresentationintent/columncount
source_url: 'https://developer.apple.com/documentation/foundation/nspresentationintent/columncount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspresentationintent/columncount.json'
content_hash: 'sha256:db1cb9ef5d5198f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPresentationIntent](../nspresentationintent.md)

# columnCount

<sub>Instance Property</sub>

The number of columns in a table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (readonly) NSInteger columnCount;
```

## Discussion

If the intent is not a table, the value of this property is `0`.

## See Also

### Getting table information

- [row](row.md) — The row number to which this cell belongs.
- [column](column.md) — The column number to which the cell belongs.
- [columnAlignments](columnalignments.md) — The alignments for the columns in a table.
