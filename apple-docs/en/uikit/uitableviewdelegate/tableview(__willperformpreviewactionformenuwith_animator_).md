---
title: 'tableView(_:willPerformPreviewActionForMenuWith:animator:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdelegate/tableview(_:willperformpreviewactionformenuwith:animator:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:willperformpreviewactionformenuwith:animator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%28_%3Awillperformpreviewactionformenuwith%3Aanimator%3A%29.json'
content_hash: 'sha256:0104f44af82ede05'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView(_:willPerformPreviewActionForMenuWith:animator:)

<sub>Instance Method</sub>

Informs the delegate when a user triggers a commit by tapping the preview.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, willPerformPreviewActionForMenuWith configuration: UIContextMenuConfiguration, animator: any UIContextMenuInteractionCommitAnimating)
```

## Parameters

- `tableView` — The table view informing the delegate of this event.

- `configuration` — The configuration of the menu being displayed.

- `animator` — The animations to run alongside the commit transition.

## See Also

### Managing context menus

- [Adding context menus in your app](../adding-context-menus-in-your-app.md) — Provide quick access to useful actions by adding context menus to your iOS app.
- [- tableView:contextMenuConfigurationForRowAtIndexPath:point:](<tableview(__contextmenuconfigurationforrowat_point_).md>) — Returns a context menu configuration for the row at a point.
- [- tableView:previewForDismissingContextMenuWithConfiguration:](<tableview(__previewfordismissingcontextmenuwithconfiguration_).md>) — Returns the destination view when dismissing a context menu.
- [- tableView:previewForHighlightingContextMenuWithConfiguration:](<tableview(__previewforhighlightingcontextmenuwithconfiguration_).md>) — Returns a view to override the default preview the table view created.
- [- tableView:willDisplayContextMenuWithConfiguration:animator:](<tableview(__willdisplaycontextmenu_animator_).md>) — Informs the delegate when a context menu will appear.
- [- tableView:willEndContextMenuInteractionWithConfiguration:animator:](<tableview(__willendcontextmenuinteraction_animator_).md>) — Informs the delegate when a context menu will disappear.
