---
title: 'contextMenuInteraction(_:configuration:dismissalPreviewForItemWithIdentifier:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicontextmenuinteractiondelegate/contextmenuinteraction(_:configuration:dismissalpreviewforitemwithidentifier:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicontextmenuinteractiondelegate/contextmenuinteraction(_:configuration:dismissalpreviewforitemwithidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontextmenuinteractiondelegate/contextmenuinteraction%28_%3Aconfiguration%3Adismissalpreviewforitemwithidentifier%3A%29.json'
content_hash: 'sha256:9acf8cbb21e84839'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIContextMenuInteractionDelegate](../uicontextmenuinteractiondelegate.md)

# contextMenuInteraction(_:configuration:dismissalPreviewForItemWithIdentifier:)

<sub>Instance Method</sub>

Asks the delegate for a preview of the item with the specified identifier when a context-menu interaction ends.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func contextMenuInteraction(_ interaction: UIContextMenuInteraction, configuration: UIContextMenuConfiguration, dismissalPreviewForItemWithIdentifier identifier: any NSCopying) -> UITargetedPreview?
```

## Parameters

- `interaction` — The context-menu interaction object.

- `configuration` — The configuration of the menu to dismiss.

- `identifier` — The identifier for the item to generate a preview for.

## Return Value

A targeted preview object corresponding to the item with the identifier to use during the menu’s dismissal animation.

## Discussion

The system calls this method when a context-menu dismissal occurs. Implement this method to override the default dismissal preview that the system generates for the item.

## See Also

### Customizing the preview animations

- [- contextMenuInteraction:configuration:highlightPreviewForItemWithIdentifier:](<contextmenuinteraction(__configuration_highlightpreviewforitemwithidentifier_).md>) — Asks the delegate for a preview of the item with the specified identifier when a context-menu interaction begins.
- [Adding menus and shortcuts to the menu bar and user interface](../adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md) — Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.
