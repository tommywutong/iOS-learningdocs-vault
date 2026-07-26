---
title: 'reconfigureItems(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/reconfigureitems(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/reconfigureitems(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/reconfigureitems%28_%3A%29.json'
content_hash: 'sha256:0e8078fc8d8ea08c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSnapshot](../nsdiffabledatasourcesnapshot-swift.struct.md)

# reconfigureItems(_:)

<sub>Instance Method</sub>

Updates the data for the items you specify in the snapshot, preserving the existing cells for the items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
mutating func reconfigureItems(_ identifiers: [ItemIdentifierType])
```

## Parameters

- `identifiers` — An array of identifiers corresponding to the items to update data for in the snapshot.

## Discussion

To update the contents of existing (including prefetched) cells without replacing them with new cells, use this method instead of [reloadItems(_:)](<reloaditems(__).md>). For optimal performance, choose to reconfigure items instead of reloading items unless you have an explicit need to replace the existing cell with a new cell.

Your cell provider must dequeue the same type of cell for the provided index path, and must return the same existing cell for a given index path. Because this method reconfigures existing cells, the collection view or table view doesn’t call `prepareForReuse` for each cell dequeued. If you need to return a different type of cell for an index path, use [reloadItems(_:)](<reloaditems(__).md>) instead.

If your cells are self-sizing, the collection view or table view resizes your cells after reconfiguring them.

Set the `animatingDifferences` parameter to tell the collection view or table view whether to animate any size or layout changes that are a result of reconfiguration when you apply the snapshot to your data source. To avoid animations when setting specific properties, use [+ performWithoutAnimation:](<../uiview/performwithoutanimation(__).md>) in your cell configuration logic.

If your collection view or table view uses a diffable data source, use this method. If your collection view uses a custom implementation of `UICollectionViewDataSource`, use [- reconfigureItemsAtIndexPaths:](<../uicollectionview/reconfigureitems(at_).md>) instead. If your table view uses a custom implementation of `UITableViewDataSource`, use [- reconfigureRowsAtIndexPaths:](<../uitableview/reconfigurerows(at_).md>) instead.

## See Also

### Reloading data

- [reconfiguredItemIdentifiers](reconfigureditemidentifiers.md) — Identifies the items reconfigured by the changes to the snapshot.
- [reloadItems(_:)](<reloaditems(__).md>) — Reloads the data within the specified items in the snapshot.
- [reloadedItemIdentifiers](reloadeditemidentifiers.md) — Identifies the items reloaded by the changes to the snapshot.
- [reloadSections(_:)](<reloadsections(__).md>) — Reloads the data within the specified sections of the snapshot.
- [reloadedSectionIdentifiers](reloadedsectionidentifiers.md) — Identifies the sections reloaded by the changes to the snapshot.
