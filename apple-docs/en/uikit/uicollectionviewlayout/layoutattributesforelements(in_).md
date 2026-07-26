---
title: 'layoutAttributesForElements(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewlayout/layoutattributesforelements(in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayout/layoutattributesforelements(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayout/layoutattributesforelements%28in%3A%29.json'
content_hash: 'sha256:cf8582c7f6d2c031'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayout](../uicollectionviewlayout.md)

# layoutAttributesForElements(in:)

<sub>Instance Method</sub>

Retrieves the layout attributes for all of the cells and views in the specified rectangle.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func layoutAttributesForElements(in rect: CGRect) -> [UICollectionViewLayoutAttributes]?
```

## Parameters

- `rect` — The rectangle (specified in the collection view’s coordinate system) containing the target views.

## Return Value

An array of [UICollectionViewLayoutAttributes](../uicollectionviewlayoutattributes.md) objects representing the layout information for the cells and views. The default implementation returns `nil`.

## Discussion

Subclasses must override this method and use it to return layout information for all items whose view intersects the specified rectangle. Your implementation should return attributes for all visual elements, including cells, supplementary views, and decoration views.

When creating the layout attributes, always create an attributes object that represents the correct element type (cell, supplementary, or decoration). The collection view differentiates between attributes for each type and uses that information to make decisions about which views to create and how to manage them.

## See Also

### Providing layout attributes

- [layoutAttributesClass](layoutattributesclass.md) — The class to use when creating layout attributes objects.
- [- prepareLayout](<prepare().md>) — Tells the layout object to update the current layout.
- [- layoutAttributesForItemAtIndexPath:](<layoutattributesforitem(at_).md>) — Retrieves layout information for an item at the specified index path with a corresponding cell.
- [- layoutAttributesForInteractivelyMovingItemAtIndexPath:withTargetPosition:](<layoutattributesforinteractivelymovingitem(at_withtargetposition_).md>) — Retrieves the layout attributes of an item when it is being moved interactively by the user.
- [- layoutAttributesForSupplementaryViewOfKind:atIndexPath:](<layoutattributesforsupplementaryview(ofkind_at_).md>) — Retrieves the layout attributes for the specified supplementary view.
- [- layoutAttributesForDecorationViewOfKind:atIndexPath:](<layoutattributesfordecorationview(ofkind_at_).md>) — Retrieves the layout attributes for the specified decoration view.
- [- targetContentOffsetForProposedContentOffset:](<targetcontentoffset(forproposedcontentoffset_).md>) — Retrieves the content offset to use after an animated layout update or change.
- [- targetContentOffsetForProposedContentOffset:withScrollingVelocity:](<targetcontentoffset(forproposedcontentoffset_withscrollingvelocity_).md>) — Retrieves the point at which to stop scrolling.
