---
title: 'tableView(_:performAction:forRowAt:withSender:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+（13.0 起废弃）, iPadOS 5.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（13.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uitableviewdelegate/tableview(_:performaction:forrowat:withsender:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:performaction:forrowat:withsender:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%28_%3Aperformaction%3Aforrowat%3Awithsender%3A%29.json'
content_hash: 'sha256:cb65dc15718b9a13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView(_:performAction:forRowAt:withSender:)

<sub>Instance Method</sub>

Tells the delegate to perform a copy or paste operation on the content of a given row.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
optional func tableView(_ tableView: UITableView, performAction action: Selector, forRowAt indexPath: IndexPath, withSender sender: Any?)
```

## Parameters

- `tableView` — The table view that is making this request.

- `action` — A selector type identifying the [- copy:](<../uiresponderstandardeditactions/copy(__).md>) or [- paste:](<../uiresponderstandardeditactions/paste(__).md>) method of the [UIResponderStandardEditActions](../uiresponderstandardeditactions.md) informal protocol.

- `indexPath` — The index path of the row.

- `sender` — The object that initially sent the `copy:` or `paste:` message.

## Discussion

The table view invokes this method for a given `action` if the user taps Copy or Paste in the editing menu. The delegate can do whatever is appropriate for the action; for example, for a copy, it can extract the relevant cell content for the row at `indexPath` and write it to the general pasteboard or an application (private) pasteboard. See [UIPasteboard](../uipasteboard.md) for further information.

## See Also

### Responding to row actions

- [- tableView:leadingSwipeActionsConfigurationForRowAtIndexPath:](<tableview(__leadingswipeactionsconfigurationforrowat_).md>) — Returns the swipe actions to display on the leading edge of the row.
- [- tableView:trailingSwipeActionsConfigurationForRowAtIndexPath:](<tableview(__trailingswipeactionsconfigurationforrowat_).md>) — Returns the swipe actions to display on the trailing edge of the row.
- [- tableView:shouldShowMenuForRowAtIndexPath:](<tableview(__shouldshowmenuforrowat_).md>) — Asks the delegate if the editing menu should be shown for a certain row. _(deprecated)_
- [- tableView:canPerformAction:forRowAtIndexPath:withSender:](<tableview(__canperformaction_forrowat_withsender_).md>) — Asks the delegate if the editing menu should omit the Copy or Paste command for a given row. _(deprecated)_
- [- tableView:editActionsForRowAtIndexPath:](<tableview(__editactionsforrowat_).md>) — Asks the delegate for the actions to display in response to a swipe in the specified row. _(deprecated)_
