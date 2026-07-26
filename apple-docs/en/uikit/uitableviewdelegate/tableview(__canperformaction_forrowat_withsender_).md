---
title: 'tableView(_:canPerformAction:forRowAt:withSender:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+（13.0 起废弃）, iPadOS 5.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（13.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uitableviewdelegate/tableview(_:canperformaction:forrowat:withsender:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:canperformaction:forrowat:withsender:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%28_%3Acanperformaction%3Aforrowat%3Awithsender%3A%29.json'
content_hash: 'sha256:c68551f569f5c916'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView(_:canPerformAction:forRowAt:withSender:)

<sub>Instance Method</sub>

Asks the delegate if the editing menu should omit the Copy or Paste command for a given row.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
optional func tableView(_ tableView: UITableView, canPerformAction action: Selector, forRowAt indexPath: IndexPath, withSender sender: Any?) -> Bool
```

## Parameters

- `tableView` — The table view that is making this request.

- `action` — A selector type identifying the [- copy:](<../uiresponderstandardeditactions/copy(__).md>) or [- paste:](<../uiresponderstandardeditactions/paste(__).md>) method of the [UIResponderStandardEditActions](../uiresponderstandardeditactions.md) informal protocol.

- `indexPath` — The index path of the row.

- `sender` — The object that initially sent the `copy:` or `paste:` message.

## Return Value

[true](../../swift/true.md) if the command corresponding to `action` should appear in the editing menu, otherwise [false](../../swift/false.md). The default value is [false](../../swift/false.md).

## Discussion

This method is invoked after [- tableView:shouldShowMenuForRowAtIndexPath:](<tableview(__shouldshowmenuforrowat_).md>). It gives the developer the opportunity to exclude one of the commands—Copy or Paste—from the editing menu. For example, the user might have copied some cell content from one row but wants to paste into another row that doesn’t take the copied content. In a case like this, return [false](../../swift/false.md) from this method.

## See Also

### Responding to row actions

- [- tableView:leadingSwipeActionsConfigurationForRowAtIndexPath:](<tableview(__leadingswipeactionsconfigurationforrowat_).md>) — Returns the swipe actions to display on the leading edge of the row.
- [- tableView:trailingSwipeActionsConfigurationForRowAtIndexPath:](<tableview(__trailingswipeactionsconfigurationforrowat_).md>) — Returns the swipe actions to display on the trailing edge of the row.
- [- tableView:shouldShowMenuForRowAtIndexPath:](<tableview(__shouldshowmenuforrowat_).md>) — Asks the delegate if the editing menu should be shown for a certain row. _(deprecated)_
- [- tableView:performAction:forRowAtIndexPath:withSender:](<tableview(__performaction_forrowat_withsender_).md>) — Tells the delegate to perform a copy or paste operation on the content of a given row. _(deprecated)_
- [- tableView:editActionsForRowAtIndexPath:](<tableview(__editactionsforrowat_).md>) — Asks the delegate for the actions to display in response to a swipe in the specified row. _(deprecated)_
