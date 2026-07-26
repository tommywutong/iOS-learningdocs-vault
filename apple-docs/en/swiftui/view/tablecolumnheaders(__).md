---
title: 'tableColumnHeaders(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/tablecolumnheaders(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/tablecolumnheaders(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/tablecolumnheaders%28_%3A%29.json'
content_hash: 'sha256:43ffc45ca2c60a70'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# tableColumnHeaders(_:)

<sub>Instance Method</sub>

Controls the visibility of a `Table`’s column header views.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func tableColumnHeaders(_ visibility: Visibility) -> some View

```

## Parameters

- `visibility` — A value of `visible` will show table columns, `hidden` will remove them, and `automatic` will defer to default behavior.

## Discussion

By default, `Table` will display a global header view with the labels of each table column. This area is also where users can sort, resize, and rearrange the columns. For simple cases that don’t require those features, this header can be hidden.

This will not affect the header of any `Section`s in a table.

```swift
Table(article.authors) {
    TableColumn("Name", value: \.name)
    TableColumn("Title", value: \.title)
}
.tableColumnHeaders(.hidden)
```

## See Also

### Customizing columns

- [TableColumnCustomization](../tablecolumncustomization.md) — A representation of the state of the columns in a table.
- [TableColumnCustomizationBehavior](../tablecolumncustomizationbehavior.md) — A set of customization behaviors of a column that a table can offer to a user.
