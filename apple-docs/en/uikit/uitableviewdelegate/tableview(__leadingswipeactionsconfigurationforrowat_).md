---
title: 'tableView(_:leadingSwipeActionsConfigurationForRowAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdelegate/tableview(_:leadingswipeactionsconfigurationforrowat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:leadingswipeactionsconfigurationforrowat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%28_%3Aleadingswipeactionsconfigurationforrowat%3A%29.json'
content_hash: 'sha256:3d965cd4b0e3a069'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView(_:leadingSwipeActionsConfigurationForRowAt:)

<sub>Instance Method</sub>

Returns the swipe actions to display on the leading edge of the row.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, leadingSwipeActionsConfigurationForRowAt indexPath: IndexPath) -> UISwipeActionsConfiguration?
```

## Parameters

- `tableView` — The table view containing the row.

- `indexPath` — The index path of the row.

## Return Value

The swipe actions to display next to the leading edge of the row. Return `nil` if you want the table to display the default set of actions.

## Discussion

Use this method to return a set of actions to display when the user swipes the row. The actions you return are displayed on the leading edge of the row. For example, in a left-to-right language environment, they are displayed on the left side of the row when the user swipes from left to right.

## See Also

### Responding to row actions

- [- tableView:trailingSwipeActionsConfigurationForRowAtIndexPath:](<tableview(__trailingswipeactionsconfigurationforrowat_).md>) — Returns the swipe actions to display on the trailing edge of the row.
- [- tableView:shouldShowMenuForRowAtIndexPath:](<tableview(__shouldshowmenuforrowat_).md>) — Asks the delegate if the editing menu should be shown for a certain row. _(deprecated)_
- [- tableView:canPerformAction:forRowAtIndexPath:withSender:](<tableview(__canperformaction_forrowat_withsender_).md>) — Asks the delegate if the editing menu should omit the Copy or Paste command for a given row. _(deprecated)_
- [- tableView:performAction:forRowAtIndexPath:withSender:](<tableview(__performaction_forrowat_withsender_).md>) — Tells the delegate to perform a copy or paste operation on the content of a given row. _(deprecated)_
- [- tableView:editActionsForRowAtIndexPath:](<tableview(__editactionsforrowat_).md>) — Asks the delegate for the actions to display in response to a swipe in the specified row. _(deprecated)_
