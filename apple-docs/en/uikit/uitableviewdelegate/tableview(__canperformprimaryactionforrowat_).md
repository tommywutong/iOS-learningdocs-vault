---
title: 'tableView(_:canPerformPrimaryActionForRowAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdelegate/tableview(_:canperformprimaryactionforrowat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:canperformprimaryactionforrowat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%28_%3Acanperformprimaryactionforrowat%3A%29.json'
content_hash: 'sha256:9cc13ff5342d8459'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView(_:canPerformPrimaryActionForRowAt:)

<sub>Instance Method</sub>

Asks the delegate whether to perform a primary action for the row at the specified index path.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, canPerformPrimaryActionForRowAt indexPath: IndexPath) -> Bool
```

## Parameters

- `tableView` — The table view object asking whether to perform a primary action.

- `indexPath` — The index path of the row.

## Return Value

[true](../../swift/true.md) if the primary action can be performed; otherwise, [false](../../swift/false.md). If you don’t implement this method, the default return value is [true](../../swift/true.md) when the table view isn’t in an editing state, and [false](../../swift/false.md) when it is.

## Discussion

Primary actions allow you to distinguish between a distinct user action and a change in selection (like a focus change or other indirect selection change). A primary action occurs when a person selects a single row without extending an existing selection.

UIKit calls this method before [- tableView:performPrimaryActionForRowAtIndexPath:](<tableview(__performprimaryactionforrowat_).md>).

## See Also

### Performing primary actions

- [- tableView:performPrimaryActionForRowAtIndexPath:](<tableview(__performprimaryactionforrowat_).md>) — Tells the delegate to perform the primary action for the row at the specified index path.
