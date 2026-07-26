---
title: 'collectionView(_:shouldShowMenuForItemAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+（13.0 起废弃）, iPadOS 6.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uicollectionviewdelegate/collectionview(_:shouldshowmenuforitemat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:shouldshowmenuforitemat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdelegate/collectionview%28_%3Ashouldshowmenuforitemat%3A%29.json'
content_hash: 'sha256:483c9690392b38bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDelegate](../uicollectionviewdelegate.md)

# collectionView(_:shouldShowMenuForItemAt:)

<sub>Instance Method</sub>

Asks the delegate if an action menu should be displayed for the specified item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, shouldShowMenuForItemAt indexPath: IndexPath) -> Bool
```

## Parameters

- `collectionView` — The collection view object that is making the request.

- `indexPath` — The index path of the affected item.

## Return Value

[true](../../swift/true.md) if the editing menu should be shown positioned near the item and pointing to it or [false](../../swift/false.md) if it should not.

## Discussion

If the user tap-holds a certain item in the collection view, this method (if implemented) is invoked first. Return [true](../../swift/true.md) if you want to permit the editing menu to be displayed. Return [false](../../swift/false.md) if the editing menu shouldn’t be shown—for example, you might return [false](../../swift/false.md) if the corresponding item contains data that should not be copied or pasted over.

If you do not implement this method, the default return value is [false](../../swift/false.md).

## See Also

### Deprecated

- [- collectionView:targetIndexPathForMoveFromItemAtIndexPath:toProposedIndexPath:](<collectionview(__targetindexpathformovefromitemat_toproposedindexpath_).md>) — Asks the delegate for the index path to use when moving an item. _(deprecated)_
- [- collectionView:contextMenuConfigurationForItemAtIndexPath:point:](<collectionview(__contextmenuconfigurationforitemat_point_).md>) — Returns a context menu configuration for the item at a point. _(deprecated)_
- [- collectionView:previewForDismissingContextMenuWithConfiguration:](<collectionview(__previewfordismissingcontextmenuwithconfiguration_).md>) — Returns the destination view when dismissing a context menu. _(deprecated)_
- [- collectionView:previewForHighlightingContextMenuWithConfiguration:](<collectionview(__previewforhighlightingcontextmenuwithconfiguration_).md>) — Returns a view to override the default preview the collection view created. _(deprecated)_
- [- collectionView:canPerformAction:forItemAtIndexPath:withSender:](<collectionview(__canperformaction_foritemat_withsender_).md>) — Asks the delegate if it can perform the specified action on an item in the collection view. _(deprecated)_
- [- collectionView:performAction:forItemAtIndexPath:withSender:](<collectionview(__performaction_foritemat_withsender_).md>) — Tells the delegate to perform the specified action on an item in the collection view. _(deprecated)_
