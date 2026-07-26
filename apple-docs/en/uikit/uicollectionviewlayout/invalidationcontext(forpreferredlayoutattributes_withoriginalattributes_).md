---
title: 'invalidationContext(forPreferredLayoutAttributes:withOriginalAttributes:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewlayout/invalidationcontext(forpreferredlayoutattributes:withoriginalattributes:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayout/invalidationcontext(forpreferredlayoutattributes:withoriginalattributes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayout/invalidationcontext%28forpreferredlayoutattributes%3Awithoriginalattributes%3A%29.json'
content_hash: 'sha256:f0adc494ade46054'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayout](../uicollectionviewlayout.md)

# invalidationContext(forPreferredLayoutAttributes:withOriginalAttributes:)

<sub>Instance Method</sub>

Retrieves a context object that identifies the portions of the layout that should change in response to dynamic cell changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func invalidationContext(forPreferredLayoutAttributes preferredAttributes: UICollectionViewLayoutAttributes, withOriginalAttributes originalAttributes: UICollectionViewLayoutAttributes) -> UICollectionViewLayoutInvalidationContext
```

## Parameters

- `preferredAttributes` — The layout attributes returned by the cell’s [- preferredLayoutAttributesFittingAttributes:](<../uicollectionreusableview/preferredlayoutattributesfitting(__).md>) method.

- `originalAttributes` — The attributes that the layout object originally suggested for the cell.

## Return Value

An invalidation context that includes information about what changes need to be made to the layout.

## Discussion

The default implementation of this method creates an instance of the class provided by the [invalidationContextClass](invalidationcontextclass.md) class method and returns it. If you want to use a custom invalidation context object with your layout, always override that method and return your custom class.

Subclasses can override this method and use it to perform additional configuration of the invalidation context before returning it. In your custom implementation, call `super` so that the parent class can perform the basic configuration of the object.

## See Also

### Invalidating the layout

- [- invalidateLayout](<invalidatelayout().md>) — Invalidates the current layout and triggers a layout update.
- [- invalidateLayoutWithContext:](<invalidatelayout(with_).md>) — Invalidates the current layout using the information in the provided context object.
- [invalidationContextClass](invalidationcontextclass.md) — Returns the class to use when creating an invalidation context for the layout.
- [- shouldInvalidateLayoutForBoundsChange:](<shouldinvalidatelayout(forboundschange_).md>) — Asks the layout object if the new bounds require a layout update.
- [- invalidationContextForBoundsChange:](<invalidationcontext(forboundschange_).md>) — Retrieves a context object that defines the portions of the layout that should change when a bounds change occurs.
- [- shouldInvalidateLayoutForPreferredLayoutAttributes:withOriginalAttributes:](<shouldinvalidatelayout(forpreferredlayoutattributes_withoriginalattributes_).md>) — Asks the layout object if changes to a self-sizing cell require a layout update.
- [- invalidationContextForInteractivelyMovingItems:withTargetPosition:previousIndexPaths:previousPosition:](<invalidationcontext(forinteractivelymovingitems_withtargetposition_previousindexpaths_previousposition_).md>) — Retrieves a context object that identifies the items that are being interactively moved in the layout.
- [- invalidationContextForEndingInteractiveMovementOfItemsToFinalIndexPaths:previousIndexPaths:movementCancelled:](<invalidationcontextforendinginteractivemovementofitems(tofinalindexpaths_previousindexpaths_movementcancelled_).md>) — Retrieves a context object that identifies the items that were moved
