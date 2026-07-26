---
title: 'tableView(_:moveRowAt:to:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdatasource/tableview(_:moverowat:to:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdatasource/tableview(_:moverowat:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdatasource/tableview%28_%3Amoverowat%3Ato%3A%29.json'
content_hash: 'sha256:e798f7dc91abd247'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDataSource](../uitableviewdatasource.md)

# tableView(_:moveRowAt:to:)

<sub>Instance Method</sub>

Tells the data source to move a row at a specific location in the table view to another location.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, moveRowAt sourceIndexPath: IndexPath, to destinationIndexPath: IndexPath)
```

## Parameters

- `tableView` — The table-view object requesting this action.

- `sourceIndexPath` — An index path locating the row to be moved in `tableView`.

- `destinationIndexPath` — An index path locating the row in `tableView` that’s the destination of the move.

## Discussion

The [UITableView](../uitableview.md) object sends this message to the data source when the user presses the reorder control in the row at `sourceIndexPath`.

## See Also

### Related Documentation

- [- tableView:commitEditingStyle:forRowAtIndexPath:](<tableview(__commit_forrowat_).md>) — Asks the data source to commit the insertion or deletion of a specified row.

### Reordering table rows

- [- tableView:canMoveRowAtIndexPath:](<tableview(__canmoverowat_).md>) — Asks the data source whether a given row can move to another location in the table view.
