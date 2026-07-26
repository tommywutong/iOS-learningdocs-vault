---
title: 'layoutAttributesForItem(at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewlayout/layoutattributesforitem(at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayout/layoutattributesforitem(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayout/layoutattributesforitem%28at%3A%29.json'
content_hash: 'sha256:a947321811f0b193'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayout](../uicollectionviewlayout.md)

# layoutAttributesForItem(at:)

<sub>Instance Method</sub>

Retrieves layout information for an item at the specified index path with a corresponding cell.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func layoutAttributesForItem(at indexPath: IndexPath) -> UICollectionViewLayoutAttributes?
```

## Parameters

- `indexPath` — The index path of the item.

## Return Value

A layout attributes object containing the information to apply to the item’s cell.

## Discussion

Subclasses must override this method and use it to return layout information for items in the collection view. You use this method to provide layout information only for items that have a corresponding cell. Do not use it for supplementary views or decoration views.

## See Also

### Providing layout attributes

- [layoutAttributesClass](layoutattributesclass.md) — The class to use when creating layout attributes objects.
- [- prepareLayout](<prepare().md>) — Tells the layout object to update the current layout.
- [- layoutAttributesForElementsInRect:](<layoutattributesforelements(in_).md>) — Retrieves the layout attributes for all of the cells and views in the specified rectangle.
- [- layoutAttributesForInteractivelyMovingItemAtIndexPath:withTargetPosition:](<layoutattributesforinteractivelymovingitem(at_withtargetposition_).md>) — Retrieves the layout attributes of an item when it is being moved interactively by the user.
- [- layoutAttributesForSupplementaryViewOfKind:atIndexPath:](<layoutattributesforsupplementaryview(ofkind_at_).md>) — Retrieves the layout attributes for the specified supplementary view.
- [- layoutAttributesForDecorationViewOfKind:atIndexPath:](<layoutattributesfordecorationview(ofkind_at_).md>) — Retrieves the layout attributes for the specified decoration view.
- [- targetContentOffsetForProposedContentOffset:](<targetcontentoffset(forproposedcontentoffset_).md>) — Retrieves the content offset to use after an animated layout update or change.
- [- targetContentOffsetForProposedContentOffset:withScrollingVelocity:](<targetcontentoffset(forproposedcontentoffset_withscrollingvelocity_).md>) — Retrieves the point at which to stop scrolling.
