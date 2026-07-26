---
title: 'contextMenuInteraction(_:willDisplayMenuFor:animator:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicontextmenuinteractiondelegate/contextmenuinteraction(_:willdisplaymenufor:animator:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicontextmenuinteractiondelegate/contextmenuinteraction(_:willdisplaymenufor:animator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontextmenuinteractiondelegate/contextmenuinteraction%28_%3Awilldisplaymenufor%3Aanimator%3A%29.json'
content_hash: 'sha256:00c00210e0a0fe57'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIContextMenuInteractionDelegate](../uicontextmenuinteractiondelegate.md)

# contextMenuInteraction(_:willDisplayMenuFor:animator:)

<sub>Instance Method</sub>

Informs the delegate when a menu display begins.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func contextMenuInteraction(_ interaction: UIContextMenuInteraction, willDisplayMenuFor configuration: UIContextMenuConfiguration, animator: (any UIContextMenuInteractionAnimating)?)
```

## Parameters

- `interaction` — The interaction object that triggered the interaction.

- `configuration` — The context menu configuration.

- `animator` — The animator to configure custom animations.

## See Also

### Handling animations

- [- contextMenuInteraction:willEndForConfiguration:animator:](<contextmenuinteraction(__willendfor_animator_).md>) — Informs the delegate when a menu display ends.
- [UIContextMenuInteractionAnimating](../uicontextmenuinteractionanimating.md) — Methods adopted by system-supplied animator objects when interacting with context menus.
