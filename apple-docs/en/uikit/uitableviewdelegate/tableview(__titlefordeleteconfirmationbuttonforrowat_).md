---
title: 'tableView(_:titleForDeleteConfirmationButtonForRowAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdelegate/tableview(_:titlefordeleteconfirmationbuttonforrowat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:titlefordeleteconfirmationbuttonforrowat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%28_%3Atitlefordeleteconfirmationbuttonforrowat%3A%29.json'
content_hash: 'sha256:fb73afe06bd30b3a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView(_:titleForDeleteConfirmationButtonForRowAt:)

<sub>Instance Method</sub>

Changes the default title of the delete-confirmation button.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, titleForDeleteConfirmationButtonForRowAt indexPath: IndexPath) -> String?
```

## Parameters

- `tableView` — The table view requesting this information.

- `indexPath` — An index path locating the row in its section.

## Return Value

A localized string to used as the title of the delete-confirmation button.

## Discussion

By default, the delete-confirmation button, which appears on the right side of the cell, has the title of “Delete”. The table view displays this button when the user attempts to delete a row, either by swiping the row or tapping the red minus icon in editing mode. You can implement this method to return an alternative title, which should be localized.

## See Also

### Editing table rows

- [- tableView:willBeginEditingRowAtIndexPath:](<tableview(__willbegineditingrowat_).md>) — Tells the delegate that the table view is about to go into editing mode.
- [- tableView:didEndEditingRowAtIndexPath:](<tableview(__didendeditingrowat_).md>) — Tells the delegate that the table view has left editing mode.
- [- tableView:editingStyleForRowAtIndexPath:](<tableview(__editingstyleforrowat_).md>) — Asks the delegate for the editing style of a row at a particular location in a table view.
- [- tableView:shouldIndentWhileEditingRowAtIndexPath:](<tableview(__shouldindentwhileeditingrowat_).md>) — Asks the delegate whether the background of the specified row should be indented while the table view is in editing mode.
