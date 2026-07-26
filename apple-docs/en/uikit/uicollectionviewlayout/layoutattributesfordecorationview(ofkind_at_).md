---
title: 'layoutAttributesForDecorationView(ofKind:at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewlayout/layoutattributesfordecorationview(ofkind:at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayout/layoutattributesfordecorationview(ofkind:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayout/layoutattributesfordecorationview%28ofkind%3Aat%3A%29.json'
content_hash: 'sha256:25fa9611e952e2eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayout](../uicollectionviewlayout.md)

# layoutAttributesForDecorationView(ofKind:at:)

<sub>Instance Method</sub>

Retrieves the layout attributes for the specified decoration view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func layoutAttributesForDecorationView(ofKind elementKind: String, at indexPath: IndexPath) -> UICollectionViewLayoutAttributes?
```

## Parameters

- `elementKind` — A string that identifies the type of the decoration view.

- `indexPath` — The index path of the decoration view.

## Return Value

A layout attributes object containing the information to apply to the decoration view.

## Discussion

If your layout object defines any decoration views, you must override this method and use it to return layout information for those views.

## See Also

### Providing layout attributes

- [layoutAttributesClass](layoutattributesclass.md) — The class to use when creating layout attributes objects.
- [- prepareLayout](<prepare().md>) — Tells the layout object to update the current layout.
- [- layoutAttributesForElementsInRect:](<layoutattributesforelements(in_).md>) — Retrieves the layout attributes for all of the cells and views in the specified rectangle.
- [- layoutAttributesForItemAtIndexPath:](<layoutattributesforitem(at_).md>) — Retrieves layout information for an item at the specified index path with a corresponding cell.
- [- layoutAttributesForInteractivelyMovingItemAtIndexPath:withTargetPosition:](<layoutattributesforinteractivelymovingitem(at_withtargetposition_).md>) — Retrieves the layout attributes of an item when it is being moved interactively by the user.
- [- layoutAttributesForSupplementaryViewOfKind:atIndexPath:](<layoutattributesforsupplementaryview(ofkind_at_).md>) — Retrieves the layout attributes for the specified supplementary view.
- [- targetContentOffsetForProposedContentOffset:](<targetcontentoffset(forproposedcontentoffset_).md>) — Retrieves the content offset to use after an animated layout update or change.
- [- targetContentOffsetForProposedContentOffset:withScrollingVelocity:](<targetcontentoffset(forproposedcontentoffset_withscrollingvelocity_).md>) — Retrieves the point at which to stop scrolling.
