---
title: 'tableView(_:performPrimaryActionForRowAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdelegate/tableview(_:performprimaryactionforrowat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:performprimaryactionforrowat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%28_%3Aperformprimaryactionforrowat%3A%29.json'
content_hash: 'sha256:471036630922b8bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView(_:performPrimaryActionForRowAt:)

<sub>Instance Method</sub>

Tells the delegate to perform the primary action for the row at the specified index path.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, performPrimaryActionForRowAt indexPath: IndexPath)
```

## Parameters

- `tableView` — The table view object on which to perform the primary action.

- `indexPath` — The index path of the row.

## Discussion

Primary actions allow you to distinguish between a distinct user action and a change in selection (like a focus change or other indirect selection change). A primary action occurs when a person selects a single row without extending an existing selection.

UIKit calls this method after [- tableView:willSelectRowAtIndexPath:](<tableview(__willselectrowat_).md>) and [- tableView:didSelectRowAtIndexPath:](<tableview(__didselectrowat_).md>), regardless of whether the row selection state changes. Use [- tableView:didSelectRowAtIndexPath:](<tableview(__didselectrowat_).md>) to update the state of the current view controller (like its buttons, title, and so on), and use [- tableView:performPrimaryActionForRowAtIndexPath:](<tableview(__performprimaryactionforrowat_).md>) for actions like navigation or showing another split view column.

If [- tableView:willSelectRowAtIndexPath:](<tableview(__willselectrowat_).md>) returns an index path to allow selection for the row, only that row has selection when the system calls this method. If [- tableView:willSelectRowAtIndexPath:](<tableview(__willselectrowat_).md>) returns `nil`, the system preserves the existing row selection in the table view. You can use this behavior to perform primary actions on nonselectable, button-style rows without changing the selection.

## See Also

### Performing primary actions

- [- tableView:canPerformPrimaryActionForRowAtIndexPath:](<tableview(__canperformprimaryactionforrowat_).md>) — Asks the delegate whether to perform a primary action for the row at the specified index path.
