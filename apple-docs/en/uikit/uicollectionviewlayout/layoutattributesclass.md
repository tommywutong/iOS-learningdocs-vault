---
title: layoutAttributesClass
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewlayout/layoutattributesclass
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayout/layoutattributesclass'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayout/layoutattributesclass.json'
content_hash: 'sha256:0185fee7a19bd7be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayout](../uicollectionviewlayout.md)

# layoutAttributesClass

<sub>Type Property</sub>

The class to use when creating layout attributes objects.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class var layoutAttributesClass: AnyClass { get }
```

## Return Value

The class to use for layout attributes objects.

## Discussion

If you subclass [UICollectionViewLayoutAttributes](../uicollectionviewlayoutattributes.md) in order to manage additional layout attributes, you should override this method and return your custom subclass. The methods for creating layout attributes use this class when creating new layout attributes objects.

This method is intended for subclassers only and does not need to be called by your code.

## See Also

### Providing layout attributes

- [- prepareLayout](<prepare().md>) — Tells the layout object to update the current layout.
- [- layoutAttributesForElementsInRect:](<layoutattributesforelements(in_).md>) — Retrieves the layout attributes for all of the cells and views in the specified rectangle.
- [- layoutAttributesForItemAtIndexPath:](<layoutattributesforitem(at_).md>) — Retrieves layout information for an item at the specified index path with a corresponding cell.
- [- layoutAttributesForInteractivelyMovingItemAtIndexPath:withTargetPosition:](<layoutattributesforinteractivelymovingitem(at_withtargetposition_).md>) — Retrieves the layout attributes of an item when it is being moved interactively by the user.
- [- layoutAttributesForSupplementaryViewOfKind:atIndexPath:](<layoutattributesforsupplementaryview(ofkind_at_).md>) — Retrieves the layout attributes for the specified supplementary view.
- [- layoutAttributesForDecorationViewOfKind:atIndexPath:](<layoutattributesfordecorationview(ofkind_at_).md>) — Retrieves the layout attributes for the specified decoration view.
- [- targetContentOffsetForProposedContentOffset:](<targetcontentoffset(forproposedcontentoffset_).md>) — Retrieves the content offset to use after an animated layout update or change.
- [- targetContentOffsetForProposedContentOffset:withScrollingVelocity:](<targetcontentoffset(forproposedcontentoffset_withscrollingvelocity_).md>) — Retrieves the point at which to stop scrolling.
