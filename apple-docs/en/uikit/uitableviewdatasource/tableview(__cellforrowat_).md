---
title: 'tableView(_:cellForRowAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdatasource/tableview(_:cellforrowat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdatasource/tableview(_:cellforrowat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdatasource/tableview%28_%3Acellforrowat%3A%29.json'
content_hash: 'sha256:bbb4915307119372'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDataSource](../uitableviewdatasource.md)

# tableView(_:cellForRowAt:)

<sub>Instance Method</sub>

Asks the data source for a cell to insert in a particular location of the table view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell
```

## Parameters

- `tableView` — A table-view object requesting the cell.

- `indexPath` — An index path locating a row in `tableView`.

## Return Value

An object inheriting from [UITableViewCell](../uitableviewcell.md) that the table view can use for the specified row. UIKit raises an assertion if you return `nil`.

## Discussion

In your implementation, create and configure an appropriate cell for the given index path. Create your cell using the table view’s [- dequeueReusableCellWithIdentifier:forIndexPath:](<../uitableview/dequeuereusablecell(withidentifier_for_).md>) method, which recycles or creates the cell for you. After creating the cell, update the properties of the cell with appropriate data values.

Never call this method yourself. If you want to retrieve cells from your table, call the table view’s [- cellForRowAtIndexPath:](<../uitableview/cellforrow(at_).md>) method instead.

## See Also

### Providing cells, headers, and footers

- [- tableView:titleForHeaderInSection:](<tableview(__titleforheaderinsection_).md>) — Asks the data source for the title of the header of the specified section of the table view.
- [- tableView:titleForFooterInSection:](<tableview(__titleforfooterinsection_).md>) — Asks the data source for the title of the footer of the specified section of the table view.
