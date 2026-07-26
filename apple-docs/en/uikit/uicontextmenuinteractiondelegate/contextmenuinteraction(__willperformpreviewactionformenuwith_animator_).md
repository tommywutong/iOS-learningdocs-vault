---
title: 'contextMenuInteraction(_:willPerformPreviewActionForMenuWith:animator:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicontextmenuinteractiondelegate/contextmenuinteraction(_:willperformpreviewactionformenuwith:animator:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicontextmenuinteractiondelegate/contextmenuinteraction(_:willperformpreviewactionformenuwith:animator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontextmenuinteractiondelegate/contextmenuinteraction%28_%3Awillperformpreviewactionformenuwith%3Aanimator%3A%29.json'
content_hash: 'sha256:28f92f77ee22fa08'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIContextMenuInteractionDelegate](../uicontextmenuinteractiondelegate.md)

# contextMenuInteraction(_:willPerformPreviewActionForMenuWith:animator:)

<sub>Instance Method</sub>

Informs the delegate when a preview action begins.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func contextMenuInteraction(_ interaction: UIContextMenuInteraction, willPerformPreviewActionForMenuWith configuration: UIContextMenuConfiguration, animator: any UIContextMenuInteractionCommitAnimating)
```

## Parameters

- `interaction` — The interaction object that triggered the interaction.

- `configuration` — The context menu configuration.

- `animator` — The animator to configure custom animations.

## See Also

### Responding to the menu’s appearance

- [UIContextMenuInteractionCommitAnimating](../uicontextmenuinteractioncommitanimating.md) — Methods adopted by system-supplied animator objects when committing preview-related animations.
