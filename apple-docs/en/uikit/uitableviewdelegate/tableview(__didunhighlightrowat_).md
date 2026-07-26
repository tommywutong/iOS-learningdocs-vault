---
title: 'tableView(_:didUnhighlightRowAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdelegate/tableview(_:didunhighlightrowat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:didunhighlightrowat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%28_%3Adidunhighlightrowat%3A%29.json'
content_hash: 'sha256:da166e2179a1ac67'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView(_:didUnhighlightRowAt:)

<sub>Instance Method</sub>

Tells the delegate that the highlight was removed from the row at the specified index path.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, didUnhighlightRowAt indexPath: IndexPath)
```

## Parameters

- `tableView` — The table view that removed the highlight from the cell.

- `indexPath` — The index path of the row that had its highlight removed.

## See Also

### Managing table view highlights

- [- tableView:shouldHighlightRowAtIndexPath:](<tableview(__shouldhighlightrowat_).md>) — Asks the delegate if the specified row should be highlighted.
- [- tableView:didHighlightRowAtIndexPath:](<tableview(__didhighlightrowat_).md>) — Tells the delegate that the specified row was highlighted.
