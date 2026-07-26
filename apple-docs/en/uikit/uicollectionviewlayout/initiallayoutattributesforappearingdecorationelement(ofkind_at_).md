---
title: 'initialLayoutAttributesForAppearingDecorationElement(ofKind:at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewlayout/initiallayoutattributesforappearingdecorationelement(ofkind:at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayout/initiallayoutattributesforappearingdecorationelement(ofkind:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayout/initiallayoutattributesforappearingdecorationelement%28ofkind%3Aat%3A%29.json'
content_hash: 'sha256:765fa83e57cd2fe8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayout](../uicollectionviewlayout.md)

# initialLayoutAttributesForAppearingDecorationElement(ofKind:at:)

<sub>Instance Method</sub>

Retrieves the starting layout information for a decoration view being inserted into the collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func initialLayoutAttributesForAppearingDecorationElement(ofKind elementKind: String, at decorationIndexPath: IndexPath) -> UICollectionViewLayoutAttributes?
```

## Parameters

- `elementKind` — A string that identifies the type of decoration view.

- `decorationIndexPath` — The index path of the item being inserted.

## Return Value

A layout attributes object that describes the position at which to place the corresponding decoration view.

## Discussion

This method is called after the [- prepareForCollectionViewUpdates:](<prepare(forcollectionviewupdates_).md>) method and before the [- finalizeCollectionViewUpdates](<finalizecollectionviewupdates().md>) method for any decoration views that are about to be inserted. Your implementation should return the layout information that describes the initial position and state of the view. The collection view uses this information as the starting point for any animations. (The end point of the animation is the view’s new location in the collection view.) If you return `nil`, the layout object uses the item’s final attributes for both the start and end points of the animation.

The default implementation of this method returns `nil`.

## See Also

### Responding to collection view updates

- [- prepareForCollectionViewUpdates:](<prepare(forcollectionviewupdates_).md>) — Notifies the layout object that the contents of the collection view are about to change.
- [- finalizeCollectionViewUpdates](<finalizecollectionviewupdates().md>) — Performs any additional animations or clean up needed during a collection view update.
- [- indexPathsToInsertForSupplementaryViewOfKind:](<indexpathstoinsertforsupplementaryview(ofkind_).md>) — Retrieves an array of index paths for the supplementary views you want to add to the layout.
- [- indexPathsToInsertForDecorationViewOfKind:](<indexpathstoinsertfordecorationview(ofkind_).md>) — Retrieves an array of index paths representing the decoration views to add.
- [- initialLayoutAttributesForAppearingItemAtIndexPath:](<initiallayoutattributesforappearingitem(at_).md>) — Retrieves the starting layout information for an item being inserted into the collection view.
- [- initialLayoutAttributesForAppearingSupplementaryElementOfKind:atIndexPath:](<initiallayoutattributesforappearingsupplementaryelement(ofkind_at_).md>) — Retrieves the starting layout information for a supplementary view being inserted into the collection view.
- [- indexPathsToDeleteForSupplementaryViewOfKind:](<indexpathstodeleteforsupplementaryview(ofkind_).md>) — Retrieves an array of index paths representing the supplementary views to remove.
- [- indexPathsToDeleteForDecorationViewOfKind:](<indexpathstodeletefordecorationview(ofkind_).md>) — Retrieves an array of index paths representing the decoration views to remove.
- [- finalLayoutAttributesForDisappearingItemAtIndexPath:](<finallayoutattributesfordisappearingitem(at_).md>) — Retrieves the final layout information for an item that is about to be removed from the collection view.
- [- finalLayoutAttributesForDisappearingSupplementaryElementOfKind:atIndexPath:](<finallayoutattributesfordisappearingsupplementaryelement(ofkind_at_).md>) — Retrieves the final layout information for a supplementary view that is about to be removed from the collection view.
- [- finalLayoutAttributesForDisappearingDecorationElementOfKind:atIndexPath:](<finallayoutattributesfordisappearingdecorationelement(ofkind_at_).md>) — Retrieves the final layout information for a decoration view that is about to be removed from the collection view.
- [- targetIndexPathForInteractivelyMovingItem:withPosition:](<targetindexpath(forinteractivelymovingitem_withposition_).md>) — Retrieves the index path to for an item when it is at the specified location in the collection view’s bounds.
