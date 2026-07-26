---
title: 'reconfigureItems(at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionview/reconfigureitems(at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/reconfigureitems(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/reconfigureitems%28at%3A%29.json'
content_hash: 'sha256:e907286f2ec4f7f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# reconfigureItems(at:)

<sub>Instance Method</sub>

Updates the data for the items at the index paths you specify, preserving the existing cells for the items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func reconfigureItems(at indexPaths: [IndexPath])
```

## Parameters

- `indexPaths` — An array of [NSIndexPath](../../foundation/nsindexpath.md) objects identifying the items you want to update.

## Discussion

To update the contents of existing (including prefetched) cells without replacing them with new cells, use this method instead of [- reloadItemsAtIndexPaths:](<reloaditems(at_).md>). For optimal performance, choose to reconfigure items instead of reloading items unless you have an explicit need to replace the existing cell with a new cell.

Your cell provider must dequeue the same type of cell for the provided index path, and must return the same existing cell for a given index path. Because this method reconfigures existing cells, the collection view doesn’t call [- prepareForReuse](<../uicollectionreusableview/prepareforreuse().md>) for each cell dequeued. If you need to return a different type of cell for an index path, use [- reloadItemsAtIndexPaths:](<reloaditems(at_).md>) instead.

If your cells are self-sizing, the collection view resizes your cells after reconfiguring them.

By default, the collection view animates any size or layout changes that result from reconfiguration. To reconfigure cells without animation, use `UIView`’s [+ performWithoutAnimation:](<../uiview/performwithoutanimation(__).md>) when you call this method. Alternatively, to avoid animations when setting specific properties, use [+ performWithoutAnimation:](<../uiview/performwithoutanimation(__).md>) in your cell configuration logic.

If your collection view uses a custom implementation of `UICollectionViewDataSource`, use this method. If your collection view uses a diffable data source, use [reconfigureItems(_:)](<../nsdiffabledatasourcesnapshot-swift.struct/reconfigureitems(__).md>) (Swift) or [- reconfigureItemsWithIdentifiers:](<../nsdiffabledatasourcesnapshotreference/reconfigureitems(withidentifiers_).md>) (Objective-C) on `NSDiffableDataSourceSnapshot` instead.

## See Also

### Reloading content

- [hasUncommittedUpdates](hasuncommittedupdates.md) — A Boolean value that indicates whether the collection view contains drop placeholders or is reordering its items as part of handling a drop.
- [- reloadData](<reloaddata().md>) — Reloads all of the data for the collection view.
- [- reloadSections:](<reloadsections(__).md>) — Reloads the data in the specified sections of the collection view.
- [- reloadItemsAtIndexPaths:](<reloaditems(at_).md>) — Reloads just the items at the specified index paths.
