---
title: 'init(style:reuseIdentifier:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewcell/init(style:reuseidentifier:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/init(style:reuseidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/init%28style%3Areuseidentifier%3A%29.json'
content_hash: 'sha256:7af75b2dc26ae4df'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# init(style:reuseIdentifier:)

<sub>Initializer</sub>

Initializes a table cell with a style and a reuse identifier and returns it to the caller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(style: UITableViewCell.CellStyle, reuseIdentifier: String?)
```

## Parameters

- `style` — A constant indicating a cell style. See [CellStyle](cellstyle.md) for descriptions of these constants.

- `reuseIdentifier` — A string used to identify the cell object if it is to be reused for drawing multiple rows of a table view. Pass `nil` if the cell object is not to be reused. You should use the same reuse identifier for all cells of the same form.

## Return Value

An initialized [UITableViewCell](../uitableviewcell.md) object or `nil` if the object could not be created.

## Discussion

This method is the designated initializer for the class. The reuse identifier is associated with those cells (rows) of a table view that have the same general configuration, minus cell content. In its implementation of [- tableView:cellForRowAtIndexPath:](<../uitableviewdatasource/tableview(__cellforrowat_).md>), the table view’s data source calls the `UITableView` method [- dequeueReusableCellWithIdentifier:](<../uitableview/dequeuereusablecell(withidentifier_).md>), passing in a reuse identifier, to obtain the cell object to use as the basis for the current row.

If you want a table cell that has a configuration different that those defined by `UITableViewCell` for `style`, you must create your own custom cell. If you want to set the row height of cells on an individual basis, implement the delegate method [- tableView:heightForRowAtIndexPath:](<../uitableviewdelegate/tableview(__heightforrowat_).md>).

## See Also

### Creating a table view cell

- [CellStyle](cellstyle.md) — An enumeration for the various styles of cells.
- [- initWithCoder:](<init(coder_).md>) — Creates a table view from data in an unarchiver.
