---
title: 'register(_:forCellReuseIdentifier:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uitableview/register(_:forcellreuseidentifier:)-5q6bo'
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/register(_:forcellreuseidentifier:)-5q6bo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/register%28_%3Aforcellreuseidentifier%3A%29-5q6bo.json'
content_hash: 'sha256:bfe2eeb410357769'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# register(_:forCellReuseIdentifier:)

<sub>Instance Method</sub>

Registers a nib object that contains a cell with the table view under a specified identifier.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func register(_ nib: UINib?, forCellReuseIdentifier identifier: String)
```

## Parameters

- `nib` — A nib object that specifies the nib file to use to create the cell.

- `identifier` — The reuse identifier for the cell. This parameter must not be `nil` and must not be an empty string.

## Discussion

Before dequeueing any cells, call this method or the [- registerClass:forCellReuseIdentifier:](<register(__forcellreuseidentifier_)-3l3ct.md>) method to tell the table view how to create new cells. If a cell of the specified type isn’t currently in a reuse queue, the table view uses the provided information to create a new cell object automatically.

If you previously registered a class or nib file with the same reuse identifier, the nib you specify in the `nib` parameter replaces the old entry. You may specify `nil` for `nib` if you want to unregister the nib from the specified reuse identifier.

## See Also

### Related Documentation

- [- tableView:cellForRowAtIndexPath:](<../uitableviewdatasource/tableview(__cellforrowat_).md>) — Asks the data source for a cell to insert in a particular location of the table view.

### Recycling table view cells

- [- registerClass:forCellReuseIdentifier:](<register(__forcellreuseidentifier_)-3l3ct.md>) — Registers a class to use in creating new table cells.
- [- dequeueReusableCellWithIdentifier:forIndexPath:](<dequeuereusablecell(withidentifier_for_).md>) — Returns a reusable table-view cell object for the specified reuse identifier and adds it to the table.
- [- dequeueReusableCellWithIdentifier:](<dequeuereusablecell(withidentifier_).md>) — Returns a reusable table-view cell object after locating it by its identifier.
