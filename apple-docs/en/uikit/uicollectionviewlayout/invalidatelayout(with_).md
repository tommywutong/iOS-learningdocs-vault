---
title: 'invalidateLayout(with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewlayout/invalidatelayout(with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayout/invalidatelayout(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayout/invalidatelayout%28with%3A%29.json'
content_hash: 'sha256:8e32b6090c8fc5d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayout](../uicollectionviewlayout.md)

# invalidateLayout(with:)

<sub>Instance Method</sub>

Invalidates the current layout using the information in the provided context object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func invalidateLayout(with context: UICollectionViewLayoutInvalidationContext)
```

## Parameters

- `context` — The context object indicating which parts of the layout to refresh.

## Discussion

The default implementation of this method optimizes the layout process using the base properties of the [UICollectionViewLayoutInvalidationContext](../uicollectionviewlayoutinvalidationcontext.md) class. If you define a custom context object for your layout, override this method and apply any custom properties of the context object to your layout computations.

If you override this method, you must call `super` at some point in your implementation.

## See Also

### Invalidating the layout

- [- invalidateLayout](<invalidatelayout().md>) — Invalidates the current layout and triggers a layout update.
- [invalidationContextClass](invalidationcontextclass.md) — Returns the class to use when creating an invalidation context for the layout.
- [- shouldInvalidateLayoutForBoundsChange:](<shouldinvalidatelayout(forboundschange_).md>) — Asks the layout object if the new bounds require a layout update.
- [- invalidationContextForBoundsChange:](<invalidationcontext(forboundschange_).md>) — Retrieves a context object that defines the portions of the layout that should change when a bounds change occurs.
- [- shouldInvalidateLayoutForPreferredLayoutAttributes:withOriginalAttributes:](<shouldinvalidatelayout(forpreferredlayoutattributes_withoriginalattributes_).md>) — Asks the layout object if changes to a self-sizing cell require a layout update.
- [- invalidationContextForPreferredLayoutAttributes:withOriginalAttributes:](<invalidationcontext(forpreferredlayoutattributes_withoriginalattributes_).md>) — Retrieves a context object that identifies the portions of the layout that should change in response to dynamic cell changes.
- [- invalidationContextForInteractivelyMovingItems:withTargetPosition:previousIndexPaths:previousPosition:](<invalidationcontext(forinteractivelymovingitems_withtargetposition_previousindexpaths_previousposition_).md>) — Retrieves a context object that identifies the items that are being interactively moved in the layout.
- [- invalidationContextForEndingInteractiveMovementOfItemsToFinalIndexPaths:previousIndexPaths:movementCancelled:](<invalidationcontextforendinginteractivemovementofitems(tofinalindexpaths_previousindexpaths_movementcancelled_).md>) — Retrieves a context object that identifies the items that were moved
