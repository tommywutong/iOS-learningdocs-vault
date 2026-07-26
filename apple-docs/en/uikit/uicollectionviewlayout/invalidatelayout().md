---
title: invalidateLayout()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewlayout/invalidatelayout()
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayout/invalidatelayout()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayout/invalidatelayout%28%29.json'
content_hash: 'sha256:2cedb1f01e51f5f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayout](../uicollectionviewlayout.md)

# invalidateLayout()

<sub>Instance Method</sub>

Invalidates the current layout and triggers a layout update.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func invalidateLayout()
```

## Discussion

You can call this method at any time to update the layout information. This method invalidates the layout of the collection view itself and returns right away. Thus, you can call this method multiple times from the same block of code without triggering multiple layout updates. The actual layout update occurs during the next view layout update cycle.

If you override this method, you must call `super` at some point in your implementation.

## See Also

### Invalidating the layout

- [- invalidateLayoutWithContext:](<invalidatelayout(with_).md>) — Invalidates the current layout using the information in the provided context object.
- [invalidationContextClass](invalidationcontextclass.md) — Returns the class to use when creating an invalidation context for the layout.
- [- shouldInvalidateLayoutForBoundsChange:](<shouldinvalidatelayout(forboundschange_).md>) — Asks the layout object if the new bounds require a layout update.
- [- invalidationContextForBoundsChange:](<invalidationcontext(forboundschange_).md>) — Retrieves a context object that defines the portions of the layout that should change when a bounds change occurs.
- [- shouldInvalidateLayoutForPreferredLayoutAttributes:withOriginalAttributes:](<shouldinvalidatelayout(forpreferredlayoutattributes_withoriginalattributes_).md>) — Asks the layout object if changes to a self-sizing cell require a layout update.
- [- invalidationContextForPreferredLayoutAttributes:withOriginalAttributes:](<invalidationcontext(forpreferredlayoutattributes_withoriginalattributes_).md>) — Retrieves a context object that identifies the portions of the layout that should change in response to dynamic cell changes.
- [- invalidationContextForInteractivelyMovingItems:withTargetPosition:previousIndexPaths:previousPosition:](<invalidationcontext(forinteractivelymovingitems_withtargetposition_previousindexpaths_previousposition_).md>) — Retrieves a context object that identifies the items that are being interactively moved in the layout.
- [- invalidationContextForEndingInteractiveMovementOfItemsToFinalIndexPaths:previousIndexPaths:movementCancelled:](<invalidationcontextforendinginteractivemovementofitems(tofinalindexpaths_previousindexpaths_movementcancelled_).md>) — Retrieves a context object that identifies the items that were moved
