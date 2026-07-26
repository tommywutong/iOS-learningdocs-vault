---
title: 'indexPathsForVisibleSupplementaryElements(ofKind:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionview/indexpathsforvisiblesupplementaryelements(ofkind:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/indexpathsforvisiblesupplementaryelements(ofkind:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/indexpathsforvisiblesupplementaryelements%28ofkind%3A%29.json'
content_hash: 'sha256:9a814cfe2fd308c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# indexPathsForVisibleSupplementaryElements(ofKind:)

<sub>Instance Method</sub>

Gets the index paths of all visible supplementary views of the specified type.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func indexPathsForVisibleSupplementaryElements(ofKind elementKind: String) -> [IndexPath]
```

## Parameters

- `elementKind` — The kind of supplementary view to locate. This value is defined by the layout object. This parameter must not be `nil`.

## Return Value

An array of [NSIndexPath](../../foundation/nsindexpath.md) objects, each of which corresponds to a visible supplementary view in the collection view. If there are no visible supplementary views, this method returns an empty array.

## See Also

### Locating items and views in the collection view

- [- indexPathForItemAtPoint:](<indexpathforitem(at_).md>) — Gets the index path of the item at the specified point in the collection view.
- [indexPathsForVisibleItems](indexpathsforvisibleitems.md) — An array of the visible items in the collection view.
- [- indexPathForCell:](<indexpath(for_).md>) — Gets the index path of the specified cell.
- [- cellForItemAtIndexPath:](<cellforitem(at_).md>) — Gets the cell object at the index path you specify.
- [- supplementaryViewForElementKind:atIndexPath:](<supplementaryview(forelementkind_at_).md>) — Gets the supplementary view at the specified index path.
- [- visibleSupplementaryViewsOfKind:](<visiblesupplementaryviews(ofkind_).md>) — Gets an array of the visible supplementary views of the specified kind.
