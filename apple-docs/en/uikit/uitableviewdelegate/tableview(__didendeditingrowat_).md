---
title: 'tableView(_:didEndEditingRowAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdelegate/tableview(_:didendeditingrowat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:didendeditingrowat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%28_%3Adidendeditingrowat%3A%29.json'
content_hash: 'sha256:6523aa0bb59da565'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView(_:didEndEditingRowAt:)

<sub>Instance Method</sub>

Tells the delegate that the table view has left editing mode.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, didEndEditingRowAt indexPath: IndexPath?)
```

## Parameters

- `tableView` — The table view providing this information.

- `indexPath` — An index path locating the row in `tableView`.

## Discussion

This method is called when the table view exits editing mode after having been put into the mode by the user swiping across the row identified by `indexPath`. As a result, a Delete button appears in the row; however, in this “swipe to delete” mode the table view does not display any insertion, deletion, and reordering controls. When entering this “swipe to delete” editing mode, the table view sends a [- tableView:willBeginEditingRowAtIndexPath:](<tableview(__willbegineditingrowat_).md>) message to the delegate to allow it to adjust its user interface.

## See Also

### Editing table rows

- [- tableView:willBeginEditingRowAtIndexPath:](<tableview(__willbegineditingrowat_).md>) — Tells the delegate that the table view is about to go into editing mode.
- [- tableView:editingStyleForRowAtIndexPath:](<tableview(__editingstyleforrowat_).md>) — Asks the delegate for the editing style of a row at a particular location in a table view.
- [- tableView:titleForDeleteConfirmationButtonForRowAtIndexPath:](<tableview(__titlefordeleteconfirmationbuttonforrowat_).md>) — Changes the default title of the delete-confirmation button.
- [- tableView:shouldIndentWhileEditingRowAtIndexPath:](<tableview(__shouldindentwhileeditingrowat_).md>) — Asks the delegate whether the background of the specified row should be indented while the table view is in editing mode.
