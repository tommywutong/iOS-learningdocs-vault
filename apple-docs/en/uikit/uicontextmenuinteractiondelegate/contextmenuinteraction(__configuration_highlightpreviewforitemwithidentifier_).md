---
title: 'contextMenuInteraction(_:configuration:highlightPreviewForItemWithIdentifier:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicontextmenuinteractiondelegate/contextmenuinteraction(_:configuration:highlightpreviewforitemwithidentifier:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicontextmenuinteractiondelegate/contextmenuinteraction(_:configuration:highlightpreviewforitemwithidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontextmenuinteractiondelegate/contextmenuinteraction%28_%3Aconfiguration%3Ahighlightpreviewforitemwithidentifier%3A%29.json'
content_hash: 'sha256:61fa58a9fc4a2c14'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIContextMenuInteractionDelegate](../uicontextmenuinteractiondelegate.md)

# contextMenuInteraction(_:configuration:highlightPreviewForItemWithIdentifier:)

<sub>Instance Method</sub>

Asks the delegate for a preview of the item with the specified identifier when a context-menu interaction begins.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func contextMenuInteraction(_ interaction: UIContextMenuInteraction, configuration: UIContextMenuConfiguration, highlightPreviewForItemWithIdentifier identifier: any NSCopying) -> UITargetedPreview?
```

## Parameters

- `interaction` — The context-menu interaction object.

- `configuration` — The configuration of the menu to present if the interaction proceeds.

- `identifier` — The identifier for the item to generate a preview for.

## Return Value

A targeted preview object corresponding to the item with the identifier to use during the menu’s highlight and presentation animation.

## Discussion

The system calls this method when a context-menu interaction begins. Implement this method to override the default highlight preview that the system generates for the item.

## See Also

### Customizing the preview animations

- [- contextMenuInteraction:configuration:dismissalPreviewForItemWithIdentifier:](<contextmenuinteraction(__configuration_dismissalpreviewforitemwithidentifier_).md>) — Asks the delegate for a preview of the item with the specified identifier when a context-menu interaction ends.
- [Adding menus and shortcuts to the menu bar and user interface](../adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md) — Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.
