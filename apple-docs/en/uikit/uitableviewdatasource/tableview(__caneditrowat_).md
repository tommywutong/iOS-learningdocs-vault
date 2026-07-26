---
title: 'tableView(_:canEditRowAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdatasource/tableview(_:caneditrowat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdatasource/tableview(_:caneditrowat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdatasource/tableview%28_%3Acaneditrowat%3A%29.json'
content_hash: 'sha256:4754bda96d52821c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDataSource](../uitableviewdatasource.md)

# tableView(_:canEditRowAt:)

<sub>Instance Method</sub>

Asks the data source to verify that the given row is editable.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, canEditRowAt indexPath: IndexPath) -> Bool
```

## Parameters

- `tableView` — The table-view object requesting this information.

- `indexPath` — An index path locating a row in `tableView`.

## Return Value

[true](../../swift/true.md) if the row indicated by `indexPath` is editable; otherwise, [false](../../swift/false.md).

## Discussion

The method permits the data source to exclude individual rows from being treated as editable. Editable rows display the insertion or deletion control in their cells. If this method isn’t implemented, all rows are assumed to be editable. Rows that aren’t editable ignore the [editingStyle](../uitableviewcell/editingstyle-swift.property.md) property of a `UITableViewCell` object and do no indentation for the deletion or insertion control. Rows that are editable, but that don’t want to have an insertion or remove control shown, can return [UITableViewCellEditingStyleNone](../uitableviewcell/editingstyle-swift.enum/none.md) from the [- tableView:editingStyleForRowAtIndexPath:](<../uitableviewdelegate/tableview(__editingstyleforrowat_).md>) delegate method.

## See Also

### Inserting or deleting table rows

- [- tableView:commitEditingStyle:forRowAtIndexPath:](<tableview(__commit_forrowat_).md>) — Asks the data source to commit the insertion or deletion of a specified row.
