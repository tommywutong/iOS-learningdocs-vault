---
title: TupleTableColumnContent
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tupletablecolumncontent
source_url: 'https://developer.apple.com/documentation/swiftui/tupletablecolumncontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tupletablecolumncontent.json'
content_hash: 'sha256:6beade65aa00d837'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TupleTableColumnContent

<sub>Structure</sub>

A type of table column content that creates table columns created from a Swift tuple of table columns.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@frozen nonisolated struct TupleTableColumnContent<RowValue, Sort, T> where RowValue : Identifiable, Sort : SortComparator
```

## Overview

Don’t use this type directly; instead, SwiftUI uses this type as the return value from the various `buildBlock` methods in [TableColumnBuilder](tablecolumnbuilder.md). The size of the tuple corresponds to how many columns you create in the `columns` closure you provide to the [Table](table.md) initializer.

## Relationships

- **Conforms To**: [TableColumnContent](tablecolumncontent.md)

## Topics

### Accessing the value

- [value](tupletablecolumncontent/value.md) — The value of a row presented by this column content.
