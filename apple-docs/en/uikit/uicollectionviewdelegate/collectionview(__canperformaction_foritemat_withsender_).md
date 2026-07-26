---
title: 'collectionView(_:canPerformAction:forItemAt:withSender:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+（13.0 起废弃）, iPadOS 6.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uicollectionviewdelegate/collectionview(_:canperformaction:foritemat:withsender:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:canperformaction:foritemat:withsender:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdelegate/collectionview%28_%3Acanperformaction%3Aforitemat%3Awithsender%3A%29.json'
content_hash: 'sha256:68952dc75a3dd623'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDelegate](../uicollectionviewdelegate.md)

# collectionView(_:canPerformAction:forItemAt:withSender:)

<sub>Instance Method</sub>

Asks the delegate if it can perform the specified action on an item in the collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, canPerformAction action: Selector, forItemAt indexPath: IndexPath, withSender sender: Any?) -> Bool
```

## Parameters

- `collectionView` — The collection view object that is making the request.

- `action` — The selector identifying the action to be performed.

- `indexPath` — The index path of the affected item.

- `sender` — The object that wants to initiate the action.

## Return Value

[true](../../swift/true.md) if the command corresponding to action should appear in the editing menu or [false](../../swift/false.md) if it should not.

## Discussion

This method is invoked after the [- collectionView:shouldShowMenuForItemAtIndexPath:](<collectionview(__shouldshowmenuforitemat_).md>) method. It gives you the opportunity to exclude commands from the editing menu. For example, the user might have copied some content from one item and wants to paste it into another item that cannot accept the content. In such a case, your method could return [false](../../swift/false.md) to prevent the display of the relevant command.

If you do not implement this method, the default return value is [false](../../swift/false.md).

## See Also

### Deprecated

- [- collectionView:targetIndexPathForMoveFromItemAtIndexPath:toProposedIndexPath:](<collectionview(__targetindexpathformovefromitemat_toproposedindexpath_).md>) — Asks the delegate for the index path to use when moving an item. _(deprecated)_
- [- collectionView:contextMenuConfigurationForItemAtIndexPath:point:](<collectionview(__contextmenuconfigurationforitemat_point_).md>) — Returns a context menu configuration for the item at a point. _(deprecated)_
- [- collectionView:previewForDismissingContextMenuWithConfiguration:](<collectionview(__previewfordismissingcontextmenuwithconfiguration_).md>) — Returns the destination view when dismissing a context menu. _(deprecated)_
- [- collectionView:previewForHighlightingContextMenuWithConfiguration:](<collectionview(__previewforhighlightingcontextmenuwithconfiguration_).md>) — Returns a view to override the default preview the collection view created. _(deprecated)_
- [- collectionView:shouldShowMenuForItemAtIndexPath:](<collectionview(__shouldshowmenuforitemat_).md>) — Asks the delegate if an action menu should be displayed for the specified item. _(deprecated)_
- [- collectionView:performAction:forItemAtIndexPath:withSender:](<collectionview(__performaction_foritemat_withsender_).md>) — Tells the delegate to perform the specified action on an item in the collection view. _(deprecated)_
