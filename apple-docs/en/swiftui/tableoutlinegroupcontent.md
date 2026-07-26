---
title: TableOutlineGroupContent
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tableoutlinegroupcontent
source_url: 'https://developer.apple.com/documentation/swiftui/tableoutlinegroupcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tableoutlinegroupcontent.json'
content_hash: 'sha256:7c50f3de454189a8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TableOutlineGroupContent

<sub>Structure</sub>

An opaque table row type created by a table’s hierarchical initializers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated struct TableOutlineGroupContent<Data> where Data : RandomAccessCollection, Data.Element : Identifiable
```

## Overview

This row content is created by `Table.init(_:,children:,...)` initializers as the table’s `Rows` generic type.

To explicitly create hierarchical rows, use [OutlineGroup](outlinegroup.md) instead.

## Relationships

- **Conforms To**: [TableRowContent](tablerowcontent.md)

## See Also

### Adding progressive disclosure

- [DisclosureTableRow](disclosuretablerow.md) — A kind of table row that shows or hides additional rows based on the state of a disclosure control.
