---
title: 'tableView(_:didBeginMultipleSelectionInteractionAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdelegate/tableview(_:didbeginmultipleselectioninteractionat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:didbeginmultipleselectioninteractionat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%28_%3Adidbeginmultipleselectioninteractionat%3A%29.json'
content_hash: 'sha256:7ab55362b8e24421'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView(_:didBeginMultipleSelectionInteractionAt:)

<sub>Instance Method</sub>

Tells the delegate when the user starts using a two-finger pan gesture to select multiple rows in a table view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, didBeginMultipleSelectionInteractionAt indexPath: IndexPath)
```

## Parameters

- `tableView` — The table view calling this method.

- `indexPath` — The index path of the item that the user touched to start the two-finger pan gesture.

## Discussion

Your implementation of this method is a good place to indicate, in the app’s user interface, that the user is selecting multiple rows; for example, you could replace an Edit or Select button with a Done button.

```swift
override func tableView(_ tableView: UITableView, didBeginMultipleSelectionInteractionAt indexPath: IndexPath) {
    // Replace the Edit button with Done, and put the
    // table view into editing mode.
    self.setEditing(true, animated: true)
}
```

## See Also

### Responding to row selections

- [Handling row selection in a table view](../handling-row-selection-in-a-table-view.md) — Detect when a user taps a table view cell so your app can take the next indicated action.
- [Selecting multiple items with a two-finger pan gesture](../selecting-multiple-items-with-a-two-finger-pan-gesture.md) — Accelerate user selection of multiple items using the multiselect gesture on table and collection views.
- [- tableView:willSelectRowAtIndexPath:](<tableview(__willselectrowat_).md>) — Tells the delegate a row is about to be selected.
- [- tableView:didSelectRowAtIndexPath:](<tableview(__didselectrowat_).md>) — Tells the delegate a row is selected.
- [- tableView:willDeselectRowAtIndexPath:](<tableview(__willdeselectrowat_).md>) — Tells the delegate that a specified row is about to be deselected.
- [- tableView:didDeselectRowAtIndexPath:](<tableview(__diddeselectrowat_).md>) — Tells the delegate that the specified row is now deselected.
- [- tableView:shouldBeginMultipleSelectionInteractionAtIndexPath:](<tableview(__shouldbeginmultipleselectioninteractionat_).md>) — Asks the delegate whether the user can use a two-finger pan gesture to select multiple items in a table view.
- [- tableViewDidEndMultipleSelectionInteraction:](<tableviewdidendmultipleselectioninteraction(__).md>) — Tells the delegate when the user stops using a two-finger pan gesture to select multiple rows in a table view.
