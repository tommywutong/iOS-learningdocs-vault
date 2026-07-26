---
title: 'shouldInvalidateLayout(forPreferredLayoutAttributes:withOriginalAttributes:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewlayout/shouldinvalidatelayout(forpreferredlayoutattributes:withoriginalattributes:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayout/shouldinvalidatelayout(forpreferredlayoutattributes:withoriginalattributes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayout/shouldinvalidatelayout%28forpreferredlayoutattributes%3Awithoriginalattributes%3A%29.json'
content_hash: 'sha256:0e354df5374883a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayout](../uicollectionviewlayout.md)

# shouldInvalidateLayout(forPreferredLayoutAttributes:withOriginalAttributes:)

<sub>Instance Method</sub>

Asks the layout object if changes to a self-sizing cell require a layout update.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func shouldInvalidateLayout(forPreferredLayoutAttributes preferredAttributes: UICollectionViewLayoutAttributes, withOriginalAttributes originalAttributes: UICollectionViewLayoutAttributes) -> Bool
```

## Parameters

- `preferredAttributes` — The layout attributes returned by the cell’s [- preferredLayoutAttributesFittingAttributes:](<../uicollectionreusableview/preferredlayoutattributesfitting(__).md>) method.

- `originalAttributes` — The attributes that the layout object originally suggested for the cell.

## Return Value

[true](../../swift/true.md) if the layout should be invalidated or [false](../../swift/false.md) if it should not.

## Discussion

When a collection view includes self-sizing cells, the cells are given the opportunity to modify their own layout attributes before those attributes are applied. A self-sizing cell might do this to specify a different cell size than the one the layout object provides. When the cell provides a different set of attributes, the collection view calls this method to determine if the cell’s change requires a larger layout refresh.

If you are implementing a custom layout, you can override this method and use it to determine if your layout should be invalidated based on the specified attributes. The default implementation of this method returns [false](../../swift/false.md).

## See Also

### Invalidating the layout

- [- invalidateLayout](<invalidatelayout().md>) — Invalidates the current layout and triggers a layout update.
- [- invalidateLayoutWithContext:](<invalidatelayout(with_).md>) — Invalidates the current layout using the information in the provided context object.
- [invalidationContextClass](invalidationcontextclass.md) — Returns the class to use when creating an invalidation context for the layout.
- [- shouldInvalidateLayoutForBoundsChange:](<shouldinvalidatelayout(forboundschange_).md>) — Asks the layout object if the new bounds require a layout update.
- [- invalidationContextForBoundsChange:](<invalidationcontext(forboundschange_).md>) — Retrieves a context object that defines the portions of the layout that should change when a bounds change occurs.
- [- invalidationContextForPreferredLayoutAttributes:withOriginalAttributes:](<invalidationcontext(forpreferredlayoutattributes_withoriginalattributes_).md>) — Retrieves a context object that identifies the portions of the layout that should change in response to dynamic cell changes.
- [- invalidationContextForInteractivelyMovingItems:withTargetPosition:previousIndexPaths:previousPosition:](<invalidationcontext(forinteractivelymovingitems_withtargetposition_previousindexpaths_previousposition_).md>) — Retrieves a context object that identifies the items that are being interactively moved in the layout.
- [- invalidationContextForEndingInteractiveMovementOfItemsToFinalIndexPaths:previousIndexPaths:movementCancelled:](<invalidationcontextforendinginteractivemovementofitems(tofinalindexpaths_previousindexpaths_movementcancelled_).md>) — Retrieves a context object that identifies the items that were moved
