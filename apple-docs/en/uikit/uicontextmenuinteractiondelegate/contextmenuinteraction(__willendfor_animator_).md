---
title: 'contextMenuInteraction(_:willEndFor:animator:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicontextmenuinteractiondelegate/contextmenuinteraction(_:willendfor:animator:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicontextmenuinteractiondelegate/contextmenuinteraction(_:willendfor:animator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontextmenuinteractiondelegate/contextmenuinteraction%28_%3Awillendfor%3Aanimator%3A%29.json'
content_hash: 'sha256:cab4b85e62735f9a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIContextMenuInteractionDelegate](../uicontextmenuinteractiondelegate.md)

# contextMenuInteraction(_:willEndFor:animator:)

<sub>Instance Method</sub>

Informs the delegate when a menu display ends.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func contextMenuInteraction(_ interaction: UIContextMenuInteraction, willEndFor configuration: UIContextMenuConfiguration, animator: (any UIContextMenuInteractionAnimating)?)
```

## Parameters

- `interaction` — The interaction object that triggered the interaction.

- `configuration` — The context menu configuration.

- `animator` — The animator to configure custom animations.

## See Also

### Handling animations

- [- contextMenuInteraction:willDisplayMenuForConfiguration:animator:](<contextmenuinteraction(__willdisplaymenufor_animator_).md>) — Informs the delegate when a menu display begins.
- [UIContextMenuInteractionAnimating](../uicontextmenuinteractionanimating.md) — Methods adopted by system-supplied animator objects when interacting with context menus.
