---
title: 'prepare(forCollectionViewUpdates:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewlayout/prepare(forcollectionviewupdates:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayout/prepare(forcollectionviewupdates:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayout/prepare%28forcollectionviewupdates%3A%29.json'
content_hash: 'sha256:a4f09cb0d24bed87'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayout](../uicollectionviewlayout.md)

# prepare(forCollectionViewUpdates:)

<sub>Instance Method</sub>

Notifies the layout object that the contents of the collection view are about to change.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func prepare(forCollectionViewUpdates updateItems: [UICollectionViewUpdateItem])
```

## Parameters

- `updateItems` — An array of [UICollectionViewUpdateItem](../uicollectionviewupdateitem.md) objects that identify the changes being made.

## Discussion

When items are inserted or deleted, the collection view notifies its layout object so that it can adjust the layout as needed. The first step in that process is to call this method to let the layout object know what changes to expect. After that, additional calls are made to gather layout information for inserted, deleted, and moved items that are going to be animated around the collection view.

## See Also

### Responding to collection view updates

- [- finalizeCollectionViewUpdates](<finalizecollectionviewupdates().md>) — Performs any additional animations or clean up needed during a collection view update.
- [- indexPathsToInsertForSupplementaryViewOfKind:](<indexpathstoinsertforsupplementaryview(ofkind_).md>) — Retrieves an array of index paths for the supplementary views you want to add to the layout.
- [- indexPathsToInsertForDecorationViewOfKind:](<indexpathstoinsertfordecorationview(ofkind_).md>) — Retrieves an array of index paths representing the decoration views to add.
- [- initialLayoutAttributesForAppearingItemAtIndexPath:](<initiallayoutattributesforappearingitem(at_).md>) — Retrieves the starting layout information for an item being inserted into the collection view.
- [- initialLayoutAttributesForAppearingSupplementaryElementOfKind:atIndexPath:](<initiallayoutattributesforappearingsupplementaryelement(ofkind_at_).md>) — Retrieves the starting layout information for a supplementary view being inserted into the collection view.
- [- initialLayoutAttributesForAppearingDecorationElementOfKind:atIndexPath:](<initiallayoutattributesforappearingdecorationelement(ofkind_at_).md>) — Retrieves the starting layout information for a decoration view being inserted into the collection view.
- [- indexPathsToDeleteForSupplementaryViewOfKind:](<indexpathstodeleteforsupplementaryview(ofkind_).md>) — Retrieves an array of index paths representing the supplementary views to remove.
- [- indexPathsToDeleteForDecorationViewOfKind:](<indexpathstodeletefordecorationview(ofkind_).md>) — Retrieves an array of index paths representing the decoration views to remove.
- [- finalLayoutAttributesForDisappearingItemAtIndexPath:](<finallayoutattributesfordisappearingitem(at_).md>) — Retrieves the final layout information for an item that is about to be removed from the collection view.
- [- finalLayoutAttributesForDisappearingSupplementaryElementOfKind:atIndexPath:](<finallayoutattributesfordisappearingsupplementaryelement(ofkind_at_).md>) — Retrieves the final layout information for a supplementary view that is about to be removed from the collection view.
- [- finalLayoutAttributesForDisappearingDecorationElementOfKind:atIndexPath:](<finallayoutattributesfordisappearingdecorationelement(ofkind_at_).md>) — Retrieves the final layout information for a decoration view that is about to be removed from the collection view.
- [- targetIndexPathForInteractivelyMovingItem:withPosition:](<targetindexpath(forinteractivelymovingitem_withposition_).md>) — Retrieves the index path to for an item when it is at the specified location in the collection view’s bounds.
