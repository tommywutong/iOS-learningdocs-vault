---
title: 'collectionView(_:performAction:forItemAt:withSender:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+（13.0 起废弃）, iPadOS 6.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uicollectionviewdelegate/collectionview(_:performaction:foritemat:withsender:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:performaction:foritemat:withsender:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdelegate/collectionview%28_%3Aperformaction%3Aforitemat%3Awithsender%3A%29.json'
content_hash: 'sha256:bc4e695eb451ea3a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDelegate](../uicollectionviewdelegate.md)

# collectionView(_:performAction:forItemAt:withSender:)

<sub>Instance Method</sub>

Tells the delegate to perform the specified action on an item in the collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, performAction action: Selector, forItemAt indexPath: IndexPath, withSender sender: Any?)
```

## Parameters

- `collectionView` — The collection view object that is making the request.

- `action` — The selector representing the action to be performed.

- `indexPath` — The index path of the affected item.

- `sender` — The object that initiated the action.

## Discussion

If the user taps an action in the editing menu, the collection view calls this method. Your implementation of this method should do whatever is appropriate for the action. For example, for a copy action, it should extract the relevant item content and write it to the general pasteboard or an application (private) pasteboard.

For information about how to perform pasteboard-related operations, see [UIPasteboard](../uipasteboard.md).

## See Also

### Deprecated

- [- collectionView:targetIndexPathForMoveFromItemAtIndexPath:toProposedIndexPath:](<collectionview(__targetindexpathformovefromitemat_toproposedindexpath_).md>) — Asks the delegate for the index path to use when moving an item. _(deprecated)_
- [- collectionView:contextMenuConfigurationForItemAtIndexPath:point:](<collectionview(__contextmenuconfigurationforitemat_point_).md>) — Returns a context menu configuration for the item at a point. _(deprecated)_
- [- collectionView:previewForDismissingContextMenuWithConfiguration:](<collectionview(__previewfordismissingcontextmenuwithconfiguration_).md>) — Returns the destination view when dismissing a context menu. _(deprecated)_
- [- collectionView:previewForHighlightingContextMenuWithConfiguration:](<collectionview(__previewforhighlightingcontextmenuwithconfiguration_).md>) — Returns a view to override the default preview the collection view created. _(deprecated)_
- [- collectionView:shouldShowMenuForItemAtIndexPath:](<collectionview(__shouldshowmenuforitemat_).md>) — Asks the delegate if an action menu should be displayed for the specified item. _(deprecated)_
- [- collectionView:canPerformAction:forItemAtIndexPath:withSender:](<collectionview(__canperformaction_foritemat_withsender_).md>) — Asks the delegate if it can perform the specified action on an item in the collection view. _(deprecated)_
