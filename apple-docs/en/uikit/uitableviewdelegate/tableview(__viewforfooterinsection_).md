---
title: 'tableView(_:viewForFooterInSection:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdelegate/tableview(_:viewforfooterinsection:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:viewforfooterinsection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%28_%3Aviewforfooterinsection%3A%29.json'
content_hash: 'sha256:a74790a0943a963b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView(_:viewForFooterInSection:)

<sub>Instance Method</sub>

Asks the delegate for a view to display in the footer of the specified section of the table view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, viewForFooterInSection section: Int) -> UIView?
```

## Parameters

- `tableView` — The table view asking for the view.

- `section` — The index number of the section containing the footer view.

## Return Value

A [UILabel](../uilabel.md), [UIImageView](../uiimageview.md), or custom view to display at the bottom of the specified section.

## Discussion

If you implement this method but don’t implement [- tableView:heightForFooterInSection:](<tableview(__heightforfooterinsection_).md>), the table view calculates the height automatically, or uses the value of [sectionFooterHeight](../uitableview/sectionfooterheight.md) if set.

## See Also

### Providing custom header and footer views

- [- tableView:viewForHeaderInSection:](<tableview(__viewforheaderinsection_).md>) — Asks the delegate for a view to display in the header of the specified section of the table view.
- [- tableView:willDisplayHeaderView:forSection:](<tableview(__willdisplayheaderview_forsection_).md>) — Tells the delegate that the table is about to display the header view for the specified section.
- [- tableView:willDisplayFooterView:forSection:](<tableview(__willdisplayfooterview_forsection_).md>) — Tells the delegate that the table is about to display the footer view for the specified section.
