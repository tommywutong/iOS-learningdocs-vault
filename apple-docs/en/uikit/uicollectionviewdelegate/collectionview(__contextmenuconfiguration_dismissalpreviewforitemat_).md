---
title: 'collectionView(_:contextMenuConfiguration:dismissalPreviewForItemAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdelegate/collectionview(_:contextmenuconfiguration:dismissalpreviewforitemat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:contextmenuconfiguration:dismissalpreviewforitemat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdelegate/collectionview%28_%3Acontextmenuconfiguration%3Adismissalpreviewforitemat%3A%29.json'
content_hash: 'sha256:3b5a08f8892b025d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDelegate](../uicollectionviewdelegate.md)

# collectionView(_:contextMenuConfiguration:dismissalPreviewForItemAt:)

<sub>Instance Method</sub>

Asks the delegate for a preview of the item at the specified index path when a context-menu interaction ends.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, contextMenuConfiguration configuration: UIContextMenuConfiguration, dismissalPreviewForItemAt indexPath: IndexPath) -> UITargetedPreview?
```

## Parameters

- `collectionView` — The collection view containing the item.

- `configuration` — The configuration of the menu to dismiss.

- `indexPath` — The index path of the item where the menu dismissal occurs.

## Return Value

A targeted preview object corresponding to the item at the index path to use during the menu’s dismissal animation.

## Discussion

The system calls this method when a context menu dismisses from the collection view. Implement this method to override the default dismissal preview that the collection view generates for the item at `indexPath`.

## See Also

### Managing context menus

- [Adding context menus in your app](../adding-context-menus-in-your-app.md) — Provide quick access to useful actions by adding context menus to your iOS app.
- [- collectionView:willDisplayContextMenuWithConfiguration:animator:](<collectionview(__willdisplaycontextmenu_animator_).md>) — Informs the delegate when a context menu will appear.
- [- collectionView:willEndContextMenuInteractionWithConfiguration:animator:](<collectionview(__willendcontextmenuinteraction_animator_).md>) — Informs the delegate when a context menu will disappear.
- [- collectionView:willPerformPreviewActionForMenuWithConfiguration:animator:](<collectionview(__willperformpreviewactionformenuwith_animator_).md>) — Informs the delegate when a user triggers a commit by tapping the preview.
- [- collectionView:contextMenuConfigurationForItemsAtIndexPaths:point:](<collectionview(__contextmenuconfigurationforitemsat_point_).md>) — Asks the delegate for a context-menu configuration for the items at the specified index paths.
- [- collectionView:contextMenuConfiguration:highlightPreviewForItemAtIndexPath:](<collectionview(__contextmenuconfiguration_highlightpreviewforitemat_).md>) — Asks the delegate for a preview of the item at the specified index path when a context-menu interaction begins.
