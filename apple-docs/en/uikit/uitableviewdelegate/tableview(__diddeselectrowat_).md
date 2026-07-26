---
title: 'tableView(_:didDeselectRowAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdelegate/tableview(_:diddeselectrowat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:diddeselectrowat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%28_%3Adiddeselectrowat%3A%29.json'
content_hash: 'sha256:977ee6a157acf557'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView(_:didDeselectRowAt:)

<sub>Instance Method</sub>

Tells the delegate that the specified row is now deselected.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, didDeselectRowAt indexPath: IndexPath)
```

## Parameters

- `tableView` — A table view informing the delegate about the row deselection.

- `indexPath` — An index path locating the deselected row in `tableView`.

## Discussion

The delegate handles row deselections in this method. It could, for example, remove the check-mark image ([UITableViewCellAccessoryCheckmark](../uitableviewcell/accessorytype-swift.enum/checkmark.md)) associated with the row.

## See Also

### Responding to row selections

- [Handling row selection in a table view](../handling-row-selection-in-a-table-view.md) — Detect when a user taps a table view cell so your app can take the next indicated action.
- [Selecting multiple items with a two-finger pan gesture](../selecting-multiple-items-with-a-two-finger-pan-gesture.md) — Accelerate user selection of multiple items using the multiselect gesture on table and collection views.
- [- tableView:willSelectRowAtIndexPath:](<tableview(__willselectrowat_).md>) — Tells the delegate a row is about to be selected.
- [- tableView:didSelectRowAtIndexPath:](<tableview(__didselectrowat_).md>) — Tells the delegate a row is selected.
- [- tableView:willDeselectRowAtIndexPath:](<tableview(__willdeselectrowat_).md>) — Tells the delegate that a specified row is about to be deselected.
- [- tableView:shouldBeginMultipleSelectionInteractionAtIndexPath:](<tableview(__shouldbeginmultipleselectioninteractionat_).md>) — Asks the delegate whether the user can use a two-finger pan gesture to select multiple items in a table view.
- [- tableView:didBeginMultipleSelectionInteractionAtIndexPath:](<tableview(__didbeginmultipleselectioninteractionat_).md>) — Tells the delegate when the user starts using a two-finger pan gesture to select multiple rows in a table view.
- [- tableViewDidEndMultipleSelectionInteraction:](<tableviewdidendmultipleselectioninteraction(__).md>) — Tells the delegate when the user stops using a two-finger pan gesture to select multiple rows in a table view.
