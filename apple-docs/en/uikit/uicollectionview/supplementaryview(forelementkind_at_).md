---
title: 'supplementaryView(forElementKind:at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionview/supplementaryview(forelementkind:at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/supplementaryview(forelementkind:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/supplementaryview%28forelementkind%3Aat%3A%29.json'
content_hash: 'sha256:306f69af662631d7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# supplementaryView(forElementKind:at:)

<sub>Instance Method</sub>

Gets the supplementary view at the specified index path.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func supplementaryView(forElementKind elementKind: String, at indexPath: IndexPath) -> UICollectionReusableView?
```

## Parameters

- `elementKind` — The kind of supplementary view to locate. This value is defined by the layout object. This parameter must not be `nil`.

- `indexPath` — The index path of the supplementary view. This parameter must not be `nil`.

## Return Value

The specified supplementary view, or `nil` if the view could not be found.

## See Also

### Locating items and views in the collection view

- [- indexPathForItemAtPoint:](<indexpathforitem(at_).md>) — Gets the index path of the item at the specified point in the collection view.
- [indexPathsForVisibleItems](indexpathsforvisibleitems.md) — An array of the visible items in the collection view.
- [- indexPathForCell:](<indexpath(for_).md>) — Gets the index path of the specified cell.
- [- cellForItemAtIndexPath:](<cellforitem(at_).md>) — Gets the cell object at the index path you specify.
- [- indexPathsForVisibleSupplementaryElementsOfKind:](<indexpathsforvisiblesupplementaryelements(ofkind_).md>) — Gets the index paths of all visible supplementary views of the specified type.
- [- visibleSupplementaryViewsOfKind:](<visiblesupplementaryviews(ofkind_).md>) — Gets an array of the visible supplementary views of the specified kind.
