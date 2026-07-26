---
title: 'collectionView(_:contextMenuConfigurationForItemAt:point:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（16.0 起废弃）, iPadOS 13.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uicollectionviewdelegate/collectionview(_:contextmenuconfigurationforitemat:point:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:contextmenuconfigurationforitemat:point:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdelegate/collectionview%28_%3Acontextmenuconfigurationforitemat%3Apoint%3A%29.json'
content_hash: 'sha256:ae6fabc4898874a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDelegate](../uicollectionviewdelegate.md)

# collectionView(_:contextMenuConfigurationForItemAt:point:)

<sub>Instance Method</sub>

Returns a context menu configuration for the item at a point.

> [!warning] Deprecated
> Use [- collectionView:contextMenuConfigurationForItemsAtIndexPaths:point:](<collectionview(__contextmenuconfigurationforitemsat_point_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, contextMenuConfigurationForItemAt indexPath: IndexPath, point: CGPoint) -> UIContextMenuConfiguration?
```

## Parameters

- `collectionView` — The collection view containing the item.

- `indexPath` — The index path of the item for which a configuration is being requested.

- `point` — The location of the interaction in the collection view’s coordinate space.

## Return Value

A contextual menu configuration object describing the menu to be presented. Returning `nil` prevents the interaction from beginning. Returning an empty configuration object causes the interaction to begin, and then end with a cancellation effect.

## Discussion

You can use the cancellation effect from returning an empty configuration to indicate to users that it’s possible for a menu to be presented from this item, but that there are no actions to present at this particular time.

## See Also

### Deprecated

- [- collectionView:targetIndexPathForMoveFromItemAtIndexPath:toProposedIndexPath:](<collectionview(__targetindexpathformovefromitemat_toproposedindexpath_).md>) — Asks the delegate for the index path to use when moving an item. _(deprecated)_
- [- collectionView:previewForDismissingContextMenuWithConfiguration:](<collectionview(__previewfordismissingcontextmenuwithconfiguration_).md>) — Returns the destination view when dismissing a context menu. _(deprecated)_
- [- collectionView:previewForHighlightingContextMenuWithConfiguration:](<collectionview(__previewforhighlightingcontextmenuwithconfiguration_).md>) — Returns a view to override the default preview the collection view created. _(deprecated)_
- [- collectionView:shouldShowMenuForItemAtIndexPath:](<collectionview(__shouldshowmenuforitemat_).md>) — Asks the delegate if an action menu should be displayed for the specified item. _(deprecated)_
- [- collectionView:canPerformAction:forItemAtIndexPath:withSender:](<collectionview(__canperformaction_foritemat_withsender_).md>) — Asks the delegate if it can perform the specified action on an item in the collection view. _(deprecated)_
- [- collectionView:performAction:forItemAtIndexPath:withSender:](<collectionview(__performaction_foritemat_withsender_).md>) — Tells the delegate to perform the specified action on an item in the collection view. _(deprecated)_
