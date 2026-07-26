---
title: columnAlignments
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nspresentationintent/columnalignments
source_url: 'https://developer.apple.com/documentation/foundation/nspresentationintent/columnalignments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspresentationintent/columnalignments.json'
content_hash: 'sha256:9af782fb6cd3d320'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPresentationIntent](../nspresentationintent.md)

# columnAlignments

<sub>Instance Property</sub>

The alignments for the columns in a table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (readonly, nullable) NSArray<NSNumber *> * columnAlignments;
```

## Discussion

If the intent is not a table, the value of this property is `nil`.

## See Also

### Getting table information

- [row](row.md) — The row number to which this cell belongs.
- [column](column.md) — The column number to which the cell belongs.
- [columnCount](columncount.md) — The number of columns in a table.
