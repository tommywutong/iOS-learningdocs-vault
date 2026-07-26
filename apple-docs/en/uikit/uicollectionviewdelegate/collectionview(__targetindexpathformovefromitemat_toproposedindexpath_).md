---
title: 'collectionView(_:targetIndexPathForMoveFromItemAt:toProposedIndexPath:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+（15.0 起废弃）, iPadOS 9.0+（15.0 起废弃）, Mac Catalyst 13.1+（15.0 起废弃）, tvOS 9.0+（15.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uicollectionviewdelegate/collectionview(_:targetindexpathformovefromitemat:toproposedindexpath:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:targetindexpathformovefromitemat:toproposedindexpath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdelegate/collectionview%28_%3Atargetindexpathformovefromitemat%3Atoproposedindexpath%3A%29.json'
content_hash: 'sha256:8a8d0906d2617665'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDelegate](../uicollectionviewdelegate.md)

# collectionView(_:targetIndexPathForMoveFromItemAt:toProposedIndexPath:)

<sub>Instance Method</sub>

Asks the delegate for the index path to use when moving an item.

> [!warning] Deprecated
> Use [- collectionView:targetIndexPathForMoveOfItemFromOriginalIndexPath:atCurrentIndexPath:toProposedIndexPath:](<collectionview(__targetindexpathformoveofitemfromoriginalindexpath_atcurrentindexpath_toproposedindexpath_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, targetIndexPathForMoveFromItemAt currentIndexPath: IndexPath, toProposedIndexPath proposedIndexPath: IndexPath) -> IndexPath
```

## Parameters

- `collectionView` — The collection view making the request.

- `currentIndexPath` — The item’s original index path.

- `proposedIndexPath` — The proposed index path of the item.

## Return Value

The index path you want to use for the item. If you do not implement this method, the collection view uses the index path in the `proposedIndexPath` parameter.

## Discussion

During the interactive moving of an item, the collection view calls this method to see if you want to provide a different index path than the proposed path. You might use this method to prevent the user from dropping the item in an invalid location. For example, you might prevent the user from dropping the item in a specific section.

## See Also

### Deprecated

- [- collectionView:contextMenuConfigurationForItemAtIndexPath:point:](<collectionview(__contextmenuconfigurationforitemat_point_).md>) — Returns a context menu configuration for the item at a point. _(deprecated)_
- [- collectionView:previewForDismissingContextMenuWithConfiguration:](<collectionview(__previewfordismissingcontextmenuwithconfiguration_).md>) — Returns the destination view when dismissing a context menu. _(deprecated)_
- [- collectionView:previewForHighlightingContextMenuWithConfiguration:](<collectionview(__previewforhighlightingcontextmenuwithconfiguration_).md>) — Returns a view to override the default preview the collection view created. _(deprecated)_
- [- collectionView:shouldShowMenuForItemAtIndexPath:](<collectionview(__shouldshowmenuforitemat_).md>) — Asks the delegate if an action menu should be displayed for the specified item. _(deprecated)_
- [- collectionView:canPerformAction:forItemAtIndexPath:withSender:](<collectionview(__canperformaction_foritemat_withsender_).md>) — Asks the delegate if it can perform the specified action on an item in the collection view. _(deprecated)_
- [- collectionView:performAction:forItemAtIndexPath:withSender:](<collectionview(__performaction_foritemat_withsender_).md>) — Tells the delegate to perform the specified action on an item in the collection view. _(deprecated)_
