---
title: 'reconfigureRows(at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableview/reconfigurerows(at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/reconfigurerows(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/reconfigurerows%28at%3A%29.json'
content_hash: 'sha256:f1fe3f3f2a56cc34'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# reconfigureRows(at:)

<sub>Instance Method</sub>

Updates the data for the rows at the index paths you specify, preserving the existing cells for the rows.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func reconfigureRows(at indexPaths: [IndexPath])
```

## Parameters

- `indexPaths` — An array of [NSIndexPath](../../foundation/nsindexpath.md) objects identifying the items you want to update.

## Discussion

To update the contents of existing (including prefetched) cells without replacing them with new cells, use this method instead of [- reloadRowsAtIndexPaths:withRowAnimation:](<reloadrows(at_with_).md>). For optimal performance, choose to reconfigure rows instead of reloading rows unless you have an explicit need to replace the existing cell with a new cell.

Your cell provider must dequeue the same type of cell for the provided index path, and must return the same existing cell for a given index path. Because this method reconfigures existing cells, the table view doesn’t call [- prepareForReuse](<../uitableviewcell/prepareforreuse().md>) for each cell dequeued. If you need to return a different type of cell for an index path, use [- reloadRowsAtIndexPaths:withRowAnimation:](<reloadrows(at_with_).md>) instead.

If your cells are self-sizing, the table view resizes your cells after reconfiguring them.

By default, the table view animates any size or layout changes that are a result of reconfiguration. To reconfigure cells without animation, use `UIView`’s [+ performWithoutAnimation:](<../uiview/performwithoutanimation(__).md>) when you call this method. Alternatively, to avoid animations when setting specific properties, use [+ performWithoutAnimation:](<../uiview/performwithoutanimation(__).md>) in your cell configuration logic.

If your table view uses a custom implementation of `UITableViewDataSource`, use this method. If your table view uses a diffable data source, use [reconfigureItems(_:)](<../nsdiffabledatasourcesnapshot-swift.struct/reconfigureitems(__).md>) (Swift) or [- reconfigureItemsWithIdentifiers:](<../nsdiffabledatasourcesnapshotreference/reconfigureitems(withidentifiers_).md>) (Objective-C) on `NSDiffableDataSourceSnapshot` instead.

## See Also

### Reloading the table view

- [hasUncommittedUpdates](hasuncommittedupdates.md) — A Boolean value that indicates whether the table view’s appearance contains changes that aren’t present in its data source.
- [- reloadData](<reloaddata().md>) — Reloads the rows and sections of the table view.
- [- reloadRowsAtIndexPaths:withRowAnimation:](<reloadrows(at_with_).md>) — Reloads the specified rows using the provided animation effect.
- [- reloadSections:withRowAnimation:](<reloadsections(__with_).md>) — Reloads the specified sections using the provided animation effect.
- [- reloadSectionIndexTitles](<reloadsectionindextitles().md>) — Reloads the items in the index bar along the right side of the table view.
