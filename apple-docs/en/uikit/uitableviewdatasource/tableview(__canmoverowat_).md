---
title: 'tableView(_:canMoveRowAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdatasource/tableview(_:canmoverowat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdatasource/tableview(_:canmoverowat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdatasource/tableview%28_%3Acanmoverowat%3A%29.json'
content_hash: 'sha256:3f5d14f61dce8bcf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDataSource](../uitableviewdatasource.md)

# tableView(_:canMoveRowAt:)

<sub>Instance Method</sub>

Asks the data source whether a given row can move to another location in the table view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, canMoveRowAt indexPath: IndexPath) -> Bool
```

## Parameters

- `tableView` — The table-view object requesting this information.

- `indexPath` — An index path locating a row in `tableView`.

## Return Value

[true](../../swift/true.md) if the row can be moved; otherwise, [false](../../swift/false.md).

## Discussion

This method allows the data source to specify that the reordering control for the specified row not be shown. By default, the reordering control is shown if the data source implements the [- tableView:moveRowAtIndexPath:toIndexPath:](<tableview(__moverowat_to_).md>) method.

## See Also

### Reordering table rows

- [- tableView:moveRowAtIndexPath:toIndexPath:](<tableview(__moverowat_to_).md>) — Tells the data source to move a row at a specific location in the table view to another location.
