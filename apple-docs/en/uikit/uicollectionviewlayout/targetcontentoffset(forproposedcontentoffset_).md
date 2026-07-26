---
title: 'targetContentOffset(forProposedContentOffset:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewlayout/targetcontentoffset(forproposedcontentoffset:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayout/targetcontentoffset(forproposedcontentoffset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayout/targetcontentoffset%28forproposedcontentoffset%3A%29.json'
content_hash: 'sha256:51978e0a999dab84'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayout](../uicollectionviewlayout.md)

# targetContentOffset(forProposedContentOffset:)

<sub>Instance Method</sub>

Retrieves the content offset to use after an animated layout update or change.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func targetContentOffset(forProposedContentOffset proposedContentOffset: CGPoint) -> CGPoint
```

## Parameters

- `proposedContentOffset` — The proposed point (in the coordinate space of the collection view’s content view) for the upper-left corner of the visible content. This represents the point that the collection view has calculated as the most likely value to use at the end of the animation.

## Return Value

The content offset that you want to use instead. The default implementation of this method returns the value in the `proposedContentOffset` parameter.

## Discussion

During layout updates, or when transitioning between layouts, the collection view calls this method to give you the opportunity to change the proposed content offset to use at the end of the animation. You might override this method if the animations or transition might cause items to be positioned in a way that is not optimal for your design.

The collection view calls this method after calling the [- prepareLayout](<prepare().md>) and [collectionViewContentSize](collectionviewcontentsize.md) methods.

## See Also

### Providing layout attributes

- [layoutAttributesClass](layoutattributesclass.md) — The class to use when creating layout attributes objects.
- [- prepareLayout](<prepare().md>) — Tells the layout object to update the current layout.
- [- layoutAttributesForElementsInRect:](<layoutattributesforelements(in_).md>) — Retrieves the layout attributes for all of the cells and views in the specified rectangle.
- [- layoutAttributesForItemAtIndexPath:](<layoutattributesforitem(at_).md>) — Retrieves layout information for an item at the specified index path with a corresponding cell.
- [- layoutAttributesForInteractivelyMovingItemAtIndexPath:withTargetPosition:](<layoutattributesforinteractivelymovingitem(at_withtargetposition_).md>) — Retrieves the layout attributes of an item when it is being moved interactively by the user.
- [- layoutAttributesForSupplementaryViewOfKind:atIndexPath:](<layoutattributesforsupplementaryview(ofkind_at_).md>) — Retrieves the layout attributes for the specified supplementary view.
- [- layoutAttributesForDecorationViewOfKind:atIndexPath:](<layoutattributesfordecorationview(ofkind_at_).md>) — Retrieves the layout attributes for the specified decoration view.
- [- targetContentOffsetForProposedContentOffset:withScrollingVelocity:](<targetcontentoffset(forproposedcontentoffset_withscrollingvelocity_).md>) — Retrieves the point at which to stop scrolling.
