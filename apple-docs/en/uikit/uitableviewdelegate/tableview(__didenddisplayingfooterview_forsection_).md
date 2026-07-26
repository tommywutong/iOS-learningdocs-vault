---
title: 'tableView(_:didEndDisplayingFooterView:forSection:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdelegate/tableview(_:didenddisplayingfooterview:forsection:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:didenddisplayingfooterview:forsection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%28_%3Adidenddisplayingfooterview%3Aforsection%3A%29.json'
content_hash: 'sha256:298c0101fff78886'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView(_:didEndDisplayingFooterView:forSection:)

<sub>Instance Method</sub>

Tells the delegate that the specified footer view was removed from the table.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, didEndDisplayingFooterView view: UIView, forSection section: Int)
```

## Parameters

- `tableView` — The table view that removed the view.

- `view` — The footer view that was removed.

- `section` — The index of the section that contained the footer.

## Discussion

Use this method to detect when a footer view is removed from a table view, as opposed to monitoring the view itself to see when it appears or disappears.

## See Also

### Tracking the removal of views

- [- tableView:didEndDisplayingCell:forRowAtIndexPath:](<tableview(__didenddisplaying_forrowat_).md>) — Tells the delegate that the specified cell was removed from the table.
- [- tableView:didEndDisplayingHeaderView:forSection:](<tableview(__didenddisplayingheaderview_forsection_).md>) — Tells the delegate that the specified header view was removed from the table.
