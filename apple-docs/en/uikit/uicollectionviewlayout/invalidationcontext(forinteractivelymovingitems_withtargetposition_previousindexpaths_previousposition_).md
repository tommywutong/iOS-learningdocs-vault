---
title: 'invalidationContext(forInteractivelyMovingItems:withTargetPosition:previousIndexPaths:previousPosition:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewlayout/invalidationcontext(forinteractivelymovingitems:withtargetposition:previousindexpaths:previousposition:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayout/invalidationcontext(forinteractivelymovingitems:withtargetposition:previousindexpaths:previousposition:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayout/invalidationcontext%28forinteractivelymovingitems%3Awithtargetposition%3Apreviousindexpaths%3Apreviousposition%3A%29.json'
content_hash: 'sha256:fe7114289a051ed7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayout](../uicollectionviewlayout.md)

# invalidationContext(forInteractivelyMovingItems:withTargetPosition:previousIndexPaths:previousPosition:)

<sub>Instance Method</sub>

Retrieves a context object that identifies the items that are being interactively moved in the layout.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func invalidationContext(forInteractivelyMovingItems targetIndexPaths: [IndexPath], withTargetPosition targetPosition: CGPoint, previousIndexPaths: [IndexPath], previousPosition: CGPoint) -> UICollectionViewLayoutInvalidationContext
```

## Parameters

- `targetIndexPaths` — The current locations of the items being moved.

- `targetPosition` — The point in the collection view’s coordinate system that is the potential drop point for the items.

- `previousIndexPaths` — The previous locations of the items being moved.

- `previousPosition` — The previous point in the collection view’s coordinate system. This is the point that was previously used to determine the drop point for the items.

## Return Value

An invalidation context that includes information about what changes need to be made to the layout.

## Discussion

The layout object uses this method to retrieve invalidation contexts when an interactive move of one or more items is in progress. The default implementation creates an instance of the class provided by the [invalidationContextClass](invalidationcontextclass.md) class method, fills it with the provided information, and returns it. If you want to use a custom invalidation context object with your layout, always override that method and return your custom class.

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
- [- invalidationContextForEndingInteractiveMovementOfItemsToFinalIndexPaths:previousIndexPaths:movementCancelled:](<invalidationcontextforendinginteractivemovementofitems(tofinalindexpaths_previousindexpaths_movementcancelled_).md>) — Retrieves a context object that identifies the items that were moved
