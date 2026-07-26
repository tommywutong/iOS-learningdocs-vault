---
title: 'indexPathForItem(at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionview/indexpathforitem(at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/indexpathforitem(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/indexpathforitem%28at%3A%29.json'
content_hash: 'sha256:c164238064652a83'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# indexPathForItem(at:)

<sub>Instance Method</sub>

Gets the index path of the item at the specified point in the collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func indexPathForItem(at point: CGPoint) -> IndexPath?
```

## Parameters

- `point` — A point in the collection view’s coordinate system.

## Return Value

The index path of the item at the specified point or `nil` if no item was found at the specified point.

## Discussion

This method relies on the layout information provided by the associated layout object to determine which item contains the point.

## See Also

### Locating items and views in the collection view

- [indexPathsForVisibleItems](indexpathsforvisibleitems.md) — An array of the visible items in the collection view.
- [- indexPathForCell:](<indexpath(for_).md>) — Gets the index path of the specified cell.
- [- cellForItemAtIndexPath:](<cellforitem(at_).md>) — Gets the cell object at the index path you specify.
- [- indexPathsForVisibleSupplementaryElementsOfKind:](<indexpathsforvisiblesupplementaryelements(ofkind_).md>) — Gets the index paths of all visible supplementary views of the specified type.
- [- supplementaryViewForElementKind:atIndexPath:](<supplementaryview(forelementkind_at_).md>) — Gets the supplementary view at the specified index path.
- [- visibleSupplementaryViewsOfKind:](<visiblesupplementaryviews(ofkind_).md>) — Gets an array of the visible supplementary views of the specified kind.
