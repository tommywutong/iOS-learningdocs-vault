---
title: 'tableView(_:didEndDisplayingHeaderView:forSection:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdelegate/tableview(_:didenddisplayingheaderview:forsection:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:didenddisplayingheaderview:forsection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%28_%3Adidenddisplayingheaderview%3Aforsection%3A%29.json'
content_hash: 'sha256:72658684d469dc32'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView(_:didEndDisplayingHeaderView:forSection:)

<sub>Instance Method</sub>

Tells the delegate that the specified header view was removed from the table.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, didEndDisplayingHeaderView view: UIView, forSection section: Int)
```

## Parameters

- `tableView` — The table view that removed the view.

- `view` — The header view that was removed.

- `section` — The index of the section that contained the header.

## Discussion

Use this method to detect when a header view is removed from a table view, as opposed to monitoring the view itself to see when it appears or disappears.

## See Also

### Tracking the removal of views

- [- tableView:didEndDisplayingCell:forRowAtIndexPath:](<tableview(__didenddisplaying_forrowat_).md>) — Tells the delegate that the specified cell was removed from the table.
- [- tableView:didEndDisplayingFooterView:forSection:](<tableview(__didenddisplayingfooterview_forsection_).md>) — Tells the delegate that the specified footer view was removed from the table.
