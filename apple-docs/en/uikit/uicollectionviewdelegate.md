---
title: UICollectionViewDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdelegate.json'
content_hash: 'sha256:de2f5dfd4c7caa16'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICollectionViewDelegate

<sub>Protocol</sub>

The methods adopted by the object you use to manage user interactions with items in a collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UICollectionViewDelegate : UIScrollViewDelegate
```

## Overview

A collection view delegate manages user interactions with the collection view’s contents, including item selection, highlighting, and performing actions on those items. The methods of this protocol are all optional.

When configuring the collection view object, assign your delegate object to its [delegate](uicollectionview/delegate.md) property. For more information, see [UICollectionView](uicollectionview.md).

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [UIScrollViewDelegate](uiscrollviewdelegate.md)

- **Inherited By**: [UICollectionViewDelegateFlowLayout](uicollectionviewdelegateflowlayout.md)

- **Conforming Types**: [UICollectionViewController](uicollectionviewcontroller.md)

## Topics

### Managing the selected cells

- [Changing the appearance of selected and highlighted cells](changing-the-appearance-of-selected-and-highlighted-cells.md) — Provide visual feedback to the user about the state of a cell and the transition between states.
- [Selecting multiple items with a two-finger pan gesture](selecting-multiple-items-with-a-two-finger-pan-gesture.md) — Accelerate user selection of multiple items using the multiselect gesture on table and collection views.
- [- collectionView:shouldSelectItemAtIndexPath:](<uicollectionviewdelegate/collectionview(__shouldselectitemat_).md>) — Asks the delegate if the specified item should be selected.
- [- collectionView:didSelectItemAtIndexPath:](<uicollectionviewdelegate/collectionview(__didselectitemat_).md>) — Tells the delegate that the item at the specified index path was selected.
- [- collectionView:shouldDeselectItemAtIndexPath:](<uicollectionviewdelegate/collectionview(__shoulddeselectitemat_).md>) — Asks the delegate if the specified item should be deselected.
- [- collectionView:didDeselectItemAtIndexPath:](<uicollectionviewdelegate/collectionview(__diddeselectitemat_).md>) — Tells the delegate that the item at the specified path was deselected.
- [- collectionView:shouldBeginMultipleSelectionInteractionAtIndexPath:](<uicollectionviewdelegate/collectionview(__shouldbeginmultipleselectioninteractionat_).md>) — Asks the delegate whether the user can select multiple items using a two-finger pan gesture in a collection view.
- [- collectionView:didBeginMultipleSelectionInteractionAtIndexPath:](<uicollectionviewdelegate/collectionview(__didbeginmultipleselectioninteractionat_).md>) — Tells the delegate when the user starts using a two-finger pan gesture to select multiple items in a collection view.
- [- collectionViewDidEndMultipleSelectionInteraction:](<uicollectionviewdelegate/collectionviewdidendmultipleselectioninteraction(__).md>) — Tells the delegate when the user stops using a two-finger pan gesture to select multiple items in a collection view.

### Managing cell highlighting

- [- collectionView:shouldHighlightItemAtIndexPath:](<uicollectionviewdelegate/collectionview(__shouldhighlightitemat_).md>) — Asks the delegate if the item should be highlighted during tracking.
- [- collectionView:didHighlightItemAtIndexPath:](<uicollectionviewdelegate/collectionview(__didhighlightitemat_).md>) — Tells the delegate that the item at the specified index path was highlighted.
- [- collectionView:didUnhighlightItemAtIndexPath:](<uicollectionviewdelegate/collectionview(__didunhighlightitemat_).md>) — Tells the delegate that the highlight was removed from the item at the specified index path.

### Tracking the addition and removal of views

- [- collectionView:willDisplayCell:forItemAtIndexPath:](<uicollectionviewdelegate/collectionview(__willdisplay_foritemat_).md>) — Tells the delegate that the specified cell is about to be displayed in the collection view.
- [- collectionView:willDisplaySupplementaryView:forElementKind:atIndexPath:](<uicollectionviewdelegate/collectionview(__willdisplaysupplementaryview_forelementkind_at_).md>) — Tells the delegate that the specified supplementary view is about to be displayed in the collection view.
- [- collectionView:didEndDisplayingCell:forItemAtIndexPath:](<uicollectionviewdelegate/collectionview(__didenddisplaying_foritemat_).md>) — Tells the delegate that the specified cell was removed from the collection view.
- [- collectionView:didEndDisplayingSupplementaryView:forElementOfKind:atIndexPath:](<uicollectionviewdelegate/collectionview(__didenddisplayingsupplementaryview_forelementofkind_at_).md>) — Tells the delegate that the specified supplementary view was removed from the collection view.

### Handling layout changes

- [- collectionView:transitionLayoutForOldLayout:newLayout:](<uicollectionviewdelegate/collectionview(__transitionlayoutforoldlayout_newlayout_).md>) — Asks for the custom transition layout to use when moving between the specified layouts.
- [- collectionView:targetContentOffsetForProposedContentOffset:](<uicollectionviewdelegate/collectionview(__targetcontentoffsetforproposedcontentoffset_).md>) — Gives the delegate an opportunity to customize the content offset for layout changes and animated updates.
- [- collectionView:targetIndexPathForMoveOfItemFromOriginalIndexPath:atCurrentIndexPath:toProposedIndexPath:](<uicollectionviewdelegate/collectionview(__targetindexpathformoveofitemfromoriginalindexpath_atcurrentindexpath_toproposedindexpath_).md>) — Asks the delegate for the index path to use when moving an item.

### Managing context menus

- [Adding context menus in your app](adding-context-menus-in-your-app.md) — Provide quick access to useful actions by adding context menus to your iOS app.
- [- collectionView:willDisplayContextMenuWithConfiguration:animator:](<uicollectionviewdelegate/collectionview(__willdisplaycontextmenu_animator_).md>) — Informs the delegate when a context menu will appear.
- [- collectionView:willEndContextMenuInteractionWithConfiguration:animator:](<uicollectionviewdelegate/collectionview(__willendcontextmenuinteraction_animator_).md>) — Informs the delegate when a context menu will disappear.
- [- collectionView:willPerformPreviewActionForMenuWithConfiguration:animator:](<uicollectionviewdelegate/collectionview(__willperformpreviewactionformenuwith_animator_).md>) — Informs the delegate when a user triggers a commit by tapping the preview.
- [- collectionView:contextMenuConfigurationForItemsAtIndexPaths:point:](<uicollectionviewdelegate/collectionview(__contextmenuconfigurationforitemsat_point_).md>) — Asks the delegate for a context-menu configuration for the items at the specified index paths.
- [- collectionView:contextMenuConfiguration:highlightPreviewForItemAtIndexPath:](<uicollectionviewdelegate/collectionview(__contextmenuconfiguration_highlightpreviewforitemat_).md>) — Asks the delegate for a preview of the item at the specified index path when a context-menu interaction begins.
- [- collectionView:contextMenuConfiguration:dismissalPreviewForItemAtIndexPath:](<uicollectionviewdelegate/collectionview(__contextmenuconfiguration_dismissalpreviewforitemat_).md>) — Asks the delegate for a preview of the item at the specified index path when a context-menu interaction ends.

### Working with focus

- [- collectionView:canFocusItemAtIndexPath:](<uicollectionviewdelegate/collectionview(__canfocusitemat_).md>) — Asks the delegate whether the item at the specified index path can be focused.
- [- indexPathForPreferredFocusedViewInCollectionView:](<uicollectionviewdelegate/indexpathforpreferredfocusedview(in_).md>) — Asks the delegate for the index path of the cell that should be focused.
- [- collectionView:shouldUpdateFocusInContext:](<uicollectionviewdelegate/collectionview(__shouldupdatefocusin_).md>) — Asks the delegate whether a change in focus should occur.
- [- collectionView:didUpdateFocusInContext:withAnimationCoordinator:](<uicollectionviewdelegate/collectionview(__didupdatefocusin_with_).md>) — Tells the delegate that a focus update occurred.
- [- collectionView:selectionFollowsFocusForItemAtIndexPath:](<uicollectionviewdelegate/collectionview(__selectionfollowsfocusforitemat_).md>) — Asks the delegate whether to relate selection and focus behavior for the cell at the corresponding index path.

### Editing items

- [- collectionView:canEditItemAtIndexPath:](<uicollectionviewdelegate/collectionview(__canedititemat_).md>) — Determines whether the specified item is editable.

### Managing actions for cells

- [- collectionView:canPerformPrimaryActionForItemAtIndexPath:](<uicollectionviewdelegate/collectionview(__canperformprimaryactionforitemat_).md>) — Asks the delegate whether to perform a primary action for the cell at the specified index path.
- [- collectionView:performPrimaryActionForItemAtIndexPath:](<uicollectionviewdelegate/collectionview(__performprimaryactionforitemat_).md>) — Tells the delegate to perform the primary action for the cell at the specified index path.

### Handling scene transitions

- [- collectionView:sceneActivationConfigurationForItemAtIndexPath:point:](<uicollectionviewdelegate/collectionview(__sceneactivationconfigurationforitemat_point_).md>) — Returns a scene activation configuration that allows the cell to expand into a new scene.

### Controlling the spring-loading behavior

- [- collectionView:shouldSpringLoadItemAtIndexPath:withContext:](<uicollectionviewdelegate/collectionview(__shouldspringloaditemat_with_).md>) — Determines whether the spring-loading interaction effect is displayed for the specified item.

### Deprecated

- [- collectionView:targetIndexPathForMoveFromItemAtIndexPath:toProposedIndexPath:](<uicollectionviewdelegate/collectionview(__targetindexpathformovefromitemat_toproposedindexpath_).md>) — Asks the delegate for the index path to use when moving an item. _(deprecated)_
- [- collectionView:contextMenuConfigurationForItemAtIndexPath:point:](<uicollectionviewdelegate/collectionview(__contextmenuconfigurationforitemat_point_).md>) — Returns a context menu configuration for the item at a point. _(deprecated)_
- [- collectionView:previewForDismissingContextMenuWithConfiguration:](<uicollectionviewdelegate/collectionview(__previewfordismissingcontextmenuwithconfiguration_).md>) — Returns the destination view when dismissing a context menu. _(deprecated)_
- [- collectionView:previewForHighlightingContextMenuWithConfiguration:](<uicollectionviewdelegate/collectionview(__previewforhighlightingcontextmenuwithconfiguration_).md>) — Returns a view to override the default preview the collection view created. _(deprecated)_
- [- collectionView:shouldShowMenuForItemAtIndexPath:](<uicollectionviewdelegate/collectionview(__shouldshowmenuforitemat_).md>) — Asks the delegate if an action menu should be displayed for the specified item. _(deprecated)_
- [- collectionView:canPerformAction:forItemAtIndexPath:withSender:](<uicollectionviewdelegate/collectionview(__canperformaction_foritemat_withsender_).md>) — Asks the delegate if it can perform the specified action on an item in the collection view. _(deprecated)_
- [- collectionView:performAction:forItemAtIndexPath:withSender:](<uicollectionviewdelegate/collectionview(__performaction_foritemat_withsender_).md>) — Tells the delegate to perform the specified action on an item in the collection view. _(deprecated)_

## See Also

### Managing collection view interactions

- [delegate](uicollectionview/delegate.md) — The object that acts as the delegate of the collection view.
