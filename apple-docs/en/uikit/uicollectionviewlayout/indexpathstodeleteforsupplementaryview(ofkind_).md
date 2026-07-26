---
title: 'indexPathsToDeleteForSupplementaryView(ofKind:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewlayout/indexpathstodeleteforsupplementaryview(ofkind:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayout/indexpathstodeleteforsupplementaryview(ofkind:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayout/indexpathstodeleteforsupplementaryview%28ofkind%3A%29.json'
content_hash: 'sha256:83d3769b34fc448c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayout](../uicollectionviewlayout.md)

# indexPathsToDeleteForSupplementaryView(ofKind:)

<sub>Instance Method</sub>

Retrieves an array of index paths representing the supplementary views to remove.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func indexPathsToDeleteForSupplementaryView(ofKind elementKind: String) -> [IndexPath]
```

## Parameters

- `elementKind` — The specific type of supplementary view.

## Return Value

An array of [NSIndexPath](../../foundation/nsindexpath.md) objects indicating the supplementary views you want to remove or an empty array if you do not want to remove any views of the given kind.

## Discussion

The collection view calls this method whenever you delete cells or sections to the collection view. Implementing this method gives your layout object an opportunity to remove any supplementary views that are no longer needed.

The collection view calls this method between its calls to [- prepareForCollectionViewUpdates:](<prepare(forcollectionviewupdates_).md>) and [- finalizeCollectionViewUpdates](<finalizecollectionviewupdates().md>).

## See Also

### Responding to collection view updates

- [- prepareForCollectionViewUpdates:](<prepare(forcollectionviewupdates_).md>) — Notifies the layout object that the contents of the collection view are about to change.
- [- finalizeCollectionViewUpdates](<finalizecollectionviewupdates().md>) — Performs any additional animations or clean up needed during a collection view update.
- [- indexPathsToInsertForSupplementaryViewOfKind:](<indexpathstoinsertforsupplementaryview(ofkind_).md>) — Retrieves an array of index paths for the supplementary views you want to add to the layout.
- [- indexPathsToInsertForDecorationViewOfKind:](<indexpathstoinsertfordecorationview(ofkind_).md>) — Retrieves an array of index paths representing the decoration views to add.
- [- initialLayoutAttributesForAppearingItemAtIndexPath:](<initiallayoutattributesforappearingitem(at_).md>) — Retrieves the starting layout information for an item being inserted into the collection view.
- [- initialLayoutAttributesForAppearingSupplementaryElementOfKind:atIndexPath:](<initiallayoutattributesforappearingsupplementaryelement(ofkind_at_).md>) — Retrieves the starting layout information for a supplementary view being inserted into the collection view.
- [- initialLayoutAttributesForAppearingDecorationElementOfKind:atIndexPath:](<initiallayoutattributesforappearingdecorationelement(ofkind_at_).md>) — Retrieves the starting layout information for a decoration view being inserted into the collection view.
- [- indexPathsToDeleteForDecorationViewOfKind:](<indexpathstodeletefordecorationview(ofkind_).md>) — Retrieves an array of index paths representing the decoration views to remove.
- [- finalLayoutAttributesForDisappearingItemAtIndexPath:](<finallayoutattributesfordisappearingitem(at_).md>) — Retrieves the final layout information for an item that is about to be removed from the collection view.
- [- finalLayoutAttributesForDisappearingSupplementaryElementOfKind:atIndexPath:](<finallayoutattributesfordisappearingsupplementaryelement(ofkind_at_).md>) — Retrieves the final layout information for a supplementary view that is about to be removed from the collection view.
- [- finalLayoutAttributesForDisappearingDecorationElementOfKind:atIndexPath:](<finallayoutattributesfordisappearingdecorationelement(ofkind_at_).md>) — Retrieves the final layout information for a decoration view that is about to be removed from the collection view.
- [- targetIndexPathForInteractivelyMovingItem:withPosition:](<targetindexpath(forinteractivelymovingitem_withposition_).md>) — Retrieves the index path to for an item when it is at the specified location in the collection view’s bounds.
