---
title: 'tableView(_:shouldBeginMultipleSelectionInteractionAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdelegate/tableview(_:shouldbeginmultipleselectioninteractionat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:shouldbeginmultipleselectioninteractionat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%28_%3Ashouldbeginmultipleselectioninteractionat%3A%29.json'
content_hash: 'sha256:97f63a2ec26dbe1b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView(_:shouldBeginMultipleSelectionInteractionAt:)

<sub>Instance Method</sub>

Asks the delegate whether the user can use a two-finger pan gesture to select multiple items in a table view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, shouldBeginMultipleSelectionInteractionAt indexPath: IndexPath) -> Bool
```

## Parameters

- `tableView` — The table view calling this method.

- `indexPath` — The index path of the row that the user touched to start the two-finger pan gesture.

## Return Value

[true](../../swift/true.md) to allow the user to select multiple rows using a two-finger pan gesture; otherwise, [false](../../swift/false.md) to disable the behavior. The default value is [false](../../swift/false.md).

## Discussion

When the system recognizes a two-finger pan gesture, it calls this method before it sets [editing](../uitableview/isediting.md) to [true](../../swift/true.md). If you return [true](../../swift/true.md) from this method, the user can select multiple rows using a two-finger pan gesture.

In macOS, the system calls this method when a user attempts to select multiple rows by holding a modifier key and clicking additional rows to select them.

To support multiple selection using the two-finger pan gesture (in iOS) or modifier keys (in macOS), set the [allowsMultipleSelectionDuringEditing](../uitableview/allowsmultipleselectionduringediting.md) property to [true](../../swift/true.md) when you configure the table view.

## See Also

### Responding to row selections

- [Handling row selection in a table view](../handling-row-selection-in-a-table-view.md) — Detect when a user taps a table view cell so your app can take the next indicated action.
- [Selecting multiple items with a two-finger pan gesture](../selecting-multiple-items-with-a-two-finger-pan-gesture.md) — Accelerate user selection of multiple items using the multiselect gesture on table and collection views.
- [- tableView:willSelectRowAtIndexPath:](<tableview(__willselectrowat_).md>) — Tells the delegate a row is about to be selected.
- [- tableView:didSelectRowAtIndexPath:](<tableview(__didselectrowat_).md>) — Tells the delegate a row is selected.
- [- tableView:willDeselectRowAtIndexPath:](<tableview(__willdeselectrowat_).md>) — Tells the delegate that a specified row is about to be deselected.
- [- tableView:didDeselectRowAtIndexPath:](<tableview(__diddeselectrowat_).md>) — Tells the delegate that the specified row is now deselected.
- [- tableView:didBeginMultipleSelectionInteractionAtIndexPath:](<tableview(__didbeginmultipleselectioninteractionat_).md>) — Tells the delegate when the user starts using a two-finger pan gesture to select multiple rows in a table view.
- [- tableViewDidEndMultipleSelectionInteraction:](<tableviewdidendmultipleselectioninteraction(__).md>) — Tells the delegate when the user stops using a two-finger pan gesture to select multiple rows in a table view.
