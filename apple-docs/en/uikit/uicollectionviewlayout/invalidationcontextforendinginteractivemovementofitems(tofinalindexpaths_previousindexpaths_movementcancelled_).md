---
title: 'invalidationContextForEndingInteractiveMovementOfItems(toFinalIndexPaths:previousIndexPaths:movementCancelled:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewlayout/invalidationcontextforendinginteractivemovementofitems(tofinalindexpaths:previousindexpaths:movementcancelled:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayout/invalidationcontextforendinginteractivemovementofitems(tofinalindexpaths:previousindexpaths:movementcancelled:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayout/invalidationcontextforendinginteractivemovementofitems%28tofinalindexpaths%3Apreviousindexpaths%3Amovementcancelled%3A%29.json'
content_hash: 'sha256:23d3504488d68e62'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayout](../uicollectionviewlayout.md)

# invalidationContextForEndingInteractiveMovementOfItems(toFinalIndexPaths:previousIndexPaths:movementCancelled:)

<sub>Instance Method</sub>

Retrieves a context object that identifies the items that were moved

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func invalidationContextForEndingInteractiveMovementOfItems(toFinalIndexPaths indexPaths: [IndexPath], previousIndexPaths: [IndexPath], movementCancelled: Bool) -> UICollectionViewLayoutInvalidationContext
```

## Parameters

- `indexPaths` — The final locations of the items. For cancelled interactions, these index paths correspond to the original index paths of the items.

- `previousIndexPaths` — The previous locations of the items. This parameter contains the last set of index paths reported by the collection view during the movement sequence.

- `movementCancelled` — A Boolean value indicating whether the interactive movement ended successfully or was cancelled.

## Return Value

An invalidation context that includes information about what changes need to be made to the layout.

## Discussion

The layout object uses this method to retrieve invalidation contexts when an interactive move of one or more items ends, either because the move was successful or because it was cancelled by the user. The default implementation creates an instance of the class provided by the [invalidationContextClass](invalidationcontextclass.md) class method, fills it with the provided information, and returns it. If you want to use a custom invalidation context object with your layout, always override that method and return your custom class.

Subclasses can override this method and use it to perform additional configuration of the invalidation context before returning it. In your custom implementation, call `super` so that the parent class can perform the basic configuration of the object.

## See Also

### Invalidating the layout

- [- invalidateLayout](<invalidatelayout().md>) — Invalidates the current layout and triggers a layout update.
- [- invalidateLayoutWithContext:](<invalidatelayout(with_).md>) — Invalidates the current layout using the information in the provided context object.
- [invalidationContextClass](invalidationcontextclass.md) — Returns the class to use when creating an invalidation context for the layout.
- [- shouldInvalidateLayoutForBoundsChange:](<shouldinvalidatelayout(forboundschange_).md>) — Asks the layout object if the new bounds require a layout update.
- [- invalidationContextForBoundsChange:](<invalidationcontext(forboundschange_).md>) — Retrieves a context object that defines the portions of the layout that should change when a bounds change occurs.
- [- shouldInvalidateLayoutForPreferredLayoutAttributes:withOriginalAttributes:](<shouldinvalidatelayout(forpreferredlayoutattributes_withoriginalattributes_).md>) — Asks the layout object if changes to a self-sizing cell require a layout update.
- [- invalidationContextForPreferredLayoutAttributes:withOriginalAttributes:](<invalidationcontext(forpreferredlayoutattributes_withoriginalattributes_).md>) — Retrieves a context object that identifies the portions of the layout that should change in response to dynamic cell changes.
- [- invalidationContextForInteractivelyMovingItems:withTargetPosition:previousIndexPaths:previousPosition:](<invalidationcontext(forinteractivelymovingitems_withtargetposition_previousindexpaths_previousposition_).md>) — Retrieves a context object that identifies the items that are being interactively moved in the layout.
