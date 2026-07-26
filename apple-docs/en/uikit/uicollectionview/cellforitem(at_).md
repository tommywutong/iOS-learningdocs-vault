---
title: 'cellForItem(at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionview/cellforitem(at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/cellforitem(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/cellforitem%28at%3A%29.json'
content_hash: 'sha256:715f85ef1784454b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# cellForItem(at:)

<sub>Instance Method</sub>

Gets the cell object at the index path you specify.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func cellForItem(at indexPath: IndexPath) -> UICollectionViewCell?
```

## Parameters

- `indexPath` — The index path that specifies the section and item number of the cell.

## Return Value

The cell object at the corresponding index path. In versions of iOS earlier than iOS 15, this method returns `nil` if the cell isn’t visible or if `indexPath` is out of range. In iOS 15 and later, this method returns a non-`nil` cell if the collection view retains a prepared cell at the specified index path, even if the cell isn’t currently visible.

## Discussion

In iOS 15 and later, the collection view retains a prepared cell in the following situations:

- Cells that the collection view prefetches and retains in its cache of prepared cells, but that aren’t visible because the collection view hasn’t displayed them yet.
- Cells that the collection view finishes displaying and continues to retain in its cache of prepared cells because they remain near the visible region and might scroll back into view.
- The cell that contains the first responder.
- The cell that has focus.

## See Also

### Locating items and views in the collection view

- [- indexPathForItemAtPoint:](<indexpathforitem(at_).md>) — Gets the index path of the item at the specified point in the collection view.
- [indexPathsForVisibleItems](indexpathsforvisibleitems.md) — An array of the visible items in the collection view.
- [- indexPathForCell:](<indexpath(for_).md>) — Gets the index path of the specified cell.
- [- indexPathsForVisibleSupplementaryElementsOfKind:](<indexpathsforvisiblesupplementaryelements(ofkind_).md>) — Gets the index paths of all visible supplementary views of the specified type.
- [- supplementaryViewForElementKind:atIndexPath:](<supplementaryview(forelementkind_at_).md>) — Gets the supplementary view at the specified index path.
- [- visibleSupplementaryViewsOfKind:](<visiblesupplementaryviews(ofkind_).md>) — Gets an array of the visible supplementary views of the specified kind.
