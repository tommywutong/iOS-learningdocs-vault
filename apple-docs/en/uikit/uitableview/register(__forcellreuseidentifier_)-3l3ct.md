---
title: 'register(_:forCellReuseIdentifier:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableview/register(_:forcellreuseidentifier:)-3l3ct'
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/register(_:forcellreuseidentifier:)-3l3ct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/register%28_%3Aforcellreuseidentifier%3A%29-3l3ct.json'
content_hash: 'sha256:453c1200d43b0a17'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# register(_:forCellReuseIdentifier:)

<sub>Instance Method</sub>

Registers a class to use in creating new table cells.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func register(_ cellClass: AnyClass?, forCellReuseIdentifier identifier: String)
```

## Parameters

- `cellClass` — The class of a cell that you want to use in the table (must be a [UITableViewCell](../uitableviewcell.md) subclass).

- `identifier` — The reuse identifier for the cell. This parameter must not be `nil` and must not be an empty string.

## Discussion

Prior to dequeueing any cells, call this method or the [- registerNib:forCellReuseIdentifier:](<register(__forcellreuseidentifier_)-5q6bo.md>) method to tell the table view how to create new cells. If a cell of the specified type isn’t currently in a reuse queue, the table view uses the provided information to create a new cell object automatically.

If you previously registered a class or nib file with the same reuse identifier, the class you specify in the `cellClass` parameter replaces the old entry. You may specify `nil` for `cellClass` if you want to unregister the class from the specified reuse identifier.

## See Also

### Recycling table view cells

- [- registerNib:forCellReuseIdentifier:](<register(__forcellreuseidentifier_)-5q6bo.md>) — Registers a nib object that contains a cell with the table view under a specified identifier.
- [- dequeueReusableCellWithIdentifier:forIndexPath:](<dequeuereusablecell(withidentifier_for_).md>) — Returns a reusable table-view cell object for the specified reuse identifier and adds it to the table.
- [- dequeueReusableCellWithIdentifier:](<dequeuereusablecell(withidentifier_).md>) — Returns a reusable table-view cell object after locating it by its identifier.
