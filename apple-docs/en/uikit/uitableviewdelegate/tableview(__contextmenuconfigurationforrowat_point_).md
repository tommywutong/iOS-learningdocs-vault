---
title: 'tableView(_:contextMenuConfigurationForRowAt:point:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdelegate/tableview(_:contextmenuconfigurationforrowat:point:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:contextmenuconfigurationforrowat:point:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%28_%3Acontextmenuconfigurationforrowat%3Apoint%3A%29.json'
content_hash: 'sha256:60c349c701ecc431'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView(_:contextMenuConfigurationForRowAt:point:)

<sub>Instance Method</sub>

Returns a context menu configuration for the row at a point.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, contextMenuConfigurationForRowAt indexPath: IndexPath, point: CGPoint) -> UIContextMenuConfiguration?
```

## Parameters

- `tableView` — The table view containing the row.

- `indexPath` — The index path of the row.

- `point` — The location of the interaction in the table view’s coordinate space.

## Return Value

A context menu configuration for the `indexPath`.

## Discussion

Use this method to provide a [UIContextMenuConfiguration](../uicontextmenuconfiguration.md) describing the menu to present. Return `nil` to prevent the interaction from beginning. Return an empty configuration to begin the interaction and then fail with a cancellation effect. Use the empty configuration to indicate to users that it’s possible for this element to present a menu, but that there are no actions to present at this time.

## See Also

### Managing context menus

- [Adding context menus in your app](../adding-context-menus-in-your-app.md) — Provide quick access to useful actions by adding context menus to your iOS app.
- [- tableView:previewForDismissingContextMenuWithConfiguration:](<tableview(__previewfordismissingcontextmenuwithconfiguration_).md>) — Returns the destination view when dismissing a context menu.
- [- tableView:previewForHighlightingContextMenuWithConfiguration:](<tableview(__previewforhighlightingcontextmenuwithconfiguration_).md>) — Returns a view to override the default preview the table view created.
- [- tableView:willDisplayContextMenuWithConfiguration:animator:](<tableview(__willdisplaycontextmenu_animator_).md>) — Informs the delegate when a context menu will appear.
- [- tableView:willEndContextMenuInteractionWithConfiguration:animator:](<tableview(__willendcontextmenuinteraction_animator_).md>) — Informs the delegate when a context menu will disappear.
- [- tableView:willPerformPreviewActionForMenuWithConfiguration:animator:](<tableview(__willperformpreviewactionformenuwith_animator_).md>) — Informs the delegate when a user triggers a commit by tapping the preview.
