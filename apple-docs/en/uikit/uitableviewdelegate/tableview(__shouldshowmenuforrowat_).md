---
title: 'tableView(_:shouldShowMenuForRowAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+（13.0 起废弃）, iPadOS 5.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（13.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uitableviewdelegate/tableview(_:shouldshowmenuforrowat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:shouldshowmenuforrowat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%28_%3Ashouldshowmenuforrowat%3A%29.json'
content_hash: 'sha256:8a73db556c6f07f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView(_:shouldShowMenuForRowAt:)

<sub>Instance Method</sub>

Asks the delegate if the editing menu should be shown for a certain row.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
optional func tableView(_ tableView: UITableView, shouldShowMenuForRowAt indexPath: IndexPath) -> Bool
```

## Parameters

- `tableView` — The table view that is making this request.

- `indexPath` — The index path of the row.

## Return Value

[true](../../swift/true.md) if the editing menu should be shown positioned near the row and pointing to it, otherwise [false](../../swift/false.md). The default value is [false](../../swift/false.md).

## Discussion

If the user tap-holds a certain row in the table view, this method (if implemented) is invoked first. Return [false](../../swift/false.md) if the editing menu shouldn’t be shown—for example, the cell corresponding to the row contains content that shouldn’t be copied or pasted over.

## See Also

### Responding to row actions

- [- tableView:leadingSwipeActionsConfigurationForRowAtIndexPath:](<tableview(__leadingswipeactionsconfigurationforrowat_).md>) — Returns the swipe actions to display on the leading edge of the row.
- [- tableView:trailingSwipeActionsConfigurationForRowAtIndexPath:](<tableview(__trailingswipeactionsconfigurationforrowat_).md>) — Returns the swipe actions to display on the trailing edge of the row.
- [- tableView:canPerformAction:forRowAtIndexPath:withSender:](<tableview(__canperformaction_forrowat_withsender_).md>) — Asks the delegate if the editing menu should omit the Copy or Paste command for a given row. _(deprecated)_
- [- tableView:performAction:forRowAtIndexPath:withSender:](<tableview(__performaction_forrowat_withsender_).md>) — Tells the delegate to perform a copy or paste operation on the content of a given row. _(deprecated)_
- [- tableView:editActionsForRowAtIndexPath:](<tableview(__editactionsforrowat_).md>) — Asks the delegate for the actions to display in response to a swipe in the specified row. _(deprecated)_
