---
title: 'targetIndexPath(forInteractivelyMovingItem:withPosition:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewlayout/targetindexpath(forinteractivelymovingitem:withposition:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayout/targetindexpath(forinteractivelymovingitem:withposition:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayout/targetindexpath%28forinteractivelymovingitem%3Awithposition%3A%29.json'
content_hash: 'sha256:76b83d2c7ea288e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayout](../uicollectionviewlayout.md)

# targetIndexPath(forInteractivelyMovingItem:withPosition:)

<sub>Instance Method</sub>

Retrieves the index path to for an item when it is at the specified location in the collection view’s bounds.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func targetIndexPath(forInteractivelyMovingItem previousIndexPath: IndexPath, withPosition position: CGPoint) -> IndexPath
```

## Parameters

- `previousIndexPath` — The previous index path of the item. Use this value to identify the item.

- `position` — The target point in the collection view’s bounds. Use this value to compute the new index path for the item.

## Return Value

The index path corresponding to the specified location in the collection view.

## Discussion

During interactive movement of an item, this method maps points in the collection view’s bounds rectangle to index paths that correspond to the locations of those points. The default implementation of this method searches for an existing cell at the specified location and returns the index path of that cell. If there are multiple cells at the same location, the method returns the topmost cell—that is, the cell whose [zIndex](../uicollectionviewlayoutattributes/zindex.md) layout attribute value is greatest.

You can override this method as needed to change how the index path is determined. For example, you might return the index path of the cell that has the lowest [zIndex](../uicollectionviewlayoutattributes/zindex.md) value instead of the highest. If you override this method, you do not need to call `super`.

## See Also

### Responding to collection view updates

- [- prepareForCollectionViewUpdates:](<prepare(forcollectionviewupdates_).md>) — Notifies the layout object that the contents of the collection view are about to change.
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
