---
title: 'layoutAttributesForInteractivelyMovingItem(at:withTargetPosition:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewlayout/layoutattributesforinteractivelymovingitem(at:withtargetposition:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayout/layoutattributesforinteractivelymovingitem(at:withtargetposition:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayout/layoutattributesforinteractivelymovingitem%28at%3Awithtargetposition%3A%29.json'
content_hash: 'sha256:04aa8e4ba62fa8af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayout](../uicollectionviewlayout.md)

# layoutAttributesForInteractivelyMovingItem(at:withTargetPosition:)

<sub>Instance Method</sub>

Retrieves the layout attributes of an item when it is being moved interactively by the user.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func layoutAttributesForInteractivelyMovingItem(at indexPath: IndexPath, withTargetPosition position: CGPoint) -> UICollectionViewLayoutAttributes
```

## Parameters

- `indexPath` — The index path of the item being moved.

- `position` — The current position of the item in the collection view’s coordinate system.

## Return Value

The layout attributes of the item while it is at the specified position.

## Discussion

When an item is moving because of user interactivity, the layout object uses this method to retrieve layout attributes to use for the item while it is at the specified position. The default implementation of this method returns a copy of the item’s existing attributes with two changes: the [center](../uicollectionviewlayoutattributes/center.md) point is set to the value in `position` and the [zIndex](../uicollectionviewlayoutattributes/zindex.md) value is set to [NSIntegerMax](../../objectivec/nsintegermax.md) so that the item floats above other items in the collection view.

Subclasses can override this method and modify additional layout attributes as needed. If you override this method, call `super` first to retrieve the item’s existing attributes and then make your changes to the returned structure.

## See Also

### Providing layout attributes

- [layoutAttributesClass](layoutattributesclass.md) — The class to use when creating layout attributes objects.
- [- prepareLayout](<prepare().md>) — Tells the layout object to update the current layout.
- [- layoutAttributesForElementsInRect:](<layoutattributesforelements(in_).md>) — Retrieves the layout attributes for all of the cells and views in the specified rectangle.
- [- layoutAttributesForItemAtIndexPath:](<layoutattributesforitem(at_).md>) — Retrieves layout information for an item at the specified index path with a corresponding cell.
- [- layoutAttributesForSupplementaryViewOfKind:atIndexPath:](<layoutattributesforsupplementaryview(ofkind_at_).md>) — Retrieves the layout attributes for the specified supplementary view.
- [- layoutAttributesForDecorationViewOfKind:atIndexPath:](<layoutattributesfordecorationview(ofkind_at_).md>) — Retrieves the layout attributes for the specified decoration view.
- [- targetContentOffsetForProposedContentOffset:](<targetcontentoffset(forproposedcontentoffset_).md>) — Retrieves the content offset to use after an animated layout update or change.
- [- targetContentOffsetForProposedContentOffset:withScrollingVelocity:](<targetcontentoffset(forproposedcontentoffset_withscrollingvelocity_).md>) — Retrieves the point at which to stop scrolling.
