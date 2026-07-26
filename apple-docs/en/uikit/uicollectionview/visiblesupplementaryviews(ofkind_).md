---
title: 'visibleSupplementaryViews(ofKind:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionview/visiblesupplementaryviews(ofkind:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/visiblesupplementaryviews(ofkind:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/visiblesupplementaryviews%28ofkind%3A%29.json'
content_hash: 'sha256:5d57ad3843f8a032'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# visibleSupplementaryViews(ofKind:)

<sub>Instance Method</sub>

Gets an array of the visible supplementary views of the specified kind.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func visibleSupplementaryViews(ofKind elementKind: String) -> [UICollectionReusableView]
```

## Parameters

- `elementKind` — The kind of supplementary view to locate. This value is defined by the layout object. This parameter must not be `nil`.

## Return Value

An array of the visible supplementary views. If no supplementary views are visible, the returned array is empty.

## See Also

### Locating items and views in the collection view

- [- indexPathForItemAtPoint:](<indexpathforitem(at_).md>) — Gets the index path of the item at the specified point in the collection view.
- [indexPathsForVisibleItems](indexpathsforvisibleitems.md) — An array of the visible items in the collection view.
- [- indexPathForCell:](<indexpath(for_).md>) — Gets the index path of the specified cell.
- [- cellForItemAtIndexPath:](<cellforitem(at_).md>) — Gets the cell object at the index path you specify.
- [- indexPathsForVisibleSupplementaryElementsOfKind:](<indexpathsforvisiblesupplementaryelements(ofkind_).md>) — Gets the index paths of all visible supplementary views of the specified type.
- [- supplementaryViewForElementKind:atIndexPath:](<supplementaryview(forelementkind_at_).md>) — Gets the supplementary view at the specified index path.
