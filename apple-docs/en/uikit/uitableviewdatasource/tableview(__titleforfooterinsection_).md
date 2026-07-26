---
title: 'tableView(_:titleForFooterInSection:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdatasource/tableview(_:titleforfooterinsection:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdatasource/tableview(_:titleforfooterinsection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdatasource/tableview%28_%3Atitleforfooterinsection%3A%29.json'
content_hash: 'sha256:d4eb3058c3617209'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDataSource](../uitableviewdatasource.md)

# tableView(_:titleForFooterInSection:)

<sub>Instance Method</sub>

Asks the data source for the title of the footer of the specified section of the table view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, titleForFooterInSection section: Int) -> String?
```

## Parameters

- `tableView` — The table-view object asking for the title.

- `section` — An index number identifying a section of `tableView`.

## Return Value

A string to use as the title of the section footer. If you return `nil` , the section will have no title.

## Discussion

The table view uses a fixed font style for section footer titles. If you want a different font style, return a custom view (for example, a [UILabel](../uilabel.md) object) in the delegate method [- tableView:viewForFooterInSection:](<../uitableviewdelegate/tableview(__viewforfooterinsection_).md>) instead.

If you don’t implement this method or the [- tableView:viewForFooterInSection:](<../uitableviewdelegate/tableview(__viewforfooterinsection_).md>) method, the table doesn’t display footers for sections. If you implement both methods, the [- tableView:viewForFooterInSection:](<../uitableviewdelegate/tableview(__viewforfooterinsection_).md>) method takes priority.

## See Also

### Providing cells, headers, and footers

- [- tableView:cellForRowAtIndexPath:](<tableview(__cellforrowat_).md>) — Asks the data source for a cell to insert in a particular location of the table view.
- [- tableView:titleForHeaderInSection:](<tableview(__titleforheaderinsection_).md>) — Asks the data source for the title of the header of the specified section of the table view.
