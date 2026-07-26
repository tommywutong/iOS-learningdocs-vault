---
title: UICollectionViewLayout
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewlayout
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayout.json'
content_hash: 'sha256:581f76e6a919ef6f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICollectionViewLayout

<sub>Class</sub>

An abstract base class for generating layout information for a collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UICollectionViewLayout
```

## Overview

A layout object determines the placement of cells, supplementary views, and decoration views inside the collection view’s bounds and reports that information to the collection view. The collection view then applies the provided layout information to the corresponding views so that they can be presented onscreen.

You must subclass [UICollectionViewLayout](uicollectionviewlayout.md) in order to use it. Before you consider subclassing, however, consider whether you can adapt [UICollectionViewCompositionalLayout](uicollectionviewcompositionallayout.md) to your layout needs.

### Subclassing notes

The layout object defines the position, size, and visual state of items in the collection view, based on the design of the layout. The views for the layout are created by the collection view’s data source.

You lay out three types of visual elements in a collection view:

- _Cells_ are the main elements positioned by the layout. Each cell represents a single data item in the collection. You can make cells interactive so that a user can perform actions like selecting, dragging, and reordering the cells. A collection view can have a single group of cells, or you can divide those cells into multiple sections. The layout object arranges the cells in the collection view’s content area.
- _Supplementary views_ present data but can’t be selected by the user. You use supplementary views to implement things like header and footer views for a given section or for the entire collection view. Supplementary views are optional and their use and placement is defined by the layout object.
- _Decoration views_ are visual adornments, like badges, that can’t be selected and aren’t inherently tied to the data of the collection view. Decoration views are another type of supplementary view. Like supplementary views, they’re optional and their use and placement is defined by the layout object.

The collection view asks its layout object to provide layout information for these elements at many different times. Every cell and view that appears on screen is positioned using information from the layout object. Similarly, every time items are inserted into or deleted from the collection view, an additional layout pass occurs for the items being added or removed. However, the collection view always limits layout to the objects that are visible onscreen.

#### Methods to override

Every layout object should implement the following methods:

- [collectionViewContentSize](uicollectionviewlayout/collectionviewcontentsize.md)
- [- layoutAttributesForElementsInRect:](<uicollectionviewlayout/layoutattributesforelements(in_).md>)
- [- layoutAttributesForItemAtIndexPath:](<uicollectionviewlayout/layoutattributesforitem(at_).md>)
- [- layoutAttributesForSupplementaryViewOfKind:atIndexPath:](<uicollectionviewlayout/layoutattributesforsupplementaryview(ofkind_at_).md>) (if your layout supports supplementary views)
- [- layoutAttributesForDecorationViewOfKind:atIndexPath:](<uicollectionviewlayout/layoutattributesfordecorationview(ofkind_at_).md>) (if your layout supports decoration views)
- [- shouldInvalidateLayoutForBoundsChange:](<uicollectionviewlayout/shouldinvalidatelayout(forboundschange_).md>)

These methods provide the fundamental layout information that the collection view needs to place contents on the screen. If your layout doesn’t support supplementary or decoration views, don’t implement the corresponding methods.

When the data in the collection view changes and items are to be inserted or deleted, the collection view asks its layout object to update the layout information. Specifically, any item that’s moved, added, or deleted must have its layout information updated to reflect its new location. For moved items, the collection view uses the standard methods to retrieve the item’s updated layout attributes. For items being inserted or deleted, the collection view calls some different methods, which you should override to provide the appropriate layout information:

- [- initialLayoutAttributesForAppearingItemAtIndexPath:](<uicollectionviewlayout/initiallayoutattributesforappearingitem(at_).md>)
- [- initialLayoutAttributesForAppearingSupplementaryElementOfKind:atIndexPath:](<uicollectionviewlayout/initiallayoutattributesforappearingsupplementaryelement(ofkind_at_).md>)
- [- initialLayoutAttributesForAppearingDecorationElementOfKind:atIndexPath:](<uicollectionviewlayout/initiallayoutattributesforappearingdecorationelement(ofkind_at_).md>)
- [- finalLayoutAttributesForDisappearingItemAtIndexPath:](<uicollectionviewlayout/finallayoutattributesfordisappearingitem(at_).md>)
- [- finalLayoutAttributesForDisappearingSupplementaryElementOfKind:atIndexPath:](<uicollectionviewlayout/finallayoutattributesfordisappearingsupplementaryelement(ofkind_at_).md>)
- [- finalLayoutAttributesForDisappearingDecorationElementOfKind:atIndexPath:](<uicollectionviewlayout/finallayoutattributesfordisappearingdecorationelement(ofkind_at_).md>)

In addition to these methods, you can also override the [- prepareForCollectionViewUpdates:](<uicollectionviewlayout/prepare(forcollectionviewupdates_).md>) to handle any layout-related preparation. You can also override the [- finalizeCollectionViewUpdates](<uicollectionviewlayout/finalizecollectionviewupdates().md>) method and use it to add animations to the overall animation block or to implement any final layout-related tasks.

#### Optimizing layout performance using invalidation contexts

When designing your custom layouts, you can improve performance by invalidating only those parts of your layout that actually changed. When you change items, calling the [- invalidateLayout](<uicollectionviewlayout/invalidatelayout().md>) method forces the collection view to recompute all of its layout information and reapply it. A better solution is to recompute only the layout information that changed, which is exactly what invalidation contexts allow you to do. An invalidation context lets you specify which parts of the layout changed. The layout object can then use that information to minimize the amount of data it recomputes.

To define a custom invalidation context for your layout, subclass the [UICollectionViewLayoutInvalidationContext](uicollectionviewlayoutinvalidationcontext.md) class. In your subclass, define custom properties that represent the parts of your layout data that can be recomputed independently. When you need to invalidate your layout at runtime, create an instance of your invalidation context subclass, configure the custom properties based on what layout information changed, and pass that object to your layout’s [- invalidateLayoutWithContext:](<uicollectionviewlayout/invalidatelayout(with_).md>) method. Your custom implementation of that method can use the information in the invalidation context to recompute only the portions of your layout that changed.

If you define a custom invalidation context class for your layout object, you should also override the [invalidationContextClass](uicollectionviewlayout/invalidationcontextclass.md) method and return your custom class. The collection view always creates an instance of the class you specify when it needs an invalidation context. Returning your custom subclass from this method ensures that your layout object always has the invalidation context it expects.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [UICollectionViewCompositionalLayout](uicollectionviewcompositionallayout.md), [UICollectionViewFlowLayout](uicollectionviewflowlayout.md), [UICollectionViewTransitionLayout](uicollectionviewtransitionlayout.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Creating the collection view layout

- [- init](<uicollectionviewlayout/init().md>) — Creates a collection view layout object.
- [- initWithCoder:](<uicollectionviewlayout/init(coder_).md>) — Creates a collection view layout object from data in a given unarchiver.

### Getting the collection view information

- [collectionView](uicollectionviewlayout/collectionview.md) — The collection view object currently using this layout object.
- [collectionViewContentSize](uicollectionviewlayout/collectionviewcontentsize.md) — The width and height of the collection view’s contents.

### Providing layout attributes

- [layoutAttributesClass](uicollectionviewlayout/layoutattributesclass.md) — The class to use when creating layout attributes objects.
- [- prepareLayout](<uicollectionviewlayout/prepare().md>) — Tells the layout object to update the current layout.
- [- layoutAttributesForElementsInRect:](<uicollectionviewlayout/layoutattributesforelements(in_).md>) — Retrieves the layout attributes for all of the cells and views in the specified rectangle.
- [- layoutAttributesForItemAtIndexPath:](<uicollectionviewlayout/layoutattributesforitem(at_).md>) — Retrieves layout information for an item at the specified index path with a corresponding cell.
- [- layoutAttributesForInteractivelyMovingItemAtIndexPath:withTargetPosition:](<uicollectionviewlayout/layoutattributesforinteractivelymovingitem(at_withtargetposition_).md>) — Retrieves the layout attributes of an item when it is being moved interactively by the user.
- [- layoutAttributesForSupplementaryViewOfKind:atIndexPath:](<uicollectionviewlayout/layoutattributesforsupplementaryview(ofkind_at_).md>) — Retrieves the layout attributes for the specified supplementary view.
- [- layoutAttributesForDecorationViewOfKind:atIndexPath:](<uicollectionviewlayout/layoutattributesfordecorationview(ofkind_at_).md>) — Retrieves the layout attributes for the specified decoration view.
- [- targetContentOffsetForProposedContentOffset:](<uicollectionviewlayout/targetcontentoffset(forproposedcontentoffset_).md>) — Retrieves the content offset to use after an animated layout update or change.
- [- targetContentOffsetForProposedContentOffset:withScrollingVelocity:](<uicollectionviewlayout/targetcontentoffset(forproposedcontentoffset_withscrollingvelocity_).md>) — Retrieves the point at which to stop scrolling.

### Responding to collection view updates

- [- prepareForCollectionViewUpdates:](<uicollectionviewlayout/prepare(forcollectionviewupdates_).md>) — Notifies the layout object that the contents of the collection view are about to change.
- [- finalizeCollectionViewUpdates](<uicollectionviewlayout/finalizecollectionviewupdates().md>) — Performs any additional animations or clean up needed during a collection view update.
- [- indexPathsToInsertForSupplementaryViewOfKind:](<uicollectionviewlayout/indexpathstoinsertforsupplementaryview(ofkind_).md>) — Retrieves an array of index paths for the supplementary views you want to add to the layout.
- [- indexPathsToInsertForDecorationViewOfKind:](<uicollectionviewlayout/indexpathstoinsertfordecorationview(ofkind_).md>) — Retrieves an array of index paths representing the decoration views to add.
- [- initialLayoutAttributesForAppearingItemAtIndexPath:](<uicollectionviewlayout/initiallayoutattributesforappearingitem(at_).md>) — Retrieves the starting layout information for an item being inserted into the collection view.
- [- initialLayoutAttributesForAppearingSupplementaryElementOfKind:atIndexPath:](<uicollectionviewlayout/initiallayoutattributesforappearingsupplementaryelement(ofkind_at_).md>) — Retrieves the starting layout information for a supplementary view being inserted into the collection view.
- [- initialLayoutAttributesForAppearingDecorationElementOfKind:atIndexPath:](<uicollectionviewlayout/initiallayoutattributesforappearingdecorationelement(ofkind_at_).md>) — Retrieves the starting layout information for a decoration view being inserted into the collection view.
- [- indexPathsToDeleteForSupplementaryViewOfKind:](<uicollectionviewlayout/indexpathstodeleteforsupplementaryview(ofkind_).md>) — Retrieves an array of index paths representing the supplementary views to remove.
- [- indexPathsToDeleteForDecorationViewOfKind:](<uicollectionviewlayout/indexpathstodeletefordecorationview(ofkind_).md>) — Retrieves an array of index paths representing the decoration views to remove.
- [- finalLayoutAttributesForDisappearingItemAtIndexPath:](<uicollectionviewlayout/finallayoutattributesfordisappearingitem(at_).md>) — Retrieves the final layout information for an item that is about to be removed from the collection view.
- [- finalLayoutAttributesForDisappearingSupplementaryElementOfKind:atIndexPath:](<uicollectionviewlayout/finallayoutattributesfordisappearingsupplementaryelement(ofkind_at_).md>) — Retrieves the final layout information for a supplementary view that is about to be removed from the collection view.
- [- finalLayoutAttributesForDisappearingDecorationElementOfKind:atIndexPath:](<uicollectionviewlayout/finallayoutattributesfordisappearingdecorationelement(ofkind_at_).md>) — Retrieves the final layout information for a decoration view that is about to be removed from the collection view.
- [- targetIndexPathForInteractivelyMovingItem:withPosition:](<uicollectionviewlayout/targetindexpath(forinteractivelymovingitem_withposition_).md>) — Retrieves the index path to for an item when it is at the specified location in the collection view’s bounds.

### Invalidating the layout

- [- invalidateLayout](<uicollectionviewlayout/invalidatelayout().md>) — Invalidates the current layout and triggers a layout update.
- [- invalidateLayoutWithContext:](<uicollectionviewlayout/invalidatelayout(with_).md>) — Invalidates the current layout using the information in the provided context object.
- [invalidationContextClass](uicollectionviewlayout/invalidationcontextclass.md) — Returns the class to use when creating an invalidation context for the layout.
- [- shouldInvalidateLayoutForBoundsChange:](<uicollectionviewlayout/shouldinvalidatelayout(forboundschange_).md>) — Asks the layout object if the new bounds require a layout update.
- [- invalidationContextForBoundsChange:](<uicollectionviewlayout/invalidationcontext(forboundschange_).md>) — Retrieves a context object that defines the portions of the layout that should change when a bounds change occurs.
- [- shouldInvalidateLayoutForPreferredLayoutAttributes:withOriginalAttributes:](<uicollectionviewlayout/shouldinvalidatelayout(forpreferredlayoutattributes_withoriginalattributes_).md>) — Asks the layout object if changes to a self-sizing cell require a layout update.
- [- invalidationContextForPreferredLayoutAttributes:withOriginalAttributes:](<uicollectionviewlayout/invalidationcontext(forpreferredlayoutattributes_withoriginalattributes_).md>) — Retrieves a context object that identifies the portions of the layout that should change in response to dynamic cell changes.
- [- invalidationContextForInteractivelyMovingItems:withTargetPosition:previousIndexPaths:previousPosition:](<uicollectionviewlayout/invalidationcontext(forinteractivelymovingitems_withtargetposition_previousindexpaths_previousposition_).md>) — Retrieves a context object that identifies the items that are being interactively moved in the layout.
- [- invalidationContextForEndingInteractiveMovementOfItemsToFinalIndexPaths:previousIndexPaths:movementCancelled:](<uicollectionviewlayout/invalidationcontextforendinginteractivemovementofitems(tofinalindexpaths_previousindexpaths_movementcancelled_).md>) — Retrieves a context object that identifies the items that were moved

### Coordinating animated changes

- [- prepareForAnimatedBoundsChange:](<uicollectionviewlayout/prepare(foranimatedboundschange_).md>) — Prepares the layout object for animated changes to the view’s bounds or the insertion or deletion of items.
- [- finalizeAnimatedBoundsChange](<uicollectionviewlayout/finalizeanimatedboundschange().md>) — Cleans up after any animated changes to the view’s bounds or after the insertion or deletion of items.

### Transitioning between layouts

- [- prepareForTransitionFromLayout:](<uicollectionviewlayout/preparefortransition(from_).md>) — Tells the layout object to prepare to be installed as the layout for the collection view.
- [- prepareForTransitionToLayout:](<uicollectionviewlayout/preparefortransition(to_).md>) — Tells the layout object that it is about to be removed as the layout for the collection view.
- [- finalizeLayoutTransition](<uicollectionviewlayout/finalizelayouttransition().md>) — Tells the layout object to perform any final steps before the transition animations occur.

### Registering decoration views

- [- registerClass:forDecorationViewOfKind:](<uicollectionviewlayout/register(__fordecorationviewofkind_)-361k6.md>) — Registers a class for use in creating decoration views for a collection view.
- [- registerNib:forDecorationViewOfKind:](<uicollectionviewlayout/register(__fordecorationviewofkind_)-35jf9.md>) — Registers a nib file for use in creating decoration views for a collection view.

### Supporting right-to-left layouts

- [developmentLayoutDirection](uicollectionviewlayout/developmentlayoutdirection.md) — The direction of the language you used when designing your custom layout.
- [flipsHorizontallyInOppositeLayoutDirection](uicollectionviewlayout/flipshorizontallyinoppositelayoutdirection.md) — A Boolean value that indicates whether the horizontal coordinate system is automatically flipped at appropriate times.

## See Also

### Manual layouts

- [Customizing collection view layouts](customizing-collection-view-layouts.md) — Customize a view layout by changing the size of cells in the flow or implementing a mosaic style.
- [UICollectionViewFlowLayout](uicollectionviewflowlayout.md) — A layout object that organizes items into a grid with optional header and footer views for each section.
- [UICollectionViewTransitionLayout](uicollectionviewtransitionlayout.md) — A special type of layout object that lets you implement behaviors when changing from one layout to another in your collection view.
- [UICollectionViewLayoutAttributes](uicollectionviewlayoutattributes.md) — A layout object that manages the layout-related attributes for a given item in a collection view.
- [UICollectionViewFlowLayoutInvalidationContext](uicollectionviewflowlayoutinvalidationcontext.md) — A set of properties for determining whether to recompute the size of items or their position in the layout.
