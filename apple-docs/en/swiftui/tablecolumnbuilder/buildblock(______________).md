---
title: 'buildBlock(_:_:_:_:_:_:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tablecolumnbuilder/buildblock(_:_:_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tablecolumnbuilder/buildblock(_:_:_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablecolumnbuilder/buildblock%28_%3A_%3A_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:e8f17228b99b5d66'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TableColumnBuilder](../tablecolumnbuilder.md)

# buildBlock(_:_:_:_:_:_:_:)

<sub>Type Method</sub>

Creates an unsortable column result from seven sources.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(_ c0: C0, _ c1: C1, _ c2: C2, _ c3: C3, _ c4: C4, _ c5: C5, _ c6: C6) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4, C5, C6)> where RowValue == C0.TableRowValue, C0 : TableColumnContent, C1 : TableColumnContent, C2 : TableColumnContent, C3 : TableColumnContent, C4 : TableColumnContent, C5 : TableColumnContent, C6 : TableColumnContent, C0.TableColumnSortComparator == Never, C0.TableRowValue == C1.TableRowValue, C1.TableColumnSortComparator == Never, C1.TableRowValue == C2.TableRowValue, C2.TableColumnSortComparator == Never, C2.TableRowValue == C3.TableRowValue, C3.TableColumnSortComparator == Never, C3.TableRowValue == C4.TableRowValue, C4.TableColumnSortComparator == Never, C4.TableRowValue == C5.TableRowValue, C5.TableColumnSortComparator == Never, C5.TableRowValue == C6.TableRowValue, C6.TableColumnSortComparator == Never
```

## See Also

### Building a column

- [buildBlock(_:)](<buildblock(__).md>) — Creates a single, unsortable column result.
- [buildBlock(_:_:)](<buildblock(____).md>) — Creates an unsortable column result from two sources.
- [buildBlock(_:_:_:)](<buildblock(______).md>) — Creates an unsortable column result from three sources.
- [buildBlock(_:_:_:_:)](<buildblock(________).md>) — Creates an unsortable column result from four sources.
- [buildBlock(_:_:_:_:_:)](<buildblock(__________).md>) — Creates an unsortable column result from five sources.
- [buildBlock(_:_:_:_:_:_:)](<buildblock(____________).md>) — Creates an unsortable column result from six sources.
- [buildBlock(_:_:_:_:_:_:_:_:)](<buildblock(________________).md>) — Creates an unsortable column result from eight sources.
- [buildBlock(_:_:_:_:_:_:_:_:_:)](<buildblock(__________________).md>) — Creates an unsortable column result from nine sources.
- [buildBlock(_:_:_:_:_:_:_:_:_:_:)](<buildblock(____________________).md>) — Creates an unsortable column result from ten sources.
- [buildExpression(_:)](<buildexpression(__).md>) — Creates a generic, unsortable single column expression.
