---
title: 'dequeueReusableCell(withIdentifier:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableview/dequeuereusablecell(withidentifier:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/dequeuereusablecell(withidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/dequeuereusablecell%28withidentifier%3A%29.json'
content_hash: 'sha256:0388799348019ca1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# dequeueReusableCell(withIdentifier:)

<sub>Instance Method</sub>

Returns a reusable table-view cell object after locating it by its identifier.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func dequeueReusableCell(withIdentifier identifier: String) -> UITableViewCell?
```

## Parameters

- `identifier` — A string identifying the cell object to be reused. This parameter must not be `nil`.

## Return Value

A [UITableViewCell](../uitableviewcell.md) object with the associated `identifier`, or `nil` if no such object exists in the reusable-cell queue.

## Discussion

For performance reasons, a table view’s data source should generally reuse [UITableViewCell](../uitableviewcell.md) objects when it assigns cells to rows in its [- tableView:cellForRowAtIndexPath:](<../uitableviewdatasource/tableview(__cellforrowat_).md>) method. A table view maintains a queue or list of [UITableViewCell](../uitableviewcell.md) objects that the data source has marked for reuse. Call this method from your data source object when asked to provide a new cell for the table view. This method dequeues an existing cell if one is available or creates a new one using the class or nib file you previously registered. If no cell is available for reuse and you didn’t register a class or nib file, this method returns `nil`.

If you registered a class for the specified `identifier` and a new cell must be created, this method initializes the cell by calling its [- initWithStyle:reuseIdentifier:](<../uitableviewcell/init(style_reuseidentifier_).md>) method. For nib-based cells, this method loads the cell object from the provided nib file. If an existing cell was available for reuse, this method calls the cell’s [- prepareForReuse](<../uitableviewcell/prepareforreuse().md>) method instead.

## See Also

### Recycling table view cells

- [- registerNib:forCellReuseIdentifier:](<register(__forcellreuseidentifier_)-5q6bo.md>) — Registers a nib object that contains a cell with the table view under a specified identifier.
- [- registerClass:forCellReuseIdentifier:](<register(__forcellreuseidentifier_)-3l3ct.md>) — Registers a class to use in creating new table cells.
- [- dequeueReusableCellWithIdentifier:forIndexPath:](<dequeuereusablecell(withidentifier_for_).md>) — Returns a reusable table-view cell object for the specified reuse identifier and adds it to the table.
