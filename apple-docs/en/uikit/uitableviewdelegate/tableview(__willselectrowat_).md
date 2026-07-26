---
title: 'tableView(_:willSelectRowAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdelegate/tableview(_:willselectrowat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:willselectrowat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%28_%3Awillselectrowat%3A%29.json'
content_hash: 'sha256:83d7777ddf22c100'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView(_:willSelectRowAt:)

<sub>Instance Method</sub>

Tells the delegate a row is about to be selected.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, willSelectRowAt indexPath: IndexPath) -> IndexPath?
```

## Parameters

- `tableView` — A table view informing the delegate about the impending selection.

- `indexPath` — An index path locating the row in `tableView`.

## Return Value

An index path that confirms or alters the selected row. Return an [IndexPath](../../foundation/indexpath.md) (Swift) or [NSIndexPath](../../foundation/nsindexpath.md) (Objective-C) other than `indexPath` if you want another cell to be selected. Return `nil` if you don’t want the row selected.

## Discussion

The system calls this method after a user has lifted their finger; the row is highlighted on the initial touch, but only selected when the touch withdraws. You can use [UITableViewCellSelectionStyleNone](../uitableviewcell/selectionstyle-swift.enum/none.md) to disable the appearance of the cell highlight on the initial touch. The system doesn’t call this method if the rows in the table aren’t selectable. See [Handling row selection in a table view](../handling-row-selection-in-a-table-view.md) for more information on controlling table row selection behavior.

## See Also

### Related Documentation

- [- tableView:shouldIndentWhileEditingRowAtIndexPath:](<tableview(__shouldindentwhileeditingrowat_).md>) — Asks the delegate whether the background of the specified row should be indented while the table view is in editing mode.

### Responding to row selections

- [Handling row selection in a table view](../handling-row-selection-in-a-table-view.md) — Detect when a user taps a table view cell so your app can take the next indicated action.
- [Selecting multiple items with a two-finger pan gesture](../selecting-multiple-items-with-a-two-finger-pan-gesture.md) — Accelerate user selection of multiple items using the multiselect gesture on table and collection views.
- [- tableView:didSelectRowAtIndexPath:](<tableview(__didselectrowat_).md>) — Tells the delegate a row is selected.
- [- tableView:willDeselectRowAtIndexPath:](<tableview(__willdeselectrowat_).md>) — Tells the delegate that a specified row is about to be deselected.
- [- tableView:didDeselectRowAtIndexPath:](<tableview(__diddeselectrowat_).md>) — Tells the delegate that the specified row is now deselected.
- [- tableView:shouldBeginMultipleSelectionInteractionAtIndexPath:](<tableview(__shouldbeginmultipleselectioninteractionat_).md>) — Asks the delegate whether the user can use a two-finger pan gesture to select multiple items in a table view.
- [- tableView:didBeginMultipleSelectionInteractionAtIndexPath:](<tableview(__didbeginmultipleselectioninteractionat_).md>) — Tells the delegate when the user starts using a two-finger pan gesture to select multiple rows in a table view.
- [- tableViewDidEndMultipleSelectionInteraction:](<tableviewdidendmultipleselectioninteraction(__).md>) — Tells the delegate when the user stops using a two-finger pan gesture to select multiple rows in a table view.
