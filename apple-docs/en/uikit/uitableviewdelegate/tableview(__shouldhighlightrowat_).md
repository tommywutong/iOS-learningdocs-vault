---
title: 'tableView(_:shouldHighlightRowAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdelegate/tableview(_:shouldhighlightrowat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:shouldhighlightrowat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%28_%3Ashouldhighlightrowat%3A%29.json'
content_hash: 'sha256:e420900f2e2435f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView(_:shouldHighlightRowAt:)

<sub>Instance Method</sub>

Asks the delegate if the specified row should be highlighted.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, shouldHighlightRowAt indexPath: IndexPath) -> Bool
```

## Parameters

- `tableView` — The table view that is making this request.

- `indexPath` — The index path of the row being highlighted.

## Return Value

[true](../../swift/true.md) if the row should be highlighted or [false](../../swift/false.md) if it should not.

## Discussion

As touch events arrive, the table view highlights rows in anticipation of the user selecting them. As it processes those touch events, the table view calls this method to ask your delegate if a given cell should be highlighted. Your delegate can implement this method and use it to prevent the highlighting of a row when another row is already selected or when other relevant criteria occur.

If you do not implement this method, the default return value is [true](../../swift/true.md).

## See Also

### Managing table view highlights

- [- tableView:didHighlightRowAtIndexPath:](<tableview(__didhighlightrowat_).md>) — Tells the delegate that the specified row was highlighted.
- [- tableView:didUnhighlightRowAtIndexPath:](<tableview(__didunhighlightrowat_).md>) — Tells the delegate that the highlight was removed from the row at the specified index path.
