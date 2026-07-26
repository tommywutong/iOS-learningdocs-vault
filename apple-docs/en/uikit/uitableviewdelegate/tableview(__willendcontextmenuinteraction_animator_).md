---
title: 'tableView(_:willEndContextMenuInteraction:animator:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdelegate/tableview(_:willendcontextmenuinteraction:animator:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:willendcontextmenuinteraction:animator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%28_%3Awillendcontextmenuinteraction%3Aanimator%3A%29.json'
content_hash: 'sha256:8620f3bdd06b5a5c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView(_:willEndContextMenuInteraction:animator:)

<sub>Instance Method</sub>

Informs the delegate when a context menu will disappear.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, willEndContextMenuInteraction configuration: UIContextMenuConfiguration, animator: (any UIContextMenuInteractionAnimating)?)
```

## Parameters

- `tableView` — The table view informing the delegate of this event.

- `configuration` — The ending configuration.

- `animator` — The animations to run alongside the disappearance transition.

## See Also

### Managing context menus

- [Adding context menus in your app](../adding-context-menus-in-your-app.md) — Provide quick access to useful actions by adding context menus to your iOS app.
- [- tableView:contextMenuConfigurationForRowAtIndexPath:point:](<tableview(__contextmenuconfigurationforrowat_point_).md>) — Returns a context menu configuration for the row at a point.
- [- tableView:previewForDismissingContextMenuWithConfiguration:](<tableview(__previewfordismissingcontextmenuwithconfiguration_).md>) — Returns the destination view when dismissing a context menu.
- [- tableView:previewForHighlightingContextMenuWithConfiguration:](<tableview(__previewforhighlightingcontextmenuwithconfiguration_).md>) — Returns a view to override the default preview the table view created.
- [- tableView:willDisplayContextMenuWithConfiguration:animator:](<tableview(__willdisplaycontextmenu_animator_).md>) — Informs the delegate when a context menu will appear.
- [- tableView:willPerformPreviewActionForMenuWithConfiguration:animator:](<tableview(__willperformpreviewactionformenuwith_animator_).md>) — Informs the delegate when a user triggers a commit by tapping the preview.
