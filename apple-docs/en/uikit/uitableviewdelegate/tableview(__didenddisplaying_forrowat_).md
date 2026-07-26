---
title: 'tableView(_:didEndDisplaying:forRowAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdelegate/tableview(_:didenddisplaying:forrowat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:didenddisplaying:forrowat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%28_%3Adidenddisplaying%3Aforrowat%3A%29.json'
content_hash: 'sha256:c2445f06e141e94e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView(_:didEndDisplaying:forRowAt:)

<sub>Instance Method</sub>

Tells the delegate that the specified cell was removed from the table.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, didEndDisplaying cell: UITableViewCell, forRowAt indexPath: IndexPath)
```

## Parameters

- `tableView` — The table view that removed the view.

- `cell` — The cell that was removed.

- `indexPath` — The index path of the cell.

## Discussion

Use this method to detect when a cell is removed from a table view, as opposed to monitoring the view itself to see when it appears or disappears.

## See Also

### Tracking the removal of views

- [- tableView:didEndDisplayingHeaderView:forSection:](<tableview(__didenddisplayingheaderview_forsection_).md>) — Tells the delegate that the specified header view was removed from the table.
- [- tableView:didEndDisplayingFooterView:forSection:](<tableview(__didenddisplayingfooterview_forsection_).md>) — Tells the delegate that the specified footer view was removed from the table.
