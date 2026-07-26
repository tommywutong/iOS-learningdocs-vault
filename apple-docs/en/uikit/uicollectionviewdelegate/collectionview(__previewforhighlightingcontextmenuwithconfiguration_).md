---
title: 'collectionView(_:previewForHighlightingContextMenuWithConfiguration:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（16.0 起废弃）, iPadOS 13.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uicollectionviewdelegate/collectionview(_:previewforhighlightingcontextmenuwithconfiguration:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:previewforhighlightingcontextmenuwithconfiguration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdelegate/collectionview%28_%3Apreviewforhighlightingcontextmenuwithconfiguration%3A%29.json'
content_hash: 'sha256:688d0ea139a6aae3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDelegate](../uicollectionviewdelegate.md)

# collectionView(_:previewForHighlightingContextMenuWithConfiguration:)

<sub>Instance Method</sub>

Returns a view to override the default preview the collection view created.

> [!warning] Deprecated
> Use [- collectionView:contextMenuConfiguration:highlightPreviewForItemAtIndexPath:](<collectionview(__contextmenuconfiguration_highlightpreviewforitemat_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, previewForHighlightingContextMenuWithConfiguration configuration: UIContextMenuConfiguration) -> UITargetedPreview?
```

## Parameters

- `collectionView` — The collection view object requesting this information.

- `configuration` — The configuration of the menu being highlighted.

## Return Value

A targeted preview object describing the highlight preview.

## See Also

### Deprecated

- [- collectionView:targetIndexPathForMoveFromItemAtIndexPath:toProposedIndexPath:](<collectionview(__targetindexpathformovefromitemat_toproposedindexpath_).md>) — Asks the delegate for the index path to use when moving an item. _(deprecated)_
- [- collectionView:contextMenuConfigurationForItemAtIndexPath:point:](<collectionview(__contextmenuconfigurationforitemat_point_).md>) — Returns a context menu configuration for the item at a point. _(deprecated)_
- [- collectionView:previewForDismissingContextMenuWithConfiguration:](<collectionview(__previewfordismissingcontextmenuwithconfiguration_).md>) — Returns the destination view when dismissing a context menu. _(deprecated)_
- [- collectionView:shouldShowMenuForItemAtIndexPath:](<collectionview(__shouldshowmenuforitemat_).md>) — Asks the delegate if an action menu should be displayed for the specified item. _(deprecated)_
- [- collectionView:canPerformAction:forItemAtIndexPath:withSender:](<collectionview(__canperformaction_foritemat_withsender_).md>) — Asks the delegate if it can perform the specified action on an item in the collection view. _(deprecated)_
- [- collectionView:performAction:forItemAtIndexPath:withSender:](<collectionview(__performaction_foritemat_withsender_).md>) — Tells the delegate to perform the specified action on an item in the collection view. _(deprecated)_
