---
title: 'tableView(_:titleForHeaderInSection:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdatasource/tableview(_:titleforheaderinsection:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdatasource/tableview(_:titleforheaderinsection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdatasource/tableview%28_%3Atitleforheaderinsection%3A%29.json'
content_hash: 'sha256:1d0118ee506efee1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDataSource](../uitableviewdatasource.md)

# tableView(_:titleForHeaderInSection:)

<sub>Instance Method</sub>

Asks the data source for the title of the header of the specified section of the table view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, titleForHeaderInSection section: Int) -> String?
```

## Parameters

- `tableView` — The table-view object asking for the title.

- `section` — An index number identifying a section of `tableView`.

## Return Value

A string to use as the title of the section header. If you return `nil` , the section will have no title.

## Discussion

The table view uses a fixed font style for section header titles. If you want a different font style, return a custom view (for example, a [UILabel](../uilabel.md) object) in the delegate method [- tableView:viewForHeaderInSection:](<../uitableviewdelegate/tableview(__viewforheaderinsection_).md>) instead.

If you don’t implement this method or the [- tableView:viewForHeaderInSection:](<../uitableviewdelegate/tableview(__viewforheaderinsection_).md>) method, the table doesn’t display headers for sections. If you implement both methods, the [- tableView:viewForHeaderInSection:](<../uitableviewdelegate/tableview(__viewforheaderinsection_).md>) method takes priority.

## See Also

### Providing cells, headers, and footers

- [- tableView:cellForRowAtIndexPath:](<tableview(__cellforrowat_).md>) — Asks the data source for a cell to insert in a particular location of the table view.
- [- tableView:titleForFooterInSection:](<tableview(__titleforfooterinsection_).md>) — Asks the data source for the title of the footer of the specified section of the table view.
