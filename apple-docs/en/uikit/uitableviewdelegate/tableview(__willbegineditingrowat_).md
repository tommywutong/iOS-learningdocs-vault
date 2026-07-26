---
title: 'tableView(_:willBeginEditingRowAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdelegate/tableview(_:willbegineditingrowat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:willbegineditingrowat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%28_%3Awillbegineditingrowat%3A%29.json'
content_hash: 'sha256:93f5df4d20404ead'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView(_:willBeginEditingRowAt:)

<sub>Instance Method</sub>

Tells the delegate that the table view is about to go into editing mode.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, willBeginEditingRowAt indexPath: IndexPath)
```

## Parameters

- `tableView` — The table view providing this information.

- `indexPath` — An index path locating the row in `tableView`.

## Discussion

This method is called when the user swipes horizontally across a row; as a consequence, the table view sets its [editing](../uitableview/isediting.md) property to [true](../../swift/true.md) (thereby entering editing mode) and displays a Delete button in the row identified by `indexPath`. In this “swipe to delete” mode the table view does not display any insertion, deletion, and reordering controls. This method gives the delegate an opportunity to adjust the application’s user interface to editing mode. When the table exits editing mode (for example, the user taps the Delete button), the table view calls [- tableView:didEndEditingRowAtIndexPath:](<tableview(__didendeditingrowat_).md>).

> [!note] Note
> A swipe motion across a cell does not cause the display of a Delete button unless the table view’s data source implements the [- tableView:commitEditingStyle:forRowAtIndexPath:](<../uitableviewdatasource/tableview(__commit_forrowat_).md>) method.

## See Also

### Editing table rows

- [- tableView:didEndEditingRowAtIndexPath:](<tableview(__didendeditingrowat_).md>) — Tells the delegate that the table view has left editing mode.
- [- tableView:editingStyleForRowAtIndexPath:](<tableview(__editingstyleforrowat_).md>) — Asks the delegate for the editing style of a row at a particular location in a table view.
- [- tableView:titleForDeleteConfirmationButtonForRowAtIndexPath:](<tableview(__titlefordeleteconfirmationbuttonforrowat_).md>) — Changes the default title of the delete-confirmation button.
- [- tableView:shouldIndentWhileEditingRowAtIndexPath:](<tableview(__shouldindentwhileeditingrowat_).md>) — Asks the delegate whether the background of the specified row should be indented while the table view is in editing mode.
