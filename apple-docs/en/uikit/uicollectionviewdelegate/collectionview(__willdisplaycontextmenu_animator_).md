---
title: 'collectionView(_:willDisplayContextMenu:animator:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.2+, iPadOS 13.2+, Mac Catalyst 13.2+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdelegate/collectionview(_:willdisplaycontextmenu:animator:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:willdisplaycontextmenu:animator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdelegate/collectionview%28_%3Awilldisplaycontextmenu%3Aanimator%3A%29.json'
content_hash: 'sha256:360ae9f2ac99efba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDelegate](../uicollectionviewdelegate.md)

# collectionView(_:willDisplayContextMenu:animator:)

<sub>Instance Method</sub>

Informs the delegate when a context menu will appear.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, willDisplayContextMenu configuration: UIContextMenuConfiguration, animator: (any UIContextMenuInteractionAnimating)?)
```

## Parameters

- `collectionView` — The collection view that informs the delegate of this event.

- `configuration` — The configuration of the menu to display.

- `animator` — The animations to run alongside the appearance transition.

## See Also

### Managing context menus

- [Adding context menus in your app](../adding-context-menus-in-your-app.md) — Provide quick access to useful actions by adding context menus to your iOS app.
- [- collectionView:willEndContextMenuInteractionWithConfiguration:animator:](<collectionview(__willendcontextmenuinteraction_animator_).md>) — Informs the delegate when a context menu will disappear.
- [- collectionView:willPerformPreviewActionForMenuWithConfiguration:animator:](<collectionview(__willperformpreviewactionformenuwith_animator_).md>) — Informs the delegate when a user triggers a commit by tapping the preview.
- [- collectionView:contextMenuConfigurationForItemsAtIndexPaths:point:](<collectionview(__contextmenuconfigurationforitemsat_point_).md>) — Asks the delegate for a context-menu configuration for the items at the specified index paths.
- [- collectionView:contextMenuConfiguration:highlightPreviewForItemAtIndexPath:](<collectionview(__contextmenuconfiguration_highlightpreviewforitemat_).md>) — Asks the delegate for a preview of the item at the specified index path when a context-menu interaction begins.
- [- collectionView:contextMenuConfiguration:dismissalPreviewForItemAtIndexPath:](<collectionview(__contextmenuconfiguration_dismissalpreviewforitemat_).md>) — Asks the delegate for a preview of the item at the specified index path when a context-menu interaction ends.
