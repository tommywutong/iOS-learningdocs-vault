---
title: 'tableView(_:willDisplayFooterView:forSection:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdelegate/tableview(_:willdisplayfooterview:forsection:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:willdisplayfooterview:forsection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%28_%3Awilldisplayfooterview%3Aforsection%3A%29.json'
content_hash: 'sha256:118350e1022fcb5e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView(_:willDisplayFooterView:forSection:)

<sub>Instance Method</sub>

Tells the delegate that the table is about to display the footer view for the specified section.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, willDisplayFooterView view: UIView, forSection section: Int)
```

## Parameters

- `tableView` — The table view informing the delegate of this event.

- `view` — The footer view that is about to be displayed.

- `section` — The index number of the section containing the footer view.

## See Also

### Providing custom header and footer views

- [- tableView:viewForHeaderInSection:](<tableview(__viewforheaderinsection_).md>) — Asks the delegate for a view to display in the header of the specified section of the table view.
- [- tableView:viewForFooterInSection:](<tableview(__viewforfooterinsection_).md>) — Asks the delegate for a view to display in the footer of the specified section of the table view.
- [- tableView:willDisplayHeaderView:forSection:](<tableview(__willdisplayheaderview_forsection_).md>) — Tells the delegate that the table is about to display the header view for the specified section.
