---
title: 'reconfigureItems(withIdentifiers:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nsdiffabledatasourcesnapshotreference/reconfigureitems(withidentifiers:)'
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshotreference/reconfigureitems(withidentifiers:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesnapshotreference/reconfigureitems%28withidentifiers%3A%29.json'
content_hash: 'sha256:7d57448ad114dfea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSnapshotReference](../nsdiffabledatasourcesnapshotreference.md)

# reconfigureItems(withIdentifiers:)

<sub>Instance Method</sub>

Updates the data for the items you specify in the snapshot, preserving the existing cells for the items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func reconfigureItems(withIdentifiers identifiers: [Any])
```

## Parameters

- `identifiers` — An array of identifiers corresponding to the items to update data for in the snapshot.

## Discussion

To update the contents of existing (including prefetched) cells without replacing them with new cells, use this method instead of [- reloadItemsWithIdentifiers:](<reloaditems(withidentifiers_).md>). For optimal performance, choose to reconfigure items instead of reloading items unless you have an explicit need to replace the existing cell with a new cell.

Your cell provider must dequeue the same type of cell for the provided index path, and must return the same existing cell for a given index path. Because this method reconfigures existing cells, the collection view or table view doesn’t call `prepareForReuse` for each cell dequeued. If you need to return a different type of cell for an index path, use [- reloadItemsWithIdentifiers:](<reloaditems(withidentifiers_).md>) instead.

If your cells are self-sizing, the collection view or table view resizes your cells after reconfiguring them.

Set the `animatingDifferences` parameter to tell the collection view or table view whether to animate any size or layout changes that are a result of reconfiguration when you apply the snapshot to your data source. To avoid animations when setting specific properties, use [+ performWithoutAnimation:](<../uiview/performwithoutanimation(__).md>) in your cell configuration logic.

If your collection view or table view uses a diffable data source, use this method. If your collection view uses a custom implementation of `UICollectionViewDataSource`, use [- reconfigureItemsAtIndexPaths:](<../uicollectionview/reconfigureitems(at_).md>) instead. If your table view uses a custom implementation of `UITableViewDataSource`, use [- reconfigureRowsAtIndexPaths:](<../uitableview/reconfigurerows(at_).md>) instead.

## See Also

### Reloading data

- [reconfiguredItemIdentifiers](reconfigureditemidentifiers.md) — Identifies the items reconfigured by the changes to the snapshot.
- [- reloadItemsWithIdentifiers:](<reloaditems(withidentifiers_).md>) — Reloads the data within the specified items in the snapshot.
- [reloadedItemIdentifiers](reloadeditemidentifiers.md) — Identifies the items reloaded by the changes to the snapshot.
- [- reloadSectionsWithIdentifiers:](<reloadsections(withidentifiers_).md>) — Reloads the data within the specified sections of the snapshot.
- [reloadedSectionIdentifiers](reloadedsectionidentifiers.md) — Identifies the sections reloaded by the changes to the snapshot.
