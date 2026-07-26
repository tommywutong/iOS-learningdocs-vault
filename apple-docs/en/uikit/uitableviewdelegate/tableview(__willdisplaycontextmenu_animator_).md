---
title: 'tableView(_:willDisplayContextMenu:animator:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdelegate/tableview(_:willdisplaycontextmenu:animator:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:willdisplaycontextmenu:animator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%28_%3Awilldisplaycontextmenu%3Aanimator%3A%29.json'
content_hash: 'sha256:358f6e90fc13f352'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView(_:willDisplayContextMenu:animator:)

<sub>Instance Method</sub>

Informs the delegate when a context menu will appear.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, willDisplayContextMenu configuration: UIContextMenuConfiguration, animator: (any UIContextMenuInteractionAnimating)?)
```

## Parameters

- `tableView` — The table view informing the delegate of this event.

- `configuration` — The configuration of the menu to display.

- `animator` — The animations to run alongside the appearance transition.

## See Also

### Managing context menus

- [Adding context menus in your app](../adding-context-menus-in-your-app.md) — Provide quick access to useful actions by adding context menus to your iOS app.
- [- tableView:contextMenuConfigurationForRowAtIndexPath:point:](<tableview(__contextmenuconfigurationforrowat_point_).md>) — Returns a context menu configuration for the row at a point.
- [- tableView:previewForDismissingContextMenuWithConfiguration:](<tableview(__previewfordismissingcontextmenuwithconfiguration_).md>) — Returns the destination view when dismissing a context menu.
- [- tableView:previewForHighlightingContextMenuWithConfiguration:](<tableview(__previewforhighlightingcontextmenuwithconfiguration_).md>) — Returns a view to override the default preview the table view created.
- [- tableView:willEndContextMenuInteractionWithConfiguration:animator:](<tableview(__willendcontextmenuinteraction_animator_).md>) — Informs the delegate when a context menu will disappear.
- [- tableView:willPerformPreviewActionForMenuWithConfiguration:animator:](<tableview(__willperformpreviewactionformenuwith_animator_).md>) — Informs the delegate when a user triggers a commit by tapping the preview.
