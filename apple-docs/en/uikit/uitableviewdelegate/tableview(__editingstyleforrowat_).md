---
title: 'tableView(_:editingStyleForRowAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdelegate/tableview(_:editingstyleforrowat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:editingstyleforrowat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%28_%3Aeditingstyleforrowat%3A%29.json'
content_hash: 'sha256:b121908b5cfaa632'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView(_:editingStyleForRowAt:)

<sub>Instance Method</sub>

Asks the delegate for the editing style of a row at a particular location in a table view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, editingStyleForRowAt indexPath: IndexPath) -> UITableViewCell.EditingStyle
```

## Parameters

- `tableView` — The table view requesting this information.

- `indexPath` — An index path locating a row in `tableView`.

## Return Value

The editing style of the cell for the row identified by `indexPath`.

## Discussion

This method allows the delegate to customize the editing style of the cell located at`indexPath`. If the delegate does not implement this method and the `UITableViewCell` object is editable (that is, it has its [editing](../uitableviewcell/isediting.md) property set to [true](../../swift/true.md)), the cell has the [UITableViewCellEditingStyleDelete](../uitableviewcell/editingstyle-swift.enum/delete.md) style set for it.

## See Also

### Editing table rows

- [- tableView:willBeginEditingRowAtIndexPath:](<tableview(__willbegineditingrowat_).md>) — Tells the delegate that the table view is about to go into editing mode.
- [- tableView:didEndEditingRowAtIndexPath:](<tableview(__didendeditingrowat_).md>) — Tells the delegate that the table view has left editing mode.
- [- tableView:titleForDeleteConfirmationButtonForRowAtIndexPath:](<tableview(__titlefordeleteconfirmationbuttonforrowat_).md>) — Changes the default title of the delete-confirmation button.
- [- tableView:shouldIndentWhileEditingRowAtIndexPath:](<tableview(__shouldindentwhileeditingrowat_).md>) — Asks the delegate whether the background of the specified row should be indented while the table view is in editing mode.
