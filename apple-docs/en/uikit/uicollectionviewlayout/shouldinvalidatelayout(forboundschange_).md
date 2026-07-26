---
title: 'shouldInvalidateLayout(forBoundsChange:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewlayout/shouldinvalidatelayout(forboundschange:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayout/shouldinvalidatelayout(forboundschange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayout/shouldinvalidatelayout%28forboundschange%3A%29.json'
content_hash: 'sha256:ae907fa0b55968e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayout](../uicollectionviewlayout.md)

# shouldInvalidateLayout(forBoundsChange:)

<sub>Instance Method</sub>

Asks the layout object if the new bounds require a layout update.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func shouldInvalidateLayout(forBoundsChange newBounds: CGRect) -> Bool
```

## Parameters

- `newBounds` — The new bounds of the collection view.

## Return Value

[true](../../swift/true.md) if the collection view requires a layout update or [false](../../swift/false.md) if the layout does not need to change.

## Discussion

The default implementation of this method returns [false](../../swift/false.md). Subclasses can override it and return an appropriate value based on whether changes in the bounds of the collection view require changes to the layout of cells and supplementary views.

If the bounds of the collection view change and this method returns [true](../../swift/true.md), the collection view invalidates the layout by calling the [- invalidateLayoutWithContext:](<invalidatelayout(with_).md>) method.

## See Also

### Invalidating the layout

- [- invalidateLayout](<invalidatelayout().md>) — Invalidates the current layout and triggers a layout update.
- [- invalidateLayoutWithContext:](<invalidatelayout(with_).md>) — Invalidates the current layout using the information in the provided context object.
- [invalidationContextClass](invalidationcontextclass.md) — Returns the class to use when creating an invalidation context for the layout.
- [- invalidationContextForBoundsChange:](<invalidationcontext(forboundschange_).md>) — Retrieves a context object that defines the portions of the layout that should change when a bounds change occurs.
- [- shouldInvalidateLayoutForPreferredLayoutAttributes:withOriginalAttributes:](<shouldinvalidatelayout(forpreferredlayoutattributes_withoriginalattributes_).md>) — Asks the layout object if changes to a self-sizing cell require a layout update.
- [- invalidationContextForPreferredLayoutAttributes:withOriginalAttributes:](<invalidationcontext(forpreferredlayoutattributes_withoriginalattributes_).md>) — Retrieves a context object that identifies the portions of the layout that should change in response to dynamic cell changes.
- [- invalidationContextForInteractivelyMovingItems:withTargetPosition:previousIndexPaths:previousPosition:](<invalidationcontext(forinteractivelymovingitems_withtargetposition_previousindexpaths_previousposition_).md>) — Retrieves a context object that identifies the items that are being interactively moved in the layout.
- [- invalidationContextForEndingInteractiveMovementOfItemsToFinalIndexPaths:previousIndexPaths:movementCancelled:](<invalidationcontextforendinginteractivemovementofitems(tofinalindexpaths_previousindexpaths_movementcancelled_).md>) — Retrieves a context object that identifies the items that were moved
