---
title: 'buildExpression(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tablecolumnbuilder/buildexpression(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tablecolumnbuilder/buildexpression(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablecolumnbuilder/buildexpression%28_%3A%29.json'
content_hash: 'sha256:0aa294e04805ec6f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TableColumnBuilder](../tablecolumnbuilder.md)

# buildExpression(_:)

<sub>Type Method</sub>

Creates a generic, unsortable single column expression.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) static func buildExpression<Column>(_ column: Column) -> Column where RowValue == Column.TableRowValue, Column : TableColumnContent, Column.TableColumnSortComparator == Never
```

## See Also

### Building a column

- [buildBlock(_:)](<buildblock(__).md>) — Creates a single, unsortable column result.
- [buildBlock(_:_:)](<buildblock(____).md>) — Creates an unsortable column result from two sources.
- [buildBlock(_:_:_:)](<buildblock(______).md>) — Creates an unsortable column result from three sources.
- [buildBlock(_:_:_:_:)](<buildblock(________).md>) — Creates an unsortable column result from four sources.
- [buildBlock(_:_:_:_:_:)](<buildblock(__________).md>) — Creates an unsortable column result from five sources.
- [buildBlock(_:_:_:_:_:_:)](<buildblock(____________).md>) — Creates an unsortable column result from six sources.
- [buildBlock(_:_:_:_:_:_:_:)](<buildblock(______________).md>) — Creates an unsortable column result from seven sources.
- [buildBlock(_:_:_:_:_:_:_:_:)](<buildblock(________________).md>) — Creates an unsortable column result from eight sources.
- [buildBlock(_:_:_:_:_:_:_:_:_:)](<buildblock(__________________).md>) — Creates an unsortable column result from nine sources.
- [buildBlock(_:_:_:_:_:_:_:_:_:_:)](<buildblock(____________________).md>) — Creates an unsortable column result from ten sources.
