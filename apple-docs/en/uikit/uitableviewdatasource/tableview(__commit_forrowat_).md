---
title: 'tableView(_:commit:forRowAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdatasource/tableview(_:commit:forrowat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdatasource/tableview(_:commit:forrowat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdatasource/tableview%28_%3Acommit%3Aforrowat%3A%29.json'
content_hash: 'sha256:e0fe5c4e503c1c0c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDataSource](../uitableviewdatasource.md)

# tableView(_:commit:forRowAt:)

<sub>Instance Method</sub>

Asks the data source to commit the insertion or deletion of a specified row.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, commit editingStyle: UITableViewCell.EditingStyle, forRowAt indexPath: IndexPath)
```

## Parameters

- `tableView` — The table-view object requesting the insertion or deletion.

- `editingStyle` — The cell editing style corresponding to a insertion or deletion requested for the row specified by `indexPath`. Possible editing styles are [UITableViewCellEditingStyleInsert](../uitableviewcell/editingstyle-swift.enum/insert.md) or [UITableViewCellEditingStyleDelete](../uitableviewcell/editingstyle-swift.enum/delete.md).

- `indexPath` — An index path locating the row in `tableView`.

## Discussion

When users tap the insertion (green plus) control or Delete button associated with a [UITableViewCell](../uitableviewcell.md) object in the table view, the table view sends this message to the data source, asking it to commit the change. (If the user taps the deletion (red minus) control, the table view then displays the Delete button to get confirmation.) The data source commits the insertion or deletion by invoking the `UITableView` methods [- insertRowsAtIndexPaths:withRowAnimation:](<../uitableview/insertrows(at_with_).md>) or [- deleteRowsAtIndexPaths:withRowAnimation:](<../uitableview/deleterows(at_with_).md>), as appropriate.

To enable the swipe-to-delete feature of table views (wherein a user swipes horizontally across a row to display a Delete button), you must implement this method.

You shouldn’t call [- setEditing:animated:](<../uitableview/setediting(__animated_).md>) within an implementation of this method. If for some reason you must, invoke it after a delay by using the [perform(_:with:afterDelay:)](<../../objectivec/nsobject-swift.class/perform(__with_afterdelay_).md>) method.

## See Also

### Inserting or deleting table rows

- [- tableView:canEditRowAtIndexPath:](<tableview(__caneditrowat_).md>) — Asks the data source to verify that the given row is editable.
