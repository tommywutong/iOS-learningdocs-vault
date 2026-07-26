---
title: 'tableView(_:shouldIndentWhileEditingRowAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdelegate/tableview(_:shouldindentwhileeditingrowat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:shouldindentwhileeditingrowat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%28_%3Ashouldindentwhileeditingrowat%3A%29.json'
content_hash: 'sha256:dcd61108f940d047'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView(_:shouldIndentWhileEditingRowAt:)

<sub>Instance Method</sub>

Asks the delegate whether the background of the specified row should be indented while the table view is in editing mode.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, shouldIndentWhileEditingRowAt indexPath: IndexPath) -> Bool
```

## Parameters

- `tableView` — The table view requesting this information.

- `indexPath` — An index path locating the row in its section.

## Return Value

[true](../../swift/true.md) if the background of the row should be indented, otherwise [false](../../swift/false.md).

## Discussion

If the delegate does not implement this method, the default is [true](../../swift/true.md). This method is unrelated to [- tableView:indentationLevelForRowAtIndexPath:](<tableview(__indentationlevelforrowat_).md>).

## See Also

### Editing table rows

- [- tableView:willBeginEditingRowAtIndexPath:](<tableview(__willbegineditingrowat_).md>) — Tells the delegate that the table view is about to go into editing mode.
- [- tableView:didEndEditingRowAtIndexPath:](<tableview(__didendeditingrowat_).md>) — Tells the delegate that the table view has left editing mode.
- [- tableView:editingStyleForRowAtIndexPath:](<tableview(__editingstyleforrowat_).md>) — Asks the delegate for the editing style of a row at a particular location in a table view.
- [- tableView:titleForDeleteConfirmationButtonForRowAtIndexPath:](<tableview(__titlefordeleteconfirmationbuttonforrowat_).md>) — Changes the default title of the delete-confirmation button.
