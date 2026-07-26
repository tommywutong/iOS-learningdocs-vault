---
title: 'tableView(_:editActionsForRowAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+（13.0 起废弃）, iPadOS 8.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uitableviewdelegate/tableview(_:editactionsforrowat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:editactionsforrowat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%28_%3Aeditactionsforrowat%3A%29.json'
content_hash: 'sha256:d2e989fd917615d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView(_:editActionsForRowAt:)

<sub>Instance Method</sub>

Asks the delegate for the actions to display in response to a swipe in the specified row.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func tableView(_ tableView: UITableView, editActionsForRowAt indexPath: IndexPath) -> [UITableViewRowAction]?
```

## Parameters

- `tableView` — The table view requesting this information.

- `indexPath` — The index path of the row.

## Return Value

An array of [UITableViewRowAction](../uitableviewrowaction.md) objects representing the actions for the row. Each action you provide is used to create a button that the user can tap.

## Discussion

Use this method when you want to provide custom actions for one of your table rows. When the user swipes horizontally in a row, the table view moves the row content aside to reveal your actions. Tapping one of the action buttons executes the handler block stored with the action object.

If you do not implement this method, the table view displays the standard accessory buttons when the user swipes the row.

## See Also

### Responding to row actions

- [- tableView:leadingSwipeActionsConfigurationForRowAtIndexPath:](<tableview(__leadingswipeactionsconfigurationforrowat_).md>) — Returns the swipe actions to display on the leading edge of the row.
- [- tableView:trailingSwipeActionsConfigurationForRowAtIndexPath:](<tableview(__trailingswipeactionsconfigurationforrowat_).md>) — Returns the swipe actions to display on the trailing edge of the row.
- [- tableView:shouldShowMenuForRowAtIndexPath:](<tableview(__shouldshowmenuforrowat_).md>) — Asks the delegate if the editing menu should be shown for a certain row. _(deprecated)_
- [- tableView:canPerformAction:forRowAtIndexPath:withSender:](<tableview(__canperformaction_forrowat_withsender_).md>) — Asks the delegate if the editing menu should omit the Copy or Paste command for a given row. _(deprecated)_
- [- tableView:performAction:forRowAtIndexPath:withSender:](<tableview(__performaction_forrowat_withsender_).md>) — Tells the delegate to perform a copy or paste operation on the content of a given row. _(deprecated)_
