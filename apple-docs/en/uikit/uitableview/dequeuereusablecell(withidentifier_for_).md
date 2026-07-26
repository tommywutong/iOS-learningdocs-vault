---
title: 'dequeueReusableCell(withIdentifier:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableview/dequeuereusablecell(withidentifier:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/dequeuereusablecell(withidentifier:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/dequeuereusablecell%28withidentifier%3Afor%3A%29.json'
content_hash: 'sha256:2349487466adc6b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# dequeueReusableCell(withIdentifier:for:)

<sub>Instance Method</sub>

Returns a reusable table-view cell object for the specified reuse identifier and adds it to the table.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func dequeueReusableCell(withIdentifier identifier: String, for indexPath: IndexPath) -> UITableViewCell
```

## Parameters

- `identifier` — A string identifying the cell object to be reused. This parameter must not be `nil`.

- `indexPath` — The index path specifying the location of the cell. Always specify the index path provided to you by your data source object. This method uses the index path to perform additional configuration based on the cell’s position in the table view.

## Return Value

A [UITableViewCell](../uitableviewcell.md) object with the associated reuse identifier. This method always returns a valid cell.

## Discussion

Call this method only from the [- tableView:cellForRowAtIndexPath:](<../uitableviewdatasource/tableview(__cellforrowat_).md>) method of your table view data source object. This method returns an existing cell of the specified type, if one is available, or it creates and returns a new cell using the class or storyboard you provided earlier. Don’t call this method outside of your data source’s [- tableView:cellForRowAtIndexPath:](<../uitableviewdatasource/tableview(__cellforrowat_).md>) method. If you need to create cells at other times, call [- dequeueReusableCellWithIdentifier:](<dequeuereusablecell(withidentifier_).md>) instead.

> [!important] Important
> You must specify a cell with a matching identifier in your storyboard file. You may also register a class or nib file using the [- registerNib:forCellReuseIdentifier:](<register(__forcellreuseidentifier_)-5q6bo.md>) or [- registerClass:forCellReuseIdentifier:](<register(__forcellreuseidentifier_)-3l3ct.md>) method, but must do so before calling this method.

When creating new cells from your storyboard or nib file, this method loads the cell object and initializes it using its [- initWithCoder:](<init(coder_).md>) method. When creating cells from a registered class, this method creates the cell and initializes it by calling its [- initWithStyle:reuseIdentifier:](<../uitableviewcell/init(style_reuseidentifier_).md>) method. For nib-based cells, this method loads the cell object from the provided nib file. If an existing cell was available for reuse, this method calls the cell’s [- prepareForReuse](<../uitableviewcell/prepareforreuse().md>) method instead.

## See Also

### Recycling table view cells

- [- registerNib:forCellReuseIdentifier:](<register(__forcellreuseidentifier_)-5q6bo.md>) — Registers a nib object that contains a cell with the table view under a specified identifier.
- [- registerClass:forCellReuseIdentifier:](<register(__forcellreuseidentifier_)-3l3ct.md>) — Registers a class to use in creating new table cells.
- [- dequeueReusableCellWithIdentifier:](<dequeuereusablecell(withidentifier_).md>) — Returns a reusable table-view cell object after locating it by its identifier.
