---
title: TableColumnAlignment
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tablecolumnalignment
source_url: 'https://developer.apple.com/documentation/swiftui/tablecolumnalignment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablecolumnalignment.json'
content_hash: 'sha256:af07e37b444dc707'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TableColumnAlignment

<sub>Structure</sub>

Describes the alignment of the content of a table column.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct TableColumnAlignment
```

## Overview

The alignment of a column applies to both its header label as well as the default alignment of its content view for each row.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the alignment

- [automatic](tablecolumnalignment/automatic.md) — The default column alignment.
- [leading](tablecolumnalignment/leading.md) — Leading column alignment.
- [center](tablecolumnalignment/center.md) — Center column alignment.
- [trailing](tablecolumnalignment/trailing.md) — Trailing column alignment.
- [numeric](tablecolumnalignment/numeric.md) — Column alignment appropriate for numeric content.
- [numeric(_:)](<tablecolumnalignment/numeric(__).md>) — Column alignment appropriate for numeric content.

## See Also

### Creating columns

- [TableColumn](tablecolumn.md) — A column that displays a view for each row in a table.
- [TableColumnContent](tablecolumncontent.md) — A type used to represent columns within a table.
- [TableColumnBuilder](tablecolumnbuilder.md) — A result builder that creates table column content from closures.
- [TableColumnForEach](tablecolumnforeach.md) — A structure that computes columns on demand from an underlying collection of identified data.
