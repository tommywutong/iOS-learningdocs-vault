---
title: 'tableView(_:willDisplay:forRowAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdelegate/tableview(_:willdisplay:forrowat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:willdisplay:forrowat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%28_%3Awilldisplay%3Aforrowat%3A%29.json'
content_hash: 'sha256:7ea208e8ed6358bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView(_:willDisplay:forRowAt:)

<sub>Instance Method</sub>

Tells the delegate the table view is about to draw a cell for a particular row.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, willDisplay cell: UITableViewCell, forRowAt indexPath: IndexPath)
```

## Parameters

- `tableView` — The table view informing the delegate of this impending event.

- `cell` — A cell that `tableView` is going to use when drawing the row.

- `indexPath` — An index path locating the row in `tableView`.

## Discussion

A table view sends this message to its delegate just before it uses `cell` to draw a row, thereby permitting the delegate to customize the cell object before it is displayed. This method gives the delegate a chance to override state-based properties set earlier by the table view, such as selection and background color. After the delegate returns, the table view sets only the alpha and frame properties, and then only when animating rows as they slide in or out.

## See Also

### Related Documentation

- [- tableView:cellForRowAtIndexPath:](<../uitableviewdatasource/tableview(__cellforrowat_).md>) — Asks the data source for a cell to insert in a particular location of the table view.
- [- prepareForReuse](<../uitableviewcell/prepareforreuse().md>) — Prepares a reusable cell for reuse by the table view’s delegate.

### Configuring rows for the table view

- [- tableView:indentationLevelForRowAtIndexPath:](<tableview(__indentationlevelforrowat_).md>) — Asks the delegate to return the level of indentation for a row in a given section.
- [- tableView:shouldSpringLoadRowAtIndexPath:withContext:](<tableview(__shouldspringloadrowat_with_).md>) — Called to let you fine tune the spring-loading behavior of the rows in a table.
