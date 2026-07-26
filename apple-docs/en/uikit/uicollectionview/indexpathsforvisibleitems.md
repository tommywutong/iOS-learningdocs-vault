---
title: indexPathsForVisibleItems
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionview/indexpathsforvisibleitems
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/indexpathsforvisibleitems'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/indexpathsforvisibleitems.json'
content_hash: 'sha256:723e7c41519aa4ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# indexPathsForVisibleItems

<sub>Instance Property</sub>

An array of the visible items in the collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var indexPathsForVisibleItems: [IndexPath] { get }
```

## Discussion

The value of this property is an unsorted array of [NSIndexPath](../../foundation/nsindexpath.md) objects, each of which corresponds to a visible cell in the collection view. This array doesn’t include any supplementary views that are currently visible. If there are no visible items, the value of this property is an empty array.

## See Also

### Related Documentation

- [visibleCells](visiblecells.md) — An array of visible cells currently displayed by the collection view.

### Locating items and views in the collection view

- [- indexPathForItemAtPoint:](<indexpathforitem(at_).md>) — Gets the index path of the item at the specified point in the collection view.
- [- indexPathForCell:](<indexpath(for_).md>) — Gets the index path of the specified cell.
- [- cellForItemAtIndexPath:](<cellforitem(at_).md>) — Gets the cell object at the index path you specify.
- [- indexPathsForVisibleSupplementaryElementsOfKind:](<indexpathsforvisiblesupplementaryelements(ofkind_).md>) — Gets the index paths of all visible supplementary views of the specified type.
- [- supplementaryViewForElementKind:atIndexPath:](<supplementaryview(forelementkind_at_).md>) — Gets the supplementary view at the specified index path.
- [- visibleSupplementaryViewsOfKind:](<visiblesupplementaryviews(ofkind_).md>) — Gets an array of the visible supplementary views of the specified kind.
